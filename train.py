# train.py
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

from model import build_model


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    BATCH_SIZE = 64
    EPOCHS = 15
    LR = 1e-3

    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    train_dataset = torchvision.datasets.FashionMNIST(
        "./data", train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.FashionMNIST(
        "./data", train=False, download=True, transform=transform
    )

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    def train_and_test(model, name: str):
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.AdamW(model.fc.parameters(), lr=LR, weight_decay=1e-2)

        for epoch in range(EPOCHS):
            model.train()
            correct, total = 0, 0
            train_loss_sum = 0.0

            for x, y in train_loader:
                x, y = x.to(device), y.to(device)

                optimizer.zero_grad()
                out = model(x)
                loss = criterion(out, y)
                loss.backward()
                optimizer.step()

                train_loss_sum += loss.item()
                pred = out.argmax(1)
                total += y.size(0)
                correct += (pred == y).sum().item()

            train_acc = 100 * correct / total
            train_loss = train_loss_sum / len(train_loader)

            model.eval()
            correct, total = 0, 0
            test_loss_sum = 0.0

            with torch.no_grad():
                for x, y in test_loader:
                    x, y = x.to(device), y.to(device)
                    out = model(x)
                    loss = criterion(out, y)

                    test_loss_sum += loss.item()
                    pred = out.argmax(1)
                    total += y.size(0)
                    correct += (pred == y).sum().item()

            test_acc = 100 * correct / total
            test_loss = test_loss_sum / len(test_loader)

            print(
                f"[{name}] Epoch {epoch+1}/{EPOCHS} | "
                f"Train Loss {train_loss:.4f} | Train Acc {train_acc:.2f}% | "
                f"Test Loss {test_loss:.4f} | Test Acc {test_acc:.2f}%"
            )

    print("=== Pretrained Feature Extractor ===")
    model_pre = build_model(pretrained=True, device=device)
    train_and_test(model_pre, "pretrained")

    print("\n=== Random-init Feature Extractor ===")
    model_rand = build_model(pretrained=False, device=device)
    train_and_test(model_rand, "random")


if __name__ == "__main__":
    main()