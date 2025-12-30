import timm
import torch

def build_model(pretrained: bool, device):
    model = timm.create_model(
        "resnet18",
        pretrained=pretrained,
        num_classes=10,
        in_chans=1
    ).to(device)

    for p in model.parameters():
        p.requires_grad = False
    for p in model.fc.parameters():
        p.requires_grad = True

    return model
