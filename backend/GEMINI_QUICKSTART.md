# ⚡ Quick Start: Gemini Integration

## 1️⃣ Get API Key (2 minutes)

1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

## 2️⃣ Add to `.env` (1 minute)

Open `backend\.env` and replace:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

With your actual key:
```env
GEMINI_API_KEY=AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4
```

Save the file!

## 3️⃣ Install Package (1 minute)

In PowerShell (with venv activated):
```powershell
pip install -r requirements.txt
```

## 4️⃣ Restart Server (30 seconds)

Stop the old server (Ctrl + C), then:
```powershell
python -m uvicorn main:app --reload
```

## 5️⃣ Test It (30 seconds)

Open browser and visit:
```
http://127.0.0.1:8000/test-ai
```

You should see Gemini's response!

---

## 📊 API Endpoints

```
✅ GET  http://127.0.0.1:8000/              → Server running
✅ GET  http://127.0.0.1:8000/health        → Health check
✅ GET  http://127.0.0.1:8000/test-ai       → Test Gemini
✅ POST http://127.0.0.1:8000/analyze?text=... → Analyze text
```

## 🗂️ Test in Swagger UI

Visit: `http://127.0.0.1:8000/docs`

Click on any endpoint → "Try it out" → "Execute"

---

## 🐛 Quick Troubleshooting

| Error | Fix |
|-------|-----|
| "GEMINI_API_KEY not found" | Check `.env` file is in backend folder |
| "ModuleNotFoundError: google" | Run `pip install -r requirements.txt` |
| "Invalid API Key" | Check API key is copied correctly in `.env` |
| "Port 8000 already in use" | Use `--port 8001` flag in start command |

---

See `GEMINI_SETUP_GUIDE.md` for full details!
