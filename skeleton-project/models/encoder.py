import tensorflow as tf


# 문제
class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        # [Do it yourself] 학습이 완료된 ResNet-152에서 fully connected layer의 가장 마지막 layer를 제거합니다.
        # Hint: https://stackoverflow.com/questions/52548174/how-to-remove-the-last-fc-layer-from-a-resnet-model-in-pytorch
        # Pretrained 된 모델에서 feature을 뽑을 때 흔히 사용하는 방법입니다.
        # 링크에서 등장하는 asterisk(*)는 Unpacking 하여 layer별로 분리하는 역할을 담당합니다

        resnet = models.resnet152(pretrained=True)
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)  # *은 리스트형태로 되어있는걸 다 풀어서 넣어주는역할

        # 마지막 layer를 제거한 resnet에서 뽑아낸 feature를 fully connected layer를 붙여 embed_size vector가 출력이 되도록 합니다.
        self.linear = nn.Linear(resnet.fc.in_features, embed_size)

        # [Do it yourself] LSTM에 넣어줄 input은 vector형태이므로 1D Batch normalization을 해줍니다.(momentum은 0.01로 해주세요)
        # https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html
        self.bn = nn.BatchNorm1d(embed_size, momentum=0.01)

    def forward(self, images):
        # 입력 이미지로부터 feature vector를 뽑아냅니다
        with torch.no_grad():
            features = self.resnet(images)
        features = features.reshape(features.size(0), -1)
        features = self.bn(self.linear(features))
        return features
