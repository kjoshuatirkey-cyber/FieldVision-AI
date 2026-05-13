# 🔧 Cricket AI System - Code Breakdown for Beginners

This guide explains every piece of the cricket AI system.

---

## 📦 Understanding the Agent Architecture

### What is an Agent?

An **agent** is a Python program that:
1. Takes **input** (match data)
2. **Processes** it using Gemini AI
3. Returns **output** (analysis/prediction)

### Agent Structure

Each agent file has this pattern:

```python
# Step 1: Import Gemini AI function
from ai import ask_ai

# Step 2: Create analysis functions
def analyze_something(match_data):
    # Create a prompt
    prompt = "AI prompt here..."
    
    # Send to Gemini
    result = ask_ai(prompt)
    
    # Return result
    return result

# Step 3: Create main function
def get_agent_analysis(match_data):
    # Call multiple functions
    analysis1 = analyze_something(match_data)
    analysis2 = analyze_something_else(match_data)
    
    # Return dictionary with results
    return {
        "analysis1": analysis1,
        "analysis2": analysis2
    }
```

---

## 🎯 Bowling Agent Deep Dive

### File: `agents/bowling_agent.py`

```python
from ai import ask_ai
from typing import Dict, Any
```

**What this means:**
- Import Gemini AI function from `ai.py`
- Import type hints (Dict, Any) for better code clarity

---

### Function 1: `analyze_batsman_weakness()`

```python
def analyze_batsman_weakness(match_data: Dict[str, Any]) -> str:
    """Analyze current batsman's weakness using AI"""
    
    # Extract batsman info from match data
    batsman = match_data["current_batsman"]
    recent_balls = match_data["recent_balls"]
    
    # Create prompt for Gemini
    prompt = f"""
    Analyze the batting weakness of {batsman['name']} based on this data:
    
    Current Stats:
    - Runs: {batsman['runs']}
    - Balls Faced: {batsman['balls_faced']}
    - Strike Rate: {batsman['strike_rate']}%
    ...
    """
    
    # Send prompt to Gemini AI
    analysis = ask_ai(prompt)
    
    # Return the AI response
    return analysis
```

**What happens:**

```
Input: Match data
  ↓
Extract batsman info
  ↓
Create prompt: "Analyze batsman weakness..."
  ↓
Send to Gemini AI
  ↓
Gemini returns: "Batsman struggles against..."
  ↓
Output: AI response
```

---

### Function 2: `suggest_next_bowler()`

```python
def suggest_next_bowler(match_data: Dict[str, Any]) -> str:
    """Suggest the best bowler for the next over"""
    
    # Get current situation
    batsman = match_data["current_batsman"]
    current_bowler = match_data["current_bowler"]
    
    # Available bowlers to choose from
    available_bowlers = [
        {"name": "Jasprit Bumrah", "type": "fast", "economy": 6.5},
        {"name": "Yuzuki Chahal", "type": "spinner", "economy": 6.8},
        ...
    ]
    
    # Create prompt asking for recommendation
    prompt = f"""
    As a cricket analyst, suggest the best bowler...
    Current Bowler: {current_bowler['name']}
    Batsman: {batsman['name']} (SR: {batsman['strike_rate']}%)
    Available Bowlers: {available_bowlers}
    """
    
    # Get Gemini's recommendation
    suggestion = ask_ai(prompt)
    return suggestion
```

**What Gemini does:**
1. Reads the prompt
2. Analyzes current bowler's performance
3. Checks available bowlers
4. Matches bowler type to batsman weakness
5. Suggests best bowler with reasoning

---

### Function 3: `get_bowling_analysis()`

```python
def get_bowling_analysis(match_data: Dict[str, Any]) -> Dict[str, Any]:
    """Get complete bowling analysis using AI agents"""
    
    # Call multiple analysis functions
    return {
        "batsman_weakness": analyze_batsman_weakness(match_data),
        "next_bowler": suggest_next_bowler(match_data),
        "bowling_strategy": suggest_bowling_strategy(match_data),
        "current_bowler": match_data["current_bowler"]["name"],
        "current_batsman": match_data["current_batsman"]["name"]
    }
```

**This function:**
- Calls all analysis functions
- Combines results into one dictionary
- Returns complete analysis

---

## 💰 Understanding Dictionary Operations

**Cricket data is stored as Python dictionaries:**

```python
# Access single value
batsman = match_data["current_batsman"]
name = batsman["name"]  # "Rohit Sharma"
runs = batsman["runs"]  # 45

# Access nested values
overs = match_data["batting_team"]["overs_played"]

# Create new dictionary
analysis = {
    "player": "Rohit",
    "score": 45,
    "status": "in form"
}

# Get key from dictionary
my_dict = {"name": "Rohit", "runs": 45}
my_dict["name"]    # Returns "Rohit"
my_dict["runs"]    # Returns 45
```

---

## 🔤 Understanding f-strings (Formatted Strings)

f-strings embed variables in text:

```python
name = "Rohit"
runs = 45

# Without f-string
text = "Batsman " + name + " scored " + str(runs)

# With f-string (cleaner!)
text = f"Batsman {name} scored {runs}"

# f-strings in multi-line text
prompt = f"""
Analyze batsman:
- Name: {name}
- Runs: {runs}
- Status: In form
"""
```

---

## 🤖 How Gemini AI Works

```python
# Step 1: Create a detailed prompt
prompt = f"""
Analyze this batsman:
- Name: Rohit Sharma
- Runs: 45
- Strike Rate: 140%
- Fours: 4
- Sixes: 1

What are weaknesses?
"""

# Step 2: Send to Gemini
response = ask_ai(prompt)

# Step 3: Get response
# Response: "Rohit struggles against yorkers and slower balls..."
```

**What Gemini does:**
1. Reads the prompt
2. Uses AI to understand cricket concepts
3. Analyzes the data provided
4. Generates intelligent response
5. Returns the response to us

---

## 🏗️ Understanding Type Hints

Type hints show what type of data a function expects:

```python
# Without type hints (unclear)
def analyze(data):
    return result

# With type hints (clear!)
def analyze(data: Dict[str, Any]) -> str:
    return result

# Explanation:
# data: Dict[str, Any]
#   ↑      ↑
#   |      └─ Can be anything (Any)
#   └──────── Is a dictionary with string keys
#
# -> str
#   └─ Function returns a string
```

**Common type hints:**
```python
def func(name: str) -> str:              # String input, string output
def func(age: int) -> int:               # Integer input, integer output
def func(items: list) -> dict:           # List input, dict output
def func(data: Dict[str, Any]) -> str:   # Complex dictionary input
```

---

## 📊 Understanding Match Data Structure

```python
match_data = {
    # Match Info
    "match_id": "IPL2024_001",
    "match_name": "Mumbai vs RCB",
    
    # Batting Team (currently batting)
    "batting_team": {
        "team_name": "Mumbai Indians",
        "total_runs": 156,
        "total_wickets": 4,
        "overs_played": 18.3,
        "run_rate": 8.45
    },
    
    # Bowling Team (currently fielding)
    "bowling_team": {
        "team_name": "RCB"
    },
    
    # Current Batsman (at crease)
    "current_batsman": {
        "name": "Rohit Sharma",
        "runs": 45,
        "balls_faced": 32,
        "strike_rate": 140.6
    },
    
    # Current Bowler
    "current_bowler": {
        "name": "Mohammed Siraj",
        "economy": 8.4
    },
    
    # Match Status
    "required_run_rate": 12.5,
    "overs_left": 1.3,
    "match_status": "ongoing"
}
```

**How to access:**
```python
# Get team name
team = match_data["batting_team"]["team_name"]  # "Mumbai Indians"

# Get runs
runs = match_data["current_batsman"]["runs"]  # 45

# Get strike rate
sr = match_data["current_batsman"]["strike_rate"]  # 140.6
```

---

## 🚀 How Routes Work

### Route Definition

```python
@app.get("/bowling")
def get_bowling_recommendation(match_id: str = "IPL2024_001"):
    """Route docstring"""
    # Route logic
    return {"status": "success", "data": analysis}
```

**Breakdown:**
- `@app.get("/bowling")` - Define a GET route at `/bowling`
- `def get_bowling_recommendation()` - Function name (can be anything)
- `match_id: str = "IPL2024_001"` - Parameter with default value
- `return {...}` - Return data as JSON

### What Happens When User Visits

```
Browser: GET http://127.0.0.1:8000/bowling
  ↓
FastAPI sees @app.get("/bowling")
  ↓
Calls get_bowling_recommendation(match_id="IPL2024_001")
  ↓
Function runs:
  - Fetches match data
  - Validates it
  - Calls AI agent
  - Gets analysis
  ↓
Returns dictionary as JSON to browser
  ↓
Browser displays JSON
```

### Query Parameters

```python
# URL with parameters
http://127.0.0.1:8000/bowling?match_id=IPL2024_002

# In function
@app.get("/bowling")
def get_bowling_recommendation(match_id: str = "IPL2024_001"):
    # match_id = "IPL2024_002" (from URL)
    match_data = fetch_live_match_data(match_id)
```

---

## ⚠️ Error Handling

### Try-Except Block

```python
try:
    # Try to do something
    match_data = fetch_live_match_data(match_id)
    analysis = get_bowling_analysis(match_data)
    
except Exception as e:
    # If ANYTHING fails, catch the error
    raise HTTPException(
        status_code=500,  # Server error
        detail=f"Error: {str(e)}"
    )
```

**What happens:**
1. Try to run code
2. If error occurs, catch it
3. Create HTTPException with error message
4. Return error to client
5. Client sees error JSON response

### Common Errors

```python
# Error 1: Missing API key
ValueError("GEMINI_API_KEY not found")

# Error 2: Invalid match data
if not validate_match_data(match_data):
    raise ValueError("Invalid match data")

# Error 3: Gemini API error
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```

---

## 🔄 Data Flow Example

**User visits: `http://127.0.0.1:8000/bowling`**

```
┌─────────────────────────────────────────────┐
│ 1. Browser Request                          │
│    GET /bowling?match_id=IPL2024_001       │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 2. FastAPI Route (main.py)                  │
│    @app.get("/bowling")                     │
│    def get_bowling_recommendation()         │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 3. Fetch Match Data (utils.py)              │
│    fetch_live_match_data("IPL2024_001")    │
│    Returns: {match data dictionary}         │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 4. Validate Data (utils.py)                 │
│    validate_match_data(match_data)          │
│    Returns: True/False                      │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 5. AI Agent (bowling_agent.py)              │
│    get_bowling_analysis(match_data)         │
│    Calls:                                   │
│    - analyze_batsman_weakness()             │
│    - suggest_next_bowler()                  │
│    - suggest_bowling_strategy()             │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 6. Gemini AI (ai.py)                        │
│    ask_ai(prompt)                           │
│    Sends prompt to Google Gemini            │
│    Returns: "AI analysis here..."           │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 7. Build Response (main.py)                 │
│    {                                        │
│      "status": "success",                   │
│      "analysis": {                          │
│        "weakness": "...",                   │
│        "bowler": "...",                     │
│        "strategy": "..."                    │
│      }                                      │
│    }                                        │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│ 8. Return JSON to Browser                   │
│    Browser displays the JSON                │
└─────────────────────────────────────────────┘
```

---

## 🧪 Testing Code Locally

### Test Fetch Match Data

```python
# In Python terminal or script
from utils import fetch_live_match_data, validate_match_data

# Get match data
match_data = fetch_live_match_data("IPL2024_001")

# Validate it
is_valid = validate_match_data(match_data)
print(f"Valid: {is_valid}")

# Print team name
print(match_data["batting_team"]["team_name"])
```

### Test AI Agent

```python
from utils import fetch_live_match_data
from agents.bowling_agent import get_bowling_analysis

# Get match data
match_data = fetch_live_match_data("IPL2024_001")

# Get analysis
analysis = get_bowling_analysis(match_data)

# Print result
print(analysis["batsman_weakness"])
print(analysis["next_bowler"])
```

### Test Route (Using requests library)

```python
import requests

# Test /bowling endpoint
response = requests.get("http://127.0.0.1:8000/bowling")

# Print response
print(response.json())
```

---

## 📚 Common Patterns

### Pattern 1: Dictionary with Default Value

```python
# If key doesn't exist, use default
fours = batsman.get("fours", 0)  # 0 if "fours" not in batsman

# In f-string
prompt = f"Fours: {batsman.get('fours', 'N/A')}"
```

### Pattern 2: List Comprehension

```python
# Get recent ball types
recent_balls = match_data["recent_balls"]

# Convert to readable string
summary = ", ".join([f"Ball: {b['type']}" for b in recent_balls])
```

### Pattern 3: Conditional Logic

```python
# Check if under pressure
if required_rr > current_rr:
    pressure_level = "MEDIUM"
elif required_rr > (current_rr + 2):
    pressure_level = "HIGH"
else:
    pressure_level = "LOW"
```

---

## 💡 Pro Tips

1. **Use f-strings** for cleaner code:
   ```python
   # Good
   message = f"Score: {runs}/{wickets}"
   
   # Bad
   message = "Score: " + str(runs) + "/" + str(wickets)
   ```

2. **Use type hints** for clarity:
   ```python
   def analyze(data: Dict[str, Any]) -> str:
       # Clear what type of data is expected
   ```

3. **Use meaningful variable names**:
   ```python
   # Good
   batsman_strike_rate = 140.5
   
   # Bad
   bsr = 140.5
   ```

4. **Separate concerns** (one function, one job):
   ```python
   # Good - separate functions
   data = fetch_match_data()
   is_valid = validate_data(data)
   analysis = analyze_data(data)
   
   # Bad - one function doing everything
   def do_everything():
       # fetch, validate, analyze all mixed
   ```

---

## 🎓 Learning Path

**To master this code:**

1. **Understand Match Data Structure**
   - Read sample JSON
   - Learn how to access nested values

2. **Understand Agents**
   - Read one agent file completely
   - Understand how it creates prompts
   - Understand how it uses Gemini

3. **Understand Routes**
   - Read how routes connect to agents
   - Understand request/response flow

4. **Understand Error Handling**
   - See try-except blocks
   - Understand HTTPException

5. **Modify Code**
   - Change a prompt in an agent
   - Add a new analysis function
   - Create a new endpoint

---

That's the complete breakdown! You now understand every piece of the cricket AI system! 🏏🤖
