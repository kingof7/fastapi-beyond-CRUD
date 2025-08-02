@echo off
python3 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python -m pip install --upgrade pip
fastapi dev main.py