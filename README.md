FashionMNIST ResNet18 Transfer Learning Comparison
이 저장소는 PyTorch와 timm 라이브러리를 사용하여 ResNet18 모델로 FashionMNIST 데이터셋을 분류하는 실험 코드를 담고 있습니다.

주요 목적은 사전 학습된(Pretrained) 모델의 Feature Extractor 성능과 무작위로 초기화된(Randomized) Feature Extractor의 성능을 비교하는 것입니다. 두 경우 모두 Backbone 네트워크의 가중치를 고정(Freeze)하고, 마지막 분류 레이어(Fully Connected Layer)만 학습시켜 성능 차이를 확인합니다.

📋 프로젝트 개요
- 모델(Architecture): ResNet18 (via timm)

- 데이터셋(Dataset): FashionMNIST (10 Classes, 1 Channel)

- 실험 조건:
-   1. Pretrained: ImageNet으로 사전 학습된 가중치 사용 + Backbone Freeze + FC Layer 학습
    2. Random-init: 무작위 가중치 초기화 + Backbone Freeze + FC Layer 학습

- 목표: 사전 학습된 Feature Extractor가 단순한 이미지를 분류하는 데에도 얼마나 유효한지 검증

🛠 요구 사항 (Requirements)
실행을 위해 다음의 라이브러리가 필요합니다.

- Python 3.8+
- PyTorch >= 2.0.0
- Torchvision >= 0.15.0
- timm >= 0.9.0

🚀 설치 및 실행 (Installation & Usage)
1. 저장소 클론 (Clone)
```Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. 의존성 설치 (Install Dependencies)

```Bash
pip install -r requirements.txt
```
3. 학습 실행 (Run Training)
```Bash
python train.py
```
실행 시 자동으로 ./data 폴더에 데이터셋을 다운로드하고 학습을 시작합니다.

📂 파일 구조 (Directory Structure)
```
.
├── model.py            # timm을 이용한 ResNet18 모델 생성 및 Layer Freeze 설정
├── train.py            # 데이터 로드, 학습 및 테스트 루프, 메인 실행 코드
├── requirements.txt    # 필요 라이브러리 목록
├── .gitignore          # Git 제외 파일 설정
└── README.md           # 프로젝트 설명
```
🔍 코드 설명 (Code Details)
model.py
- timm.create_model을 사용하여 ResNet18을 불러옵니다.

- FashionMNIST는 흑백 이미지이므로 in_chans=1로 설정합니다.

- Freeze Logic: 모든 파라미터의 requires_grad를 False로 설정한 뒤, model.fc (분류기)의 파라미터만 True로 변경하여 Backbone을 고정합니다.

train.py
- Transforms: 이미지를 32x32로 리사이즈하고 정규화를 수행합니다.

- Optimizer: AdamW를 사용하며, 최적화 대상은 model.fc.parameters()로 한정됩니다.

- Comparison:
-   1. Pretrained Feature Extractor 모드로 학습 및 평가
    2. Random-init Feature Extractor 모드로 학습 및 평가

📊 예상 결과 (Expected Results)
코드를 실행하면 다음과 같은 양상의 로그를 확인할 수 있습니다.
- Pretrained: Backbone이 이미지 특징(Edge, Texture 등)을 잘 추출하도록 학습되어 있으므로, FC Layer만 학습해도 높은 정확도를 보입니다.
- Random: Backbone이 랜덤한 상태에서 고정(Freeze)되어 있으므로, 특징 추출이 제대로 이루어지지 않아 정확도가 매우 낮게 나옵니다 (Feature Extractor로서의 역할을 못함).
```Plaintext
[pretrained] Epoch 3/3 | Train Acc 85.xx% | Test Acc 84.xx%
...
[random] Epoch 3/3 | Train Acc 10.xx% | Test Acc 10.xx%
```
📜 License
This project is open-sourced under the MIT license.
