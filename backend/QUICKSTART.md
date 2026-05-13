# Quick Start (TL;DR)

## 1. Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
You should see `(venv)` in your prompt.

## 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

## 3. Run Server
```powershell
python -m uvicorn main:app --reload
```

## 4. Test
Open browser: `http://127.0.0.1:8000`

Expected response:
```json
{"message": "FieldVision AI Backend Running"}
```

## 5. View API Documentation
Open browser: `http://127.0.0.1:8000/docs`

## Stop Server
Press `CTRL + C` in PowerShell

---

**Full setup guide:** See `SETUP_GUIDE.md`
