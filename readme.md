# Allergy Sticker Generator

This Python script reads a CSV file containing people's names and their allergies (which can be comma-delimited) and generates printable 4″ × 3″ name-tag stickers as PNG files at 300 DPI.

---

## Files in this Project

- **allergy.py**: The main script that reads the CSV and produces the stickers, including automatic font detection.
- **Option_1__Comma-Delimited_Allergies.csv**: A sample input file with headers:
  - `Name` (full name)
  - `Allergy` (either a single item, `None`/empty/`NaN` for no allergies, or a comma-separated list)
  You can replace this file with your own CSV, just remember to keep or update these column names.
- **stickers/**: This folder will be created to store the generated `sticker_<n>_<Name>.png` output files.

---

## Prerequisites

- Python 3.7+
- Pandas library
- Pillow library

---

## Getting Started

Follow these steps to get the sticker generator up and running:

### 1. Clone & Navigate

First, clone this repository or download the project files:

```bash
git clone <repo-URL>
cd allergy-sticker-generator
```

### 2. Create & Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

**Windows (PowerShell)**

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**Windows (CMD)**

```cmd
python -m venv env
env\Scripts\activate.bat
```

**macOS / Linux (bash/zsh)**

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

Once your virtual environment is active, install the required libraries:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```
pandas
pillow
```

### 4. Prepare Your CSV

The script uses `Option_1__Comma-Delimited_Allergies.csv` by default. Make sure your CSV file has two columns: `Name` and `Allergy`.

To use your own data, either replace `Option_1__Comma-Delimited_Allergies.csv` with your file or update the `INPUT_FILE` constant in `allergy.py` to point to your custom CSV path.

### 5. Automatic Font Detection

The script includes a `find_font()` helper that attempts to locate common system fonts like `arial.ttf` or `DejaVuSans.ttf`.

- If a font is found, it uses generous fixed sizes (**150 px** for names, **80 px** for allergy text).
- If no common system font is detected, it gracefully falls back to Pillow’s default font.

You can modify the font search list within `find_font()` or directly specify a font path in `allergy.py`, for example:

```python
font = ImageFont.truetype('path/to/your/font.ttf', size)
```

### 6. Run the Script

Execute the script from your terminal:

```bash
python allergy.py
```

The script will:

- Read your CSV and automatically fill any missing allergy entries with "No allergy."
- Generate one PNG image for each person, sized at **1200×900 px** (4″×3″ at 300 DPI).
- Save these files in the `stickers/` directory, named sequentially (e.g., `sticker_1_AliceSmith.png`).

---

## Customization

You can easily adjust several parameters in `allergy.py` to suit your needs:

- **Canvas size**: Modify `IMG_WIDTH` and `IMG_HEIGHT`.
- **Font sizes**: Change `NAME_FONT_SZ` for names and `ALLERGY_FONT_SZ` for allergy text.
- **Column headers**: Update `NAME_COL` and `ALLERGY_COL` if your CSV uses different column names.

---

# 알레르기 스티커 생성기

이 Python 스크립트는 사람들의 이름과 (쉼표로 구분될 수 있는) 알레르기 정보가 포함된 CSV 파일을 읽어 300 DPI의 인쇄 가능한 4″ × 3″ 명찰 스티커(PNG 파일)를 생성합니다.

---

## 프로젝트 파일

- **allergy.py**: CSV를 읽고 스티커를 생성하는 메인 스크립트이며, 자동 폰트 감지 기능이 포함되어 있습니다.
- **Option_1__Comma-Delimited_Allergies.csv**: 샘플 입력 파일로, 다음과 같은 헤더를 가집니다:
  - `Name` (전체 이름)
  - `Allergy` (단일 항목, 알레르기가 없는 경우 `None`/빈 값/`NaN`, 또는 쉼표로 구분된 목록)
  이 파일을 원하는 CSV로 교체할 수 있지만, 이 열 이름을 유지하거나 업데이트해야 합니다.
- **stickers/**: 생성된 `sticker_<n>_<Name>.png` 출력 파일이 저장될 폴더입니다.

---

## 필수 요건

- Python 3.7 이상
- Pandas 라이브러리
- Pillow 라이브러리

---

## 시작하기

스티커 생성기를 실행하려면 다음 단계를 따르세요:

### 1. 저장소 복제 및 이동

먼저, 이 저장소를 복제하거나 프로젝트 파일을 다운로드하세요:

```bash
git clone <repo-URL>
cd allergy-sticker-generator
```

### 2. 가상 환경 생성 및 활성화

종속성 관리를 위해 가상 환경을 사용하는 것을 권장합니다.

**Windows (PowerShell)**

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**Windows (CMD)**

```cmd
python -m venv env
env\Scripts\activate.bat
```

**macOS / Linux (bash/zsh)**

```bash
python3 -m venv env
source env/bin/activate
```

### 3. 종속성 설치

가상 환경이 활성화되면, 필요한 라이브러리를 설치하세요:

```bash
pip install -r requirements.txt
```

`requirements.txt` 파일에는 다음 내용이 포함되어 있습니다:

```
pandas
pillow
```

### 4. CSV 준비

스크립트는 기본적으로 `Option_1__Comma-Delimited_Allergies.csv`를 사용합니다. CSV 파일에 `Name`과 `Allergy` 두 열이 있는지 확인하세요.

자신의 데이터를 사용하려면, `Option_1__Comma-Delimited_Allergies.csv` 파일을 교체하거나 `allergy.py` 파일의 `INPUT_FILE` 상수를 자신의 CSV 경로로 업데이트하세요.

### 5. 자동 폰트 감지

스크립트에는 `find_font()` 도우미가 포함되어 있습니다. 이 도우미는 `arial.ttf` 또는 `DejaVuSans.ttf`와 같은 일반적인 시스템 폰트를 찾습니다.

- 폰트를 찾으면, 이름에는 **150px**, 알레르기 텍스트에는 **80px**의 고정 크기를 사용합니다.
- 일반적인 시스템 폰트를 찾지 못하면, Pillow의 기본 폰트로 대체됩니다.

`find_font()` 내의 폰트 검색 목록을 수정하거나, `allergy.py`에서 직접 폰트 경로를 지정할 수 있습니다. 예:

```python
font = ImageFont.truetype('path/to/your/font.ttf', size)
```

### 6. 스크립트 실행

터미널에서 스크립트를 실행합니다:

```bash
python allergy.py
```

스크립트는 다음을 수행합니다:

- CSV를 읽고 누락된 알레르기 항목을 자동으로 "No allergy."로 채웁니다.
- 각 사람마다 **1200×900 px** (300 DPI에서 4″×3″에 해당) 크기의 PNG 이미지를 생성합니다.
- stickers/ 디렉토리에 순서대로 저장합니다 (예: `sticker_1_AliceSmith.png`).

---

## 사용자 정의

`allergy.py`의 매개변수를 수정하여 필요에 맞게 조정할 수 있습니다:

- **캔버스 크기**: `IMG_WIDTH`와 `IMG_HEIGHT` 수정
- **폰트 크기**: `NAME_FONT_SZ`와 `ALLERGY_FONT_SZ` 변경
- **열 헤더**: CSV 열 이름이 다른 경우 `NAME_COL`과 `ALLERGY_COL` 업데이트
