# 🧪 Testing Guide: FieldVision AI Backend with Gemini

This guide shows you how to test your Gemini AI integration with multiple tools.

---

## 🌐 Method 1: Browser (Easiest)

### Test `/test-ai` Endpoint

1. **Make sure server is running:**
   ```powershell
   python -m uvicorn main:app --reload
   ```

2. **Open browser and go to:**
   ```
   http://127.0.0.1:8000/test-ai
   ```

3. **You should see:**
   ```json
   {
     "status": "success",
     "message": "Gemini AI is working correctly!",
     "prompt": "What is the capital of France?",
     "response": "The capital of France is Paris..."
   }
   ```

### Test `/` Endpoint

```
http://127.0.0.1:8000/
```

Response:
```json
{"message": "FieldVision AI Backend Running"}
```

### Test `/health` Endpoint

```
http://127.0.0.1:8000/health
```

Response:
```json
{"status": "healthy", "service": "FieldVision AI Backend"}
```

### Test `/analyze` Endpoint

Try different prompts:

```
http://127.0.0.1:8000/analyze?text=What%20is%20machine%20learning
```

```
http://127.0.0.1:8000/analyze?text=Explain%20quantum%20computing
```

```
http://127.0.0.1:8000/analyze?text=Write%20a%20poem%20about%20AI
```

---

## 📚 Method 2: Swagger UI (Interactive)

### Best for Testing with GUI

1. **Start server:**
   ```powershell
   python -m uvicorn main:app --reload
   ```

2. **Open Swagger UI:**
   ```
   http://127.0.0.1:8000/docs
   ```

3. **You'll see all endpoints listed**

4. **To test `/test-ai`:**
   - Click on "GET /test-ai"
   - Click "Try it out"
   - Click "Execute"
   - See response below

5. **To test `/analyze`:**
   - Click on "POST /analyze"
   - Click "Try it out"
   - Enter text in "text" field
   - Click "Execute"
   - See response

### Swagger Features

- **Try it out:** Test endpoints interactly
- **Schema:** See response format
- **Code examples:** View request/response format

---

## 🖥️ Method 3: PowerShell Curl

### Simple GET Request

```powershell
curl http://127.0.0.1:8000/test-ai
```

### Get Formatted JSON

```powershell
curl http://127.0.0.1:8000/test-ai | ConvertFrom-Json | ConvertTo-Json
```

### Test `/analyze` (URL encoding)

```powershell
curl "http://127.0.0.1:8000/analyze?text=hello%20world"
```

### Full Example

```powershell
# Test if Gemini is working
$response = curl http://127.0.0.1:8000/test-ai
Write-Host $response
```

---

## 🔌 Method 4: Python Requests

Create a test file: `backend\test_api.py`

```python
import requests

# Test /test-ai endpoint
response = requests.get("http://127.0.0.1:8000/test-ai")
print("Status Code:", response.status_code)
print("Response:", response.json())

# Test /analyze endpoint
response = requests.post(
    "http://127.0.0.1:8000/analyze",
    params={"text": "What is machine learning?"}
)
print("Response:", response.json())
```

Run it:
```powershell
python test_api.py
```

---

## 🧪 Method 5: VS Code REST Client Extension

Create `test_api.http` file:

```http
### Test basic endpoint
GET http://127.0.0.1:8000/

### Test Gemini
GET http://127.0.0.1:8000/test-ai

### Test health
GET http://127.0.0.1:8000/health

### Test analyze
GET http://127.0.0.1:8000/analyze?text=hello%20world
```

Then click "Send Request" above each endpoint!

---

## 📋 Expected Responses

### ✅ Successful `/test-ai` Response

```json
{
  "status": "success",
  "message": "Gemini AI is working correctly!",
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris, known as the City of Light..."
}
```

### ✅ Successful `/analyze` Response

```json
{
  "status": "success",
  "input": "What is machine learning?",
  "analysis": "Machine learning is a subset of artificial intelligence (AI) that..."
}
```

### ❌ Error Response (Invalid API Key)

```json
{
  "detail": "Gemini API Error: Invalid API key provided."
}
```

### ❌ Error Response (Missing API Key)

```json
{
  "detail": "Gemini API Error: GEMINI_API_KEY not found in environment variables."
}
```

---

## 🧪 Test Cases

### Test 1: Server Running
```
GET http://127.0.0.1:8000/
Expected: {"message": "FieldVision AI Backend Running"}
```

### Test 2: Gemini AI Working
```
GET http://127.0.0.1:8000/test-ai
Expected: Successful response with AI answer
```

### Test 3: Text Analysis
```
GET http://127.0.0.1:8000/analyze?text=explain%20AI
Expected: Analysis of the text from Gemini
```

### Test 4: Different Models
Try different test prompts:
- "What is Python?"
- "Write a haiku about technology"
- "Explain blockchain in simple terms"
- "How does photosynthesis work?"

### Test 5: Error Handling
- Stop server and try to access endpoints
- Use invalid API key in `.env`
- Use port 8001 instead of 8000

---

## 📊 Performance Testing

### Response Time

```powershell
# Measure response time
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
curl http://127.0.0.1:8000/test-ai > $null
$stopwatch.Stop()
Write-Host "Response time: $($stopwatch.ElapsedMilliseconds)ms"
```

Typical response times:
- `/` → < 10ms
- `/health` → < 10ms
- `/test-ai` → 1-5 seconds (Gemini API call)
- `/analyze` → 1-5 seconds (Gemini API call)

### Load Testing

Install Apache Bench:
```powershell
# Windows: Download from Apache Bench website
# Or use Python's Apache Bench alternative
```

---

## 🔍 Debugging Tips

### View Server Logs

The terminal running your server shows:
```
INFO:     127.0.0.1:54321 - "GET /test-ai HTTP/1.1" 200 OK
```

This shows:
- IP address of request
- Endpoint called
- HTTP status (200 = OK, 500 = Error)

### Check Environment Variables

```powershell
# View all environment variables
Get-Item env:GEMINI_API_KEY

# Or in Python:
# import os
# print(os.getenv("GEMINI_API_KEY"))
```

### Test API Key Validity

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("test")
    print("API Key is valid!")
except Exception as e:
    print(f"Error: {e}")
```

---

## ✅ Testing Checklist

- [ ] Server starts without errors
- [ ] Can access `http://127.0.0.1:8000/`
- [ ] `/test-ai` returns Gemini response
- [ ] `/analyze` works with different text
- [ ] Error handling works (try invalid input)
- [ ] Response times are reasonable
- [ ] Can view docs at `/docs`
- [ ] API key is secure (in `.env` only)

---

## 🚀 Common Test Scenarios

### Test 1: New Setup
1. Install requirements: `pip install -r requirements.txt`
2. Add API key to `.env`
3. Start server
4. Visit `/test-ai`
5. Should work!

### Test 2: After Server Restart
```powershell
# Stop server (Ctrl + C)
# Start again
python -m uvicorn main:app --reload
```
Gemini should work again!

### Test 3: Different Prompts
```
/analyze?text=Explain%20recursion
/analyze?text=What%20is%20a%20REST%20API
/analyze?text=How%20does%20FastAPI%20work
```

All should return detailed responses!

---

## 📚 Resources

- **Swagger/OpenAPI Docs:** http://127.0.0.1:8000/docs
- **Swagger Alternative:** http://127.0.0.1:8000/redoc
- **Gemini API Docs:** https://ai.google.dev/
- **FastAPI Testing:** https://fastapi.tiangolo.com/tutorial/testing/

---

That's it! You now know multiple ways to test your FieldVision AI backend! 🎉
