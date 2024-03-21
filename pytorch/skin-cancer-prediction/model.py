from torch import nn


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.linear_relu_stack = nn.Sequential(
            nn.Conv2d(3, 96, (11,11), stride=4), # 30 filtros / 90 imagenes de 224 - 19 (px - filtro - 1)  osea 224 - 19 = 205
            nn.MaxPool2d((3,3)), # divimos entre el 5 // 41 x 41
            nn.Conv2d(96, 256, (3,3), padding=2), ## 240 imagenes de 41 - 4 (px - filtro - 1)  osea 41 - 4 = 37,
            nn.MaxPool2d((3,3), stride=2), # divimos entre el 3 // 12 x 12
            nn.Conv2d(256, 256, (3,3), padding=2), ## 240 imagenes de 41 - 4 (px - filtro - 1)  osea 41 - 4 = 37
            nn.MaxPool2d((3,3), stride=2), # divimos entre el 3 // 12 x 12
            nn.Flatten(),

            nn.Linear(6400, 3000),
            nn.ReLU(),
            nn.Linear(3000, 300),
            nn.ReLU(),
            nn.Linear(300, 30),
            nn.ReLU(),

        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits