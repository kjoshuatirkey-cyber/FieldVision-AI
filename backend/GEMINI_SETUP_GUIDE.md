# 🚀 Gemini AI Integration Guide - FieldVision AI Backend

## 📋 What You're Building

You're adding **Google Gemini AI** to your FastAPI backend. This allows your application to:
- Generate intelligent responses
- Analyze text using AI
- Process natural language
- Build AI-powered features

---

## 🔑 STEP 1: Get Your Gemini API Key

### What is an API Key?
An **API key** is like a password that lets your application talk to Google's Gemini AI. It's secret and should never be shared!

### Getting Your Free API Key

1. **Open this link in your browser:**
   ```
   https://aistudio.google.com/app/apikey
   ```
   (Or search "Google AI Studio" in Google)

2. **Sign in with your Google account**
   - If you don't have a Google account, create one (free!)

3. **Click "Create API Key"**
   - Select "Create API key in new project"
   
4. **Copy the API Key**
   - You'll see a long string of characters
   - Click "Copy" button
   - Keep this secret!

### Example API Key (DO NOT USE - THIS IS FAKE):
```
AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4
```
Your real key will look similar but be different.

---

## 💾 STEP 2: Add API Key to `.env` File

### 🔒 What is `.env`?
The `.env` file stores **secret information** like API keys. It's NOT shared with GitHub.

### How to Add Your Key

1. **Open the `.env` file** in VS Code
   - File path: `backend\.env`

2. **Find this line:**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Replace** `your_gemini_api_key_here` with your actual API key
   
4. **Example (with fake key):**
   ```
   GEMINI_API_KEY=AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4
   ```

5. **Save the file** (Ctrl + S)

### ⚠️ IMPORTANT: Keep `.env` Secret!
- The `.env` file is in your `.gitignore` (won't be uploaded to GitHub)
- Never share your API key with anyone
- Never commit `.env` to Git

---

## 📦 STEP 3: Install Google Generative AI Package

Your server needs the `google-generativeai` package to talk to Gemini.

### Commands in PowerShell

1. **Navigate to backend folder** (if not already there):
   ```powershell
   cd "C:\Users\kjosh\OneDrive\Desktop\FieldVision AI\backend"
   ```

2. **Activate virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   (You should see `(venv)` in your prompt)

3. **Install the new packages**:
   ```powershell
   pip install -r requirements.txt
   ```
   This installs:
   - ✅ fastapi
   - ✅ uvicorn
   - ✅ python-dotenv
   - ✅ **google-generativeai** (NEW!)

### Verify Installation
```powershell
pip list
```
Look for `google-generativeai` in the list.

---

## 🔄 STEP 4: Update Your Server

### Changes Made to Your Files

**New in `ai.py`:**
```python
import google.generativeai as genai

def ask_ai(prompt: str) -> str:
    """Send a prompt to Gemini and get response"""
    response = model.generate_content(prompt)
    return response.text
```

**New in `main.py`:**
```python
@app.get("/test-ai")
def test_ai():
    """Test endpoint for Gemini integration"""
    ai_response = ask_ai("What is the capital of France?")
    return {"status": "success", "response": ai_response}
```

---

## ✅ STEP 5: Restart Your Server

### Stop Current Server (if running)
Press `Ctrl + C` in PowerShell

### Start Fresh Server
```powershell
python -m uvicorn main:app --reload
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

If you see errors, check the **Troubleshooting** section below.

---

## 🧪 STEP 6: Test Gemini Integration

### Test Using Browser

1. **Open this URL:**
   ```
   http://127.0.0.1:8000/test-ai
   ```

2. **You should see a response like:**
   ```json
   {
     "status": "success",
     "message": "Gemini AI is working correctly!",
     "prompt": "What is the capital of France?",
     "response": "The capital of France is Paris, known as the City of Light..."
   }
   ```

### Test Using Swagger UI (Interactive Docs)

1. **Open:**
   ```
   http://127.0.0.1:8000/docs
   ```

2. **Find `GET /test-ai`**

3. **Click "Try it out"**

4. **Click "Execute"**

5. **See the response below**

### Test with Curl Command (PowerShell)

```powershell
curl http://127.0.0.1:8000/test-ai
```

---

## 📊 Your API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Check server is running |
| `/health` | GET | Health check |
| `/test-ai` | GET | Test Gemini integration |
| `/analyze?text=...` | POST | Analyze text with Gemini |

### Examples

**Test AI:**
```
http://127.0.0.1:8000/test-ai
```

**Analyze Text:**
```
http://127.0.0.1:8000/analyze?text=Explain%20machine%20learning
```

(The `%20` represents a space in URLs)

---

## 🔍 Understanding the Code

### How `ai.py` Works

```python
# 1. Import Gemini library
import google.generativeai as genai

# 2. Load API key from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 3. Set up Gemini with your API key
genai.configure(api_key=GEMINI_API_KEY)

# 4. Get the model
model = genai.GenerativeModel("gemini-pro")

# 5. Create a function to ask questions
def ask_ai(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
```

### How `main.py` Uses It

```python
from ai import ask_ai  # Import the function

@app.get("/test-ai")
def test_ai():
    # Call the AI function
    ai_response = ask_ai("What is the capital of France?")
    
    # Return the response as JSON
    return {"response": ai_response}
```

### How Environment Variables Work

```python
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")
```

When Python runs, it reads `.env` and makes all variables available.

---

## ⚠️ Troubleshooting

### ❌ Error: "GEMINI_API_KEY not found in environment variables"

**What it means:** Your `.env` file isn't set up correctly.

**Solutions:**

1. **Check if `.env` exists:**
   - Look in: `backend\.env`
   - File should be in the backend folder (not inside venv)

2. **Check the content:**
   - Open `.env` in VS Code
   - Should have: `GEMINI_API_KEY=your_actual_api_key`

3. **No spaces around `=`:**
   ```
   ❌ WRONG: GEMINI_API_KEY = AIzaSy...
   ✅ RIGHT: GEMINI_API_KEY=AIzaSy...
   ```

4. **Restart the server:**
   ```powershell
   # Stop server: Ctrl + C
   # Start again:
   python -m uvicorn main:app --reload
   ```

### ❌ Error: "ModuleNotFoundError: No module named 'google.generativeai'"

**What it means:** The package isn't installed.

**Solution:**
```powershell
# Make sure (venv) is in your prompt
pip install google-generativeai

# Or reinstall everything:
pip install -r requirements.txt
```

### ❌ Error: "401 Unauthorized" or "Invalid API Key"

**What it means:** Your API key is wrong.

**Solutions:**

1. **Check your API key:**
   - Open `.env`
   - Is it the exact key from Google AI Studio?
   - No extra spaces? No typos?

2. **Get a new API key:**
   - Go to https://aistudio.google.com/app/apikey
   - Generate a new key
   - Copy and paste (don't type)

3. **Make sure you have free quota:**
   - Gemini API is free to use with limits
   - Check Google's website if you hit rate limits

### ❌ Error: "Failed to generate content"

**What it means:** Gemini rejected the request.

**Solutions:**

1. **Wait a moment** - Maybe rate limited, try again
2. **Check your internet connection**
3. **Try a different prompt** - Some words might be blocked
4. **Restart the server**

### ❌ Error: "dotenv not installed"

**Solution:**
```powershell
pip install python-dotenv
```

### ❌ Server won't start - "Address already in use"

**What it means:** Something is using port 8000.

**Solution - Use a different port:**
```powershell
python -m uvicorn main:app --reload --port 8001
```

Then visit: `http://127.0.0.1:8001/test-ai`

---

## 🔐 Security Best Practices

### ✅ DO:
- Store API keys in `.env` file
- Add `.env` to `.gitignore` (already done!)
- Use environment variables for secrets
- Rotate keys if compromised
- Keep keys private

### ❌ DON'T:
- Hardcode API keys in Python files
- Share your API key with anyone
- Commit `.env` to GitHub
- Post your key in forums/chat
- Use the same key for multiple projects

### Example of WRONG Way:
```python
# ❌ NEVER DO THIS!
api_key = "AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4"
genai.configure(api_key=api_key)
```

### Example of RIGHT Way:
```python
# ✅ DO THIS!
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
```

---

## 📚 Understanding Gemini Models

### Available Models

```python
# Fast, general purpose (FREE)
genai.GenerativeModel("gemini-pro")

# For images
genai.GenerativeModel("gemini-pro-vision")

# More powerful (may require payment)
genai.GenerativeModel("gemini-1.5-pro")
```

### Changing the Model

To use a different model, edit `ai.py`:

```python
# Change this line:
model = genai.GenerativeModel("gemini-pro")

# To this:
model = genai.GenerativeModel("gemini-1.5-pro")
```

---

## 📖 Useful Resources

- **Google AI Studio:** https://aistudio.google.com/
- **Gemini API Docs:** https://ai.google.dev/
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Python Environment Variables:** https://docs.python.org/3/library/os.html
- **REST API Basics:** https://restfulapi.net/

---

## ✅ Checklist

- [ ] Got Gemini API key from https://aistudio.google.com/app/apikey
- [ ] Added API key to `.env` file
- [ ] Installed `google-generativeai` (`pip install -r requirements.txt`)
- [ ] Updated `ai.py` with Gemini code
- [ ] Updated `main.py` with `/test-ai` endpoint
- [ ] Started server (`python -m uvicorn main:app --reload`)
- [ ] Tested `/test-ai` endpoint in browser
- [ ] Got successful response from Gemini
- [ ] Understanding all the code explanations

---

## 🎉 What's Next?

1. **Test different prompts:**
   - Try `/analyze?text=explain%20quantum%20computing`

2. **Create more endpoints:**
   - Image analysis with `gemini-pro-vision`
   - Chat history feature
   - Different AI models

3. **Connect to frontend:**
   - Your React app can call `/test-ai` endpoint
   - Display AI responses in the UI

4. **Add error handling:**
   - Better error messages
   - Logging for debugging
   - Rate limiting

---

**Congratulations! Your FieldVision AI backend now has Gemini AI integration!** 🚀
