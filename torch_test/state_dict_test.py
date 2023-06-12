import torch
import torch.nn as nn
import torchvision.models as models

class ResNetWithPrint(nn.Module):
    def __init__(self, num_classes):
        super(ResNetWithPrint, self).__init__()
        self.resnet = models.resnet50(pretrained=False)
        self.fc = nn.Linear(2048, num_classes)

    def forward(self, x):
        x = self.resnet(x)
        x = self.fc(x)
        return x

# 创建ResNet模型并打印state_dict中每个参数的名称
model = ResNetWithPrint(num_classes=1000)
state_dict = model.state_dict()
for name, param in state_dict.items():
    print(name)

# 输出state_dict中每个参数的名称
