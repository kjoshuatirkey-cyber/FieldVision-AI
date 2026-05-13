# 🏏 Cricket AI Agents - Complete Setup Guide

This guide walks you through the Cricket Match Data System and AI Agents integration.

---

## 🎯 What You're Building

A **live cricket match analysis system** that uses AI agents to:
- 📊 Fetch live IPL/cricket match data
- 🤖 Use Gemini AI to analyze matches
- 🎙️ Generate exciting match commentary
- 🔮 Predict match outcomes
- 💡 Provide bowling & batting strategies

---

## 📋 Project Structure

```
backend/
├── agents/
│   ├── __init__.py                # Package initialization
│   ├── bowling_agent.py           # AI for bowling analysis
│   ├── batting_agent.py           # AI for batting analysis
│   ├── prediction_agent.py        # AI for match prediction
│   └── commentary_agent.py        # AI for commentary generation
├── main.py                        # Updated with cricket routes
├── utils.py                       # Cricket data fetching & utilities
├── ai.py                          # Existing Gemini integration
├── .env                           # API keys
├── requirements.txt               # Updated with requests library
└── [other existing files]
```

---

## 🚀 Quick Start (5 minutes)

### 1. Install New Package
```powershell
# Make sure venv is activated
.\venv\Scripts\Activate.ps1

# Install requests library (for API calls)
pip install requests
```

Or reinstall all:
```powershell
pip install -r requirements.txt
```

### 2. Start Your Server
```powershell
python -m uvicorn main:app --reload
```

### 3. Test Cricket Endpoints
Open your browser:

**View match data:**
```
http://127.0.0.1:8000/match
```

**Get bowling analysis:**
```
http://127.0.0.1:8000/bowling
```

**Get batting analysis:**
```
http://127.0.0.1:8000/batting
```

**Get match prediction:**
```
http://127.0.0.1:8000/prediction
```

**Get commentary:**
```
http://127.0.0.1:8000/commentary
```

---

## 📚 Understanding the Code

### 1. **utils.py** - Cricket Data & Utilities

This file handles fetching and providing cricket data.

**Key Functions:**

```python
# Get mock match data (for testing)
match_data = get_mock_match_data("IPL2024_001")

# In production: fetch from real cricket API
match_data = fetch_live_match_data(match_id)

# Validate match data is correct
is_valid = validate_match_data(match_data)

# Get text summary of match
summary = get_match_summary(match_data)
```

**Sample Match Data Structure:**

```json
{
  "match_id": "IPL2024_001",
  "match_name": "Mumbai Indians vs Royal Challengers Bangalore",
  "batting_team": {
    "team_name": "Mumbai Indians",
    "total_runs": 156,
    "total_wickets": 4,
    "overs_played": 18.3,
    "run_rate": 8.45
  },
  "bowling_team": {
    "team_name": "Royal Challengers Bangalore"
  },
  "current_batsman": {
    "name": "Rohit Sharma",
    "runs": 45,
    "balls_faced": 32,
    "strike_rate": 140.6
  },
  "current_bowler": {
    "name": "Mohammed Siraj",
    "overs_bowled": 3.3,
    "economy": 8.4
  },
  "required_run_rate": 12.5,
  "overs_left": 1.3,
  "match_status": "ongoing"
}
```

### 2. **agents/bowling_agent.py** - Bowling AI

Analyzes bowling strategies using Gemini AI.

**Functions:**

```python
# Analyze batsman's weaknesses
weakness = analyze_batsman_weakness(match_data)

# Suggest next bowler to use
suggestion = suggest_next_bowler(match_data)

# Get overall bowling strategy
strategy = suggest_bowling_strategy(match_data)

# Get complete analysis
analysis = get_bowling_analysis(match_data)
```

**What the AI Does:**
- Analyzes current batsman's strike rate, fours, sixes
- Identifies which deliveries the batsman struggles with
- Suggests which bowler should bowl next based on matchup
- Recommends overall team strategy

### 3. **agents/batting_agent.py** - Batting AI

Analyzes batting strategies and pressure.

**Functions:**

```python
# Analyze match pressure
pressure = analyze_batting_pressure(match_data)

# Suggest batting tactics
strategy = suggest_batting_strategy(match_data)

# Analyze run rate situation
rr_analysis = analyze_run_rate(match_data)

# Get complete analysis
analysis = get_batting_analysis(match_data)
```

**What the AI Does:**
- Assesses if the team is under pressure (comparing required RR to current RR)
- Suggests whether to be aggressive or cautious
- Advises who should take more risk
- Calculates if target is achievable

### 4. **agents/prediction_agent.py** - Prediction AI

Predicts match outcomes.

**Functions:**

```python
# Predict final score
score = predict_final_score(match_data)

# Predict winning probability
probability = predict_winning_probability(match_data)

# Predict key player performance
performance = predict_key_player_performance(match_data)

# Get complete predictions
predictions = get_match_prediction(match_data)
```

**What the AI Does:**
- Projects final score based on current run rate
- Predicts winning chance for bowling team
- Forecasts key player performances
- Identifies critical moments ahead

### 5. **agents/commentary_agent.py** - Commentary AI

Generates exciting IPL-style commentary.

**Functions:**

```python
# Generate live commentary
commentary = generate_live_commentary(match_data)

# Describe overall situation
situation = generate_situation_commentary(match_data)

# Describe current batsman
batsman_desc = generate_batsman_description(match_data)

# Analyze current bowler
bowler_desc = generate_bowler_analysis_commentary(match_data)

# Get complete commentary
full_commentary = get_match_commentary(match_data)
```

**What the AI Does:**
- Writes exciting "FOUR!", "SIX!" style commentary
- Describes current match drama
- Analyzes batsman's form and playing style
- Comments on bowler's performance

### 6. **main.py** - New Routes

Five new API endpoints:

```python
@app.get("/match")
# Get live match data

@app.get("/bowling")
# Get AI bowling analysis

@app.get("/batting")
# Get AI batting analysis

@app.get("/prediction")
# Get AI match predictions

@app.get("/commentary")
# Get AI commentary
```

---

## 🌐 API Endpoints Reference

### 1. GET `/match`
**Purpose:** Fetch live cricket match data

**URL:**
```
http://127.0.0.1:8000/match?match_id=IPL2024_001
```

**Response Example:**
```json
{
  "status": "success",
  "match_id": "IPL2024_001",
  "match_name": "Mumbai Indians vs RCB",
  "batting_team": {
    "team_name": "Mumbai Indians",
    "total_runs": 156,
    "total_wickets": 4,
    "overs_played": 18.3,
    "run_rate": 8.45
  },
  "bowling_team": {
    "team_name": "RCB"
  },
  "current_batsman": {
    "name": "Rohit Sharma",
    "runs": 45,
    "balls_faced": 32,
    "strike_rate": 140.6
  },
  "required_run_rate": 12.5,
  "overs_left": 1.3
}
```

### 2. GET `/bowling`
**Purpose:** Get AI bowling analysis and recommendations

**URL:**
```
http://127.0.0.1:8000/bowling?match_id=IPL2024_001
```

**Response Example:**
```json
{
  "status": "success",
  "bowling_team": "RCB",
  "current_batsman": "Rohit Sharma",
  "current_bowler": "Mohammed Siraj",
  "analysis": {
    "batsman_weakness": "Rohit Sharma has high SR against spinners but struggles against yorkers. Recent pattern shows...",
    "next_bowler_suggestion": "Best Choice: Jasprit Bumrah because his yorkers can trouble the aggressive batsman...",
    "bowling_strategy": "RCB should focus on tight line and length. Bowl yorkers at the death..."
  }
}
```

### 3. GET `/batting`
**Purpose:** Get AI batting strategy analysis

**URL:**
```
http://127.0.0.1:8000/batting?match_id=IPL2024_001
```

**Response Example:**
```json
{
  "status": "success",
  "batting_team": "Mumbai Indians",
  "current_score": "156/4",
  "analysis": {
    "pressure_analysis": "Mumbai is under MEDIUM pressure. Required RR is 12.5 vs current 8.45...",
    "batting_strategy": "Rohit should continue aggressive approach while Surya plays support role...",
    "run_rate_analysis": "Current RR is 8.45, need 12.5. Team needs to score 21 runs in 8 balls..."
  }
}
```

### 4. GET `/prediction`
**Purpose:** Get AI match predictions

**URL:**
```
http://127.0.0.1:8000/prediction?match_id=IPL2024_001
```

**Response Example:**
```json
{
  "status": "success",
  "teams": "Mumbai vs RCB",
  "overs_left": 1.3,
  "predictions": {
    "final_score": "Projected Score: 178-182 (80% confidence). Best case: 185+...",
    "winning_probability": "RCB has 35% chance of winning. Key factors: need 2 more wickets...",
    "key_player_performance": "Rohit likely to score 50+. Bumrah 85% chance of taking a wicket..."
  }
}
```

### 5. GET `/commentary`
**Purpose:** Get exciting IPL-style commentary

**URL:**
```
http://127.0.0.1:8000/commentary?match_id=IPL2024_001
```

**Response Example:**
```json
{
  "status": "success",
  "match_summary": "Mumbai vs RCB",
  "current_status": "156/4 (18.3 overs)",
  "commentary": {
    "live_commentary": "ROHIT ON FIRE! What a SCREAMER of a shot! The batsman is DOMINATING...",
    "situation_analysis": "This is DRAMA! Mumbai needs 21 in 8 balls. Can they pull off...",
    "batsman_description": "Rohit Sharma is IN FORM! Strike rate over 140, aggressive batting...",
    "bowler_analysis": "Mohammed Siraj struggling to contain the onslaught..."
  }
}
```

---

## 🧪 Testing Instructions

### Test Using Browser

**1. Test Match Data Endpoint:**
```
http://127.0.0.1:8000/match
```
You should see live match data in JSON format.

**2. Test Bowling Analysis:**
```
http://127.0.0.1:8000/bowling
```
You should see AI analysis of bowling strategy.

**3. Test Batting Analysis:**
```
http://127.0.0.1:8000/batting
```
You should see AI analysis of batting situation.

**4. Test Prediction:**
```
http://127.0.0.1:8000/prediction
```
You should see AI predictions for the match.

**5. Test Commentary:**
```
http://127.0.0.1:8000/commentary
```
You should see exciting IPL-style commentary!

### Test Using Swagger UI

Go to: `http://127.0.0.1:8000/docs`

1. Find each endpoint (match, bowling, batting, prediction, commentary)
2. Click "Try it out"
3. Click "Execute"
4. See the AI-powered response!

### Test Different Matches

Try both matches:
```
# Match 1
http://127.0.0.1:8000/match?match_id=IPL2024_001

# Match 2
http://127.0.0.1:8000/match?match_id=IPL2024_002
```

---

## 📊 Understanding JSON

**What is JSON?**

JSON = JavaScript Object Notation. It's a way to structure data.

**Example:**
```json
{
  "team_name": "Mumbai Indians",
  "runs": 156,
  "wickets": 4,
  "players": ["Rohit", "Surya"]
}
```

**Python Dictionary (same thing):**
```python
{
    "team_name": "Mumbai Indians",
    "runs": 156,
    "wickets": 4,
    "players": ["Rohit", "Surya"]
}
```

**Accessing values:**
```python
data = {
    "team_name": "Mumbai Indians",
    "runs": 156
}

print(data["team_name"])  # Output: Mumbai Indians
print(data["runs"])        # Output: 156
```

---

## 🔌 Understanding API Requests

**What is an API Request?**

An API request is asking another computer (server) for data.

**Example:**
```
Browser → Server: "Give me bowling analysis!"
Server → Browser: "Here's the AI bowling analysis!"
```

**In our code:**

```python
@app.get("/bowling")
def get_bowling_recommendation(match_id: str = "IPL2024_001"):
    # 1. Fetch match data
    match_data = fetch_live_match_data(match_id)
    
    # 2. Analyze with AI
    analysis = get_bowling_analysis(match_data)
    
    # 3. Return to client
    return {"status": "success", "analysis": analysis}
```

**When you visit:**
```
http://127.0.0.1:8000/bowling
```

**It does:**
1. Fetches match data
2. Sends it to Gemini AI
3. Gets AI response
4. Returns it as JSON to your browser

---

## ⚠️ Error Handling

All endpoints have error handling:

```python
try:
    # Try to get match data
    match_data = fetch_live_match_data(match_id)
    # Try to validate it
    if not validate_match_data(match_data):
        raise ValueError("Invalid data")
    # Try to analyze with AI
    analysis = get_bowling_analysis(match_data)
    
except Exception as e:
    # If anything fails, return error
    raise HTTPException(
        status_code=500,
        detail=f"Error: {str(e)}"
    )
```

**Common Errors & Solutions:**

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid match data" | Missing required fields | Check match data structure |
| "Gemini API Error" | API key invalid | Check .env file |
| "ModuleNotFoundError: requests" | requests library not installed | `pip install requests` |
| "Connection timeout" | Server not running | `python -m uvicorn main:app --reload` |

---

## 🏗️ Modular Code Structure

The code is organized for **easy maintenance and extension:**

```
agents/
├── bowling_agent.py    ← Bowling logic only
├── batting_agent.py    ← Batting logic only
├── prediction_agent.py ← Prediction logic only
└── commentary_agent.py ← Commentary logic only

main.py                 ← Routes that use agents

utils.py               ← Data fetching & utilities

ai.py                  ← Gemini integration
```

**Benefits:**
- ✅ Easy to find code (bowling logic in bowling_agent.py)
- ✅ Easy to test (each agent is separate)
- ✅ Easy to extend (add new agents easily)
- ✅ Clean and maintainable

**How to Add a New Agent:**

1. Create `new_agent.py` in `agents/` folder
2. Import Gemini function: `from ai import ask_ai`
3. Create AI functions
4. Export main function
5. Add route in `main.py`

---

## 🔄 Data Flow

Here's how data flows through the system:

```
1. Browser Request
   ↓
   GET /bowling

2. FastAPI Route (main.py)
   ↓
   fetch_live_match_data()

3. Utils (utils.py)
   ↓
   Returns mock/real cricket data

4. Agent (bowling_agent.py)
   ↓
   analyze_batsman_weakness()
   suggest_next_bowler()
   suggest_bowling_strategy()

5. Gemini AI (ai.py)
   ↓
   ask_ai() → Google's Gemini

6. Response
   ↓
   JSON back to browser
```

---

## 💻 Real-World Cricket APIs

**To use real live cricket data instead of mock data:**

### Option 1: Cricketdata.org API
```python
response = requests.get(
    "https://api.cricketdata.org/cricketdata/v1/match_info",
    params={
        "match_id": match_id,
        "offset": 0
    },
    headers={"Authorization": f"Bearer {CRICKET_API_KEY}"}
)
match_data = response.json()
```

### Option 2: RapidAPI (Cricket Live)
```python
response = requests.get(
    "https://cricketapi1.p.rapidapi.com/matches",
    headers={
        "X-RapidAPI-Key": YOUR_RAPIDAPI_KEY,
        "X-RapidAPI-Host": "cricketapi1.p.rapidapi.com"
    }
)
```

### Option 3: ESPNcricinfo (Web Scraping)
```python
# Scrape live data from ESPNcricinfo
soup = BeautifulSoup(requests.get("espncricinfo.com").content)
# Parse match data from HTML
```

**For now, we use mock data for testing and learning!**

---

## 🎓 Key Concepts

| Concept | Explanation |
|---------|-----------|
| **Agent** | AI program that analyzes specific cricket aspects |
| **Prompt** | Instructions sent to Gemini AI |
| **Mock Data** | Fake data for testing without real API |
| **Route** | URL endpoint that does something (`/bowling`) |
| **JSON** | Data format for storing and exchanging data |
| **Module** | Python file with related functions |
| **API** | Interface for getting data from another service |
| **Validation** | Checking data is correct before using it |

---

## 📝 File Summary

| File | Purpose |
|------|---------|
| **utils.py** | Fetches cricket data, contains mock data, validation |
| **agents/bowling_agent.py** | AI analysis for bowling strategies |
| **agents/batting_agent.py** | AI analysis for batting strategies |
| **agents/prediction_agent.py** | AI predictions for match outcomes |
| **agents/commentary_agent.py** | AI-generated exciting commentary |
| **main.py** | Routes that connect everything |
| **ai.py** | Gemini API integration (existing) |
| **requirements.txt** | Python packages needed |

---

## ✅ Checklist

- [ ] Installed requests package: `pip install -r requirements.txt`
- [ ] Created agents/ directory with 4 agent files
- [ ] Created utils.py with mock cricket data
- [ ] Updated main.py with 5 new routes
- [ ] Server starts without errors
- [ ] Can access `/match` endpoint
- [ ] Can access `/bowling` endpoint
- [ ] Can access `/batting` endpoint  
- [ ] Can access `/prediction` endpoint
- [ ] Can access `/commentary` endpoint
- [ ] All endpoints return JSON responses
- [ ] Gemini AI is responding correctly

---

## 🚀 Next Steps

### Immediate:
1. Test all endpoints in browser
2. Try different match IDs
3. Read the generated AI responses

### Short Term:
1. Create more mock matches
2. Add player injury data
3. Add weather data to analysis
4. Customize AI prompts

### Medium Term:
1. Integrate with real cricket API
2. Add database to store match history
3. Create frontend for displaying analysis
4. Add real-time WebSocket updates

### Long Term:
1. Build mobile app
2. Add betting odds analysis
3. Create player rating system
4. Publish as SaaS platform

---

## 📖 Resources

- **Cricketdata API:** https://cricketdata.org/
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Gemini API:** https://ai.google.dev/
- **Python Requests:** https://requests.readthedocs.io/
- **JSON Tutorial:** https://www.json.org/

---

That's it! You now have a complete cricket AI analysis system! 🏏🤖

Start testing with: `http://127.0.0.1:8000/docs`
