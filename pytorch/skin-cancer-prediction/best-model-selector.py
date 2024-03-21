import torch
from model import NeuralNetwork
from dataloader import SkinCancerPredictionDatasetLoader

torch.cuda.empty_cache()

model = NeuralNetwork()

model.load_state_dict(torch.load('models/model.pth', map_location=torch.device('cpu')), strict=False)


test_dataset = SkinCancerPredictionDatasetLoader('./train')