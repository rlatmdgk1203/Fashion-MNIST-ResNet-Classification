🧠 Python Deep Learning Training Project

Python과 PyTorch를 사용하여 이미지 분류 모델을 학습하고 평가하는 프로젝트입니다.
모델 정의(model.py)와 학습 로직(train.py)을 분리하여 구현하였습니다.

📂 Project Structure
.
├── model.py            # 모델 구조 정의
├── train.py            # 학습 및 평가 코드
├── requirements.txt    # 필요한 라이브러리 목록
├── README.md
├── data/               # 데이터셋 (GitHub에는 포함되지 않음)
├── venv/               # 가상환경 (GitHub에는 포함되지 않음)
└── __pycache__/        # 캐시 파일 (GitHub에는 포함되지 않음)

⚙️ Environment Setup
1️⃣ Python 버전

Python 3.8 이상 권장

2️⃣ 가상환경 생성 및 활성화
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ 라이브러리 설치
pip install -r requirements.txt

📊 Dataset

데이터셋은 data/ 디렉토리에 위치해야 합니다.

데이터 용량 및 라이선스 문제로 GitHub에는 업로드하지 않았습니다.

train.py 실행 전 데이터 경로를 확인해주세요.

🚀 Training

아래 명령어로 모델 학습을 실행할 수 있습니다.

python train.py


학습 과정에서:

모델이 학습 데이터로 학습됨

테스트 데이터로 성능 평가 수행

콘솔에 loss / accuracy 출력

🧩 Model Description

model.py

PyTorch 기반 모델 구조 정의

분류 문제를 위한 신경망 구성

train.py

데이터 로딩

학습 루프 (forward / backward)

평가 로직 포함

🛠 Requirements

주요 라이브러리:

torch

torchvision

numpy
(자세한 목록은 requirements.txt 참고)

📌 Notes

venv/, data/, __pycache__/는 .gitignore로 관리됩니다.

실험 재현을 위해 requirements.txt를 반드시 사용해주세요.
