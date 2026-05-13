# 📖 Code Explanation: Gemini Integration

This guide explains every line of code in the Gemini integration.

---

## 📦 Understanding Imports

### In `ai.py`

```python
import os
```
**What it does:** Lets you read environment variables (like `GEMINI_API_KEY`)

**Example:**
```python
api_key = os.getenv("GEMINI_API_KEY")  # Read from .env
```

---

```python
from dotenv import load_dotenv
```
**What it does:** Loads variables from the `.env` file into your Python program

**Example:**
```python
load_dotenv()  # Read .env file
```

After this runs, you can access variables with `os.getenv()`

---

```python
import google.generativeai as genai
```
**What it does:** Imports Google's Gemini API library

**What `as genai` means:** Shorthand so you write `genai` instead of `google.generativeai`

**Example:**
```python
genai.configure(api_key=my_key)  # Instead of google.generativeai.configure()
```

---

### In `main.py`

```python
from fastapi import FastAPI, HTTPException
```
**What it does:** Import FastAPI tools
- `FastAPI` - Creates the web server
- `HTTPException` - Handles error responses

---

```python
from ai import get_ai_response, ask_ai
```
**What it does:** Import functions from your `ai.py` file

**This means:**
- You can use `get_ai_response()` in `main.py`
- You can use `ask_ai()` in `main.py`
- They're defined in `ai.py` but used in `main.py`

---

## 🔧 Understanding Configuration

### Loading Environment Variables

```python
# In ai.py
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```

**What happens:**
1. `load_dotenv()` reads the `.env` file
2. `os.getenv("GEMINI_API_KEY")` looks for `GEMINI_API_KEY` in `.env`
3. The value is stored in the `GEMINI_API_KEY` variable

**Example `.env` file:**
```env
GEMINI_API_KEY=AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4
```

**Then in Python:**
```python
GEMINI_API_KEY = "AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4"
```

---

### Checking If API Key Exists

```python
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables. "
        "Please add it to your .env file."
    )
```

**What it does:**
- Checks if `GEMINI_API_KEY` is empty
- If it is, shows an error message
- Prevents the program from running without an API key

**Why it's useful:**
- Catches configuration errors early
- Helps you debug quickly
- Better error message for beginners

---

### Configuring Gemini

```python
genai.configure(api_key=GEMINI_API_KEY)
```

**What it does:** Tells the Google library which account to use

**Analogy:** Like logging into a website - you need credentials

---

### Getting the Model

```python
model = genai.GenerativeModel("gemini-pro")
```

**What it does:** Selects which AI model to use

**Available models:**
- `"gemini-pro"` - Fast, general purpose (FREE) ← We use this
- `"gemini-pro-vision"` - For images
- `"gemini-1.5-pro"` - More powerful (may cost)

---

## 🤖 Understanding Functions

### The `ask_ai()` Function

```python
def ask_ai(prompt: str) -> str:
    """Send a prompt to Google Gemini and get a response"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = f"Error calling Gemini API: {str(e)}"
        print(error_msg)
        raise
```

**Breaking it down:**

```python
def ask_ai(prompt: str) -> str:
```
- `def` - Defines a function
- `ask_ai` - Function name
- `(prompt: str)` - Takes one argument: `prompt` (must be text)
- `-> str` - Returns text

---

```python
try:
    response = model.generate_content(prompt)
    return response.text
```
- `try:` - Try this code
- `model.generate_content(prompt)` - Send prompt to Gemini
- `response.text` - Get just the text part of the response
- `return` - Give the text back to whoever called this function

---

```python
except Exception as e:
    error_msg = f"Error calling Gemini API: {str(e)}"
    print(error_msg)
    raise
```
- `except Exception as e:` - If something goes wrong, catch the error
- `error_msg = ...` - Create an error message
- `print(error_msg)` - Show the error
- `raise` - Pass the error to the calling code

---

### The `get_ai_response()` Function

```python
def get_ai_response(text: str) -> str:
    """Process text and return AI analysis using Gemini"""
    prompt = f"Please analyze the following text and provide insights:\n\n{text}"
    return ask_ai(prompt)
```

**What it does:**
1. Takes some text as input
2. Creates a prompt for analyzing it
3. Calls `ask_ai()` with that prompt
4. Returns the response

**Example:**
```python
get_ai_response("Machine learning is...")
```

This creates the prompt:
```
Please analyze the following text and provide insights:

Machine learning is...
```

Then sends it to Gemini!

---

## 🌐 Understanding Endpoints

### The `/test-ai` Endpoint

```python
@app.get("/test-ai")
def test_ai():
    """Test endpoint to verify Gemini AI integration is working"""
    try:
        test_prompt = "What is the capital of France?"
        ai_response = ask_ai(test_prompt)
        return {
            "status": "success",
            "message": "Gemini AI is working correctly!",
            "prompt": test_prompt,
            "response": ai_response
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini API Error: {str(e)}"
        )
```

**What `@app.get("/test-ai")` means:**
- `@app` - Decorator (tells FastAPI about the route)
- `.get` - HTTP GET request (reading data, not sending)
- `"/test-ai"` - The endpoint path
- Visiting `http://localhost:8000/test-ai` calls this function

**What the function does:**
1. Creates a test prompt
2. Calls `ask_ai()` to get Gemini's response
3. Returns success with the response as JSON

**What the return looks like:**
```json
{
  "status": "success",
  "message": "Gemini AI is working correctly!",
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris, known as the City of Light..."
}
```

---

### Error Handling with HTTPException

```python
except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=f"Gemini API Error: {str(e)}"
    )
```

**What it does:**
- If something fails, return an HTTP error
- `status_code=500` - "Internal Server Error"
- `detail` - The error message to show

**What the browser sees:**
```json
{
  "detail": "Gemini API Error: Invalid API key provided."
}
```

---

### The `/analyze` Endpoint

```python
@app.post("/analyze")
def analyze(text: str):
    """Analyze text using Gemini AI"""
    try:
        result = get_ai_response(text)
        return {
            "status": "success",
            "input": text,
            "analysis": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis Error: {str(e)}"
        )
```

**Key differences from `/test-ai`:**
- Uses `@app.post` instead of `@app.get`
- Takes a parameter: `text: str`
- Calls `get_ai_response(text)` instead of `ask_ai()`

**Why `POST` instead of `GET`?**
- `GET` - For reading/retrieving data
- `POST` - For sending/processing data

**How to use it:**
```
GET http://127.0.0.1:8000/analyze?text=hello
```

**What it returns:**
```json
{
  "status": "success",
  "input": "hello",
  "analysis": "..."
}
```

---

## 🔐 Understanding API Keys & Security

### Why Store in `.env`?

**WRONG Way (INSECURE):**
```python
# ❌ DO NOT DO THIS
api_key = "AIzaSyDfv9ZgFr0FjpgKfEDXhX5xFVxXfvH_hX4"
genai.configure(api_key=api_key)
```

**Problems:**
- Key is visible in code
- Anyone can see it in GitHub
- Easy to accidentally share

---

**RIGHT Way (SECURE):**
```python
# ✅ DO THIS
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
```

**Benefits:**
- Key hidden in `.env` file
- `.env` is in `.gitignore` (not uploaded)
- Easy to change without touching code

---

### `.env` File Format

```env
# Comments start with #
KEY=value
API_KEY=AIzaSy...

# No spaces around =
❌ WRONG: KEY = value
✅ RIGHT: KEY=value

# Values with spaces need quotes
NAME="John Doe"
```

---

## 🎯 Data Flow Diagram

### When you visit `/test-ai`:

```
1. Browser
   ↓ GET request to /test-ai
2. FastAPI Server (main.py)
   ↓ Calls test_ai() function
3. Function creates prompt
   ↓ Calls ask_ai()
4. ask_ai() in ai.py
   ↓ Calls model.generate_content()
5. Gemini API (Google servers)
   ↓ Generates response
6. Response comes back
   ↓ ask_ai() returns text
7. test_ai() returns JSON
   ↓ Sent back to browser
8. Browser displays JSON
```

---

## 📋 Variable Types (Type Hints)

The code uses "type hints" to show what type variables should be:

```python
def ask_ai(prompt: str) -> str:
```

- `prompt: str` - `prompt` must be a string
- `-> str` - This function returns a string

**Other common types:**
```python
def function(name: str) -> str:              # Takes string, returns string
def function(age: int) -> int:               # Takes integer, returns integer
def function(items: list) -> dict:           # Takes list, returns dictionary
def function(data: dict) -> bool:            # Takes dict, returns boolean
```

**Why use type hints?**
- Makes code clearer
- Helps catch errors
- Works with autocomplete in VS Code

---

## 🧪 Testing the Code

### Test `ask_ai()` Directly

```python
# In a Python terminal
from ai import ask_ai

response = ask_ai("What is Python?")
print(response)
```

---

### Test `get_ai_response()` Directly

```python
from ai import get_ai_response

analysis = get_ai_response("Explain machine learning")
print(analysis)
```

---

## 🔄 Module Interaction

```
main.py
├── Imports: from ai import ask_ai, get_ai_response
├── Uses ask_ai() in /test-ai endpoint
└── Uses get_ai_response() in /analyze endpoint

ai.py
├── Imports: google.generativeai, os, dotenv
├── Loads: GEMINI_API_KEY from .env
├── Defines: ask_ai() function
└── Defines: get_ai_response() function
```

---

## ✨ Summary of Key Concepts

| Concept | Explanation |
|---------|-----------|
| Imports | Bring in code from libraries (`from X import Y`) |
| Functions | Reusable blocks of code (`def name():`) |
| Type Hints | Show what types variables should be (`param: str`) |
| API Keys | Secret credentials for external services |
| `.env` | File that stores secrets (not shared) |
| `load_dotenv()` | Loads `.env` variables into Python |
| `os.getenv()` | Reads environment variables |
| Decorators | `@app.get()` tells FastAPI how to route requests |
| Try/Except | Handle errors gracefully |
| JSON | Format for sending data between client and server |
| HTTP Methods | GET (read), POST (send), PUT (update), DELETE (remove) |

---

## 🎓 Learning Path

**Phase 1: Understand Concepts**
1. Read this file
2. Understand imports
3. Understand functions
4. Understand endpoints

**Phase 2: Run the Code**
1. Get API key
2. Add to `.env`
3. Start server
4. Test endpoints

**Phase 3: Modify the Code**
1. Change test prompt
2. Create new endpoint
3. Add custom logic
4. Build features

---

**Now you understand the entire Gemini integration!** 🚀

Next step: Run it yourself and test the endpoints!
