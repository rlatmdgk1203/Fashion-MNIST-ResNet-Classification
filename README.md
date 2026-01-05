# 🧠 Python Deep Learning Training Project

Python과 PyTorch를 사용하여 이미지 분류 모델을 학습하고 평가하는 프로젝트입니다.  
모델 정의(`model.py`)와 학습 로직(`train.py`)을 분리하여 구현했습니다.

---

## 📂 Project Structure

.
├── model.py # 모델 구조 정의
├── train.py # 학습 및 평가 코드
├── requirements.txt # 필요한 라이브러리 목록
├── README.md
├── data/ # 데이터셋 (GitHub에는 포함하지 않음)
├── venv/ # 가상환경 (GitHub에는 포함하지 않음)
└── pycache/ # 캐시 파일 (GitHub에는 포함하지 않음)


---

## ⚙️ Environment Setup

### 1️⃣ Python 버전
- Python 3.8 이상 권장

### 2️⃣ 가상환경 생성 및 활성화

```bash
python -m venv venv

venv\Scripts\activate

source venv/bin/activate

pip install -r requirements.txt

📊 Dataset

데이터셋은 data/ 디렉토리에 위치해야 합니다.

데이터 용량 및 라이선스 문제로 GitHub에는 업로드하지 않았습니다.

train.py 실행 전 데이터 경로를 확인해주세요.
