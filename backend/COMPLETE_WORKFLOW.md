# 🎯 Complete Workflow: FastAPI + Gemini AI Setup

This guide walks you through the ENTIRE process from start to finish.

---

## 🚀 COMPLETE SETUP WORKFLOW (15-20 minutes)

### Phase 1: Get Gemini API Key (2 minutes)

**Step 1.1: Open Google AI Studio**
- Visit: https://aistudio.google.com/app/apikey
- Sign in with your Google account
- Click "Create API Key"
- Copy the key to clipboard

**Step 1.2: Keep It Safe**
- Don't share this key
- Don't put it in code
- Only put it in `.env` file

---

### Phase 2: Configure Your Backend (3 minutes)

**Step 2.1: Open PowerShell**
- Press `Windows Key + X`
- Click "Windows PowerShell"

**Step 2.2: Navigate to Backend**
```powershell
cd "C:\Users\kjosh\OneDrive\Desktop\FieldVision AI\backend"
```

**Step 2.3: Check Virtual Environment**
```powershell
.\venv\Scripts\Activate.ps1
```
(You should see `(venv)` in your prompt)

**Step 2.4: Add API Key to `.env`**
- Open `backend\.env` in VS Code
- Find: `GEMINI_API_KEY=your_gemini_api_key_here`
- Replace with your actual key:
  ```env
  GEMINI_API_KEY=AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4
  ```
- Save (Ctrl + S)

---

### Phase 3: Install Packages (2 minutes)

**Step 3.1: Install Gemini Package**
```powershell
# Make sure (venv) is active
pip install -r requirements.txt
```

This installs:
- FastAPI
- Uvicorn
- python-dotenv
- **google-generativeai** (NEW!)

**Step 3.2: Verify Installation**
```powershell
pip list
```
Look for `google-generativeai` in the output.

---

### Phase 4: Start Your Server (30 seconds)

**Step 4.1: Run Server**
```powershell
python -m uvicorn main:app --reload
```

**Step 4.2: Verify It Started**
Look for:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

---

### Phase 5: Test Your Integration (2 minutes)

**Step 5.1: Test Basic Server**
- Open browser: `http://127.0.0.1:8000/`
- Should see: `{"message": "FieldVision AI Backend Running"}`

**Step 5.2: Test Gemini Integration**
- Open browser: `http://127.0.0.1:8000/test-ai`
- Wait a moment (Gemini API call takes 1-3 seconds)
- Should see response from Gemini!

**Step 5.3: View API Documentation**
- Open: `http://127.0.0.1:8000/docs`
- Click on `/test-ai`
- Click "Try it out"
- Click "Execute"
- See Gemini's response!

---

## ✅ Verification Checklist

Use this to confirm everything is working:

- [ ] API key obtained from https://aistudio.google.com/app/apikey
- [ ] API key added to `backend\.env`
- [ ] Virtual environment activated (`(venv)` visible in prompt)
- [ ] Packages installed (`pip install -r requirements.txt` completed)
- [ ] Server running (`python -m uvicorn main:app --reload` started)
- [ ] Server responds to `http://127.0.0.1:8000/`
- [ ] `/test-ai` returns a response from Gemini
- [ ] No errors in PowerShell terminal
- [ ] Can see docs at `http://127.0.0.1:8000/docs`

---

## 📊 File Overview

### main.py (Updated)
```python
from fastapi import FastAPI
from ai import ask_ai

app = FastAPI()

@app.get("/test-ai")
def test_ai():
    """Test Gemini integration"""
    ai_response = ask_ai("What is the capital of France?")
    return {
        "status": "success",
        "response": ai_response
    }
```

### ai.py (Updated)
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

def ask_ai(prompt: str) -> str:
    """Send prompt to Gemini and get response"""
    response = model.generate_content(prompt)
    return response.text
```

### .env (Updated)
```env
GEMINI_API_KEY=your_actual_api_key_here
ENVIRONMENT=development
DEBUG=True
```

### requirements.txt (Updated)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
google-generativeai==0.3.0
```

---

## 🧪 Test All Endpoints

### Test 1: Basic Server Health
```
GET http://127.0.0.1:8000/
```
**Expected:** `{"message": "FieldVision AI Backend Running"}`

### Test 2: Gemini Integration
```
GET http://127.0.0.1:8000/test-ai
```
**Expected:** Response from Gemini about "the capital of France"

### Test 3: Analyze Text
```
GET http://127.0.0.1:8000/analyze?text=Explain%20machine%20learning
```
**Expected:** Analysis of the text

### Test 4: Health Check
```
GET http://127.0.0.1:8000/health
```
**Expected:** `{"status": "healthy", "service": "FieldVision AI Backend"}`

---

## 🔄 Daily Workflow

### Each Time You Start Working:

**1. Open PowerShell**
```powershell
cd "C:\Users\kjosh\OneDrive\Desktop\FieldVision AI\backend"
```

**2. Activate Virtual Environment**
```powershell
.\venv\Scripts\Activate.ps1
```

**3. Start Server**
```powershell
python -m uvicorn main:app --reload
```

**4. Work on Code**
- Edit `main.py` or `ai.py`
- Server automatically reloads with `--reload` flag

**5. Stop Server** (when done)
```powershell
Ctrl + C
```

---

## 🐛 If Something Goes Wrong

### Server Won't Start
```powershell
# Make sure venv is activated
# Check if port 8000 is free
# Try different port:
python -m uvicorn main:app --reload --port 8001
```

### "GEMINI_API_KEY not found"
- Check `.env` file exists in `backend` folder
- Verify API key is set correctly
- Make sure no typos in `.env`
- Restart server

### "ModuleNotFoundError: google"
```powershell
pip install google-generativeai
```

### "401 Unauthorized"
- Check API key is correct in `.env`
- Visit Google AI Studio: https://aistudio.google.com/app/apikey
- Generate new key if needed

### Port Already in Use
```powershell
python -m uvicorn main:app --reload --port 8001
# Then visit: http://127.0.0.1:8001/test-ai
```

---

## 📚 Available Guides

1. **GEMINI_QUICKSTART.md** - 2-minute overview
2. **GEMINI_SETUP_GUIDE.md** - Detailed explanations
3. **TESTING_GUIDE.md** - Multiple testing methods
4. **SETUP_GUIDE.md** - Initial FastAPI setup
5. **QUICKSTART.md** - General quick reference

---

## 🚀 Next Steps After This Works

1. **Test Different Prompts**
   - Try: `/analyze?text=what%20is%20AI`
   - Try: `/analyze?text=explain%20quantum%20computing`

2. **Explore Gemini Models**
   - Change `"gemini-pro"` to other models in `ai.py`

3. **Build More Endpoints**
   - Image analysis
   - Chat history
   - Custom prompts

4. **Connect Frontend**
   - Your React app can call these endpoints
   - Display AI responses in the UI

5. **Add Error Handling**
   - Better error messages
   - Logging
   - Rate limiting

---

## ✨ Tips for Success

### ✅ DO:
- Use `.env` for sensitive data
- Check that venv is activated (look for `(venv)` in prompt)
- Save files before restarting server
- Test endpoints regularly
- Read error messages carefully

### ❌ DON'T:
- Hardcode API keys in Python files
- Share your API key
- Put `.env` in Git
- Try to manually edit `.venv` folder
- Use the same API key for multiple projects

---

## 🎓 What You're Learning

**Concepts covered:**
- REST APIs with FastAPI
- Environment variables and `.env` files
- API integration (Google Gemini)
- Virtual environments
- Server management
- Testing endpoints
- Error handling

**Skills developed:**
- Backend development
- API design
- Configuration management
- Debugging
- Testing

---

## 📞 Quick Command Reference

| Need | Command |
|------|---------|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Deactivate venv | `deactivate` |
| Install packages | `pip install -r requirements.txt` |
| Start server | `python -m uvicorn main:app --reload` |
| Start on port 8001 | `python -m uvicorn main:app --reload --port 8001` |
| Stop server | `Ctrl + C` |
| List packages | `pip list` |
| Test Gemini | Open: `http://127.0.0.1:8000/test-ai` |
| View docs | Open: `http://127.0.0.1:8000/docs` |

---

## 🎉 Success!

You now have:
- ✅ FastAPI backend server
- ✅ Google Gemini AI integration
- ✅ Working endpoints
- ✅ API documentation
- ✅ Multiple testing methods

**Ready to build amazing things with AI!** 🚀

---

**Questions?** Check the detailed guides:
- **GEMINI_SETUP_GUIDE.md** - Most common questions
- **TESTING_GUIDE.md** - How to test everything
- **TROUBLESHOOTING** section above
