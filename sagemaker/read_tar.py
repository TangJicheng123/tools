import datetime
import time
import tarfile

def extract_tar_files(archive_filename):
    i = 0
    try:
        with tarfile.open(archive_filename, 'r') as tar:
            for member in tar.getmembers():
                # 忽略目录，只处理文件
                if member.isfile():
                    file_data = tar.extractfile(member)
                    if file_data:
                        content = file_data.read()
                        i += 1
                        print(f"[{i}] File name: {member.name}")
                        # print(f"Content:\n{content}\n")
    except tarfile.TarError as e:
        print(f"Error while extracting the tar file: {e}")

archive_filename = '/home/ec2-user/SageMaker/s3mount/users/tangjicheng/p2.tar'
print(f"[{datetime.datetime.now()}] start")
start_time = time.time()

extract_tar_files(archive_filename)

print(f"[{datetime.datetime.now()}] end")
end_time = time.time()

cost_time = end_time - start_time
print(f"cost: {cost_time}")
