#!/bin/bash

set -ex

# OVERVIEW
# This script stops a SageMaker notebook once it's idle for more than 1 hour (default time)
# You can change the idle time for stop using the environment variable below.
# If you want the notebook the stop only if no browsers are open, remove the --ignore-connections flag
#
# Note that this script will fail if either condition is not met
#   1. Ensure the Notebook Instance has internet connectivity to fetch the example config
#   2. Ensure the Notebook Instance execution role permissions to SageMaker:StopNotebookInstance to stop the notebook
#       and SageMaker:DescribeNotebookInstance to describe the notebook.
#

# PARAMETERS
IDLE_TIME=60

BUCKET="staging-g123-ai"
RESOURCE_NAME=$(jq -r .ResourceName </opt/ml/metadata/resource-metadata.json)
S3_CONFIG_PATH="s3://$BUCKET/operations/$RESOURCE_NAME"
LOCAL_CONFIG_PATH="$RESOURCE_NAME"
DEFAULT_FILE="default_requirements.txt"
GUAJI_FILE="$S3_CONFIG_PATH/guaji"

# Create the guaji command
echo "#!/bin/bash" | sudo tee /usr/local/bin/guaji >/dev/null
echo "sudo touch /guaji" | sudo tee -a /usr/local/bin/guaji >/dev/null
echo "aws s3 cp /guaji $GUAJI_FILE" | sudo tee -a /usr/local/bin/guaji >/dev/null
sudo chmod +x /usr/local/bin/guaji

# Create the buguaji command
echo "#!/bin/bash" | sudo tee /usr/local/bin/buguaji >/dev/null
echo "aws s3 rm $GUAJI_FILE" | sudo tee -a /usr/local/bin/buguaji >/dev/null
sudo chmod +x /usr/local/bin/buguaji

echo "Fetching the autostop script"
aws s3 cp "s3://staging-g123-ai/operations/idle-detection.py" ./
aws s3 cp "s3://staging-g123-ai/operations/$DEFAULT_FILE" ./

echo "Download the custom config files"
mkdir -p "$LOCAL_CONFIG_PATH"

if aws s3 ls "$S3_CONFIG_PATH" 2>/dev/null; then
    aws s3 cp "$S3_CONFIG_PATH" "$LOCAL_CONFIG_PATH" --recursive
else
    echo "The path does not exist: $S3_CONFIG_PATH"
fi
echo "Detecting Python install with boto3 install"

# Find which install has boto3 and use that to run the cron command. So will use default when available
# Redirect stderr as it is unneeded
CONDA_PYTHON_DIR=$(source /home/ec2-user/anaconda3/bin/activate /home/ec2-user/anaconda3/envs/JupyterSystemEnv && which python)
if $CONDA_PYTHON_DIR -c "import boto3" 2>/dev/null; then
    PYTHON_DIR=$CONDA_PYTHON_DIR
elif /usr/bin/python -c "import boto3" 2>/dev/null; then
    PYTHON_DIR='/usr/bin/python'
else
    # If no boto3 just quit because the script won't work
    echo "No boto3 found in Python or Python3. Exiting..."
    exit 1
fi

echo "Found boto3 at $PYTHON_DIR"

echo "Start installing the custom config"

# if [ -e "$LOCAL_CONFIG_PATH/requirements.txt" ]; then
#     echo "Installing python packages from requirements.txt"
#     grep -vxFf default_requirements.txt "$LOCAL_CONFIG_PATH/requirements.txt" > requirements.txt
#     $PYTHON_DIR -m pip install -r requirements.txt
# fi

# Execute shell scripts one by one
if ls "$LOCAL_CONFIG_PATH"/*.sh 1>/dev/null 2>&1; then
    echo "Executing shell scripts"
    for file in "$LOCAL_CONFIG_PATH"/*.sh; do
        bash "$file"
    done
fi

echo "Starting the SageMaker autostop script in cron"

(
    crontab -l 2>/dev/null
    echo "*/1 * * * * $PYTHON_DIR $PWD/idle-detection.py --time $IDLE_TIME --ignore-connections >> /var/log/jupyter.log"
) | crontab -
# (crontab -l 2>/dev/null; echo "*/1 * * * * $PYTHON_DIR -m pip freeze > requirements.txt && aws s3 cp requirements.txt $S3_CONFIG_PATH/") | crontab -

# install s3fs for mounting s3
sudo amazon-linux-extras install -y epel
sudo yum install -y s3fs-fuse fuse

# mount s3
sudo -u ec2-user -i <<EOF
mkdir -p /home/ec2-user/SageMaker/s3mount
s3fs -o iam_role=auto staging-g123-ai-disk /home/ec2-user/SageMaker/s3mount
EOF
