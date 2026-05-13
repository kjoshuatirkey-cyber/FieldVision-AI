# 🏏 Cricket AI Testing Guide

Complete testing instructions for the cricket match data system.

---

## 🚀 Pre-Testing Checklist

- [ ] Server is running: `python -m uvicorn main:app --reload`
- [ ] All new packages installed: `pip install -r requirements.txt`
- [ ] API key in `.env` file
- [ ] agents/ folder exists with 4 agent files
- [ ] utils.py has mock cricket data

---

## 🌐 Browser Testing

### Test 1: Match Data Endpoint

**URL:**
```
http://127.0.0.1:8000/match
```

**Expected Response:**
```json
{
  "status": "success",
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

**What to look for:**
- ✅ Status is "success"
- ✅ Contains batting team info
- ✅ Contains bowling team info
- ✅ Contains batsman and bowler data
- ✅ No errors in response

---

### Test 2: Bowling Analysis Endpoint

**URL:**
```
http://127.0.0.1:8000/bowling
```

**Expected Response (with AI Analysis):**
```json
{
  "status": "success",
  "match_id": "IPL2024_001",
  "bowling_team": "Royal Challengers Bangalore",
  "current_batsman": "Rohit Sharma",
  "current_bowler": "Mohammed Siraj",
  "analysis": {
    "batsman_weakness": "Rohit Sharma has shown a high strike rate against spinners but appears vulnerable to yorkers and slower deliveries. The batsman's aggressive approach...",
    "next_bowler_suggestion": "Best Choice: Jasprit Bumrah because his yorkers and death bowling skills can effectively restrict the aggressive batsman...",
    "bowling_strategy": "RCB should focus on bowl tight lines and lengths. Consider bowling yorkers at the death..."
  }
}
```

**What to look for:**
- ✅ Status is "success"
- ✅ Contains AI-generated weakness analysis
- ✅ Contains next bowler suggestion
- ✅ Contains bowling strategy
- ✅ Analysis is cricket-specific

---

### Test 3: Batting Analysis Endpoint

**URL:**
```
http://127.0.0.1:8000/batting
```

**Expected Response (with AI Analysis):**
```json
{
  "status": "success",
  "match_id": "IPL2024_001",
  "batting_team": "Mumbai Indians",
  "current_score": "156/4",
  "analysis": {
    "pressure_analysis": "Mumbai is under MEDIUM-HIGH pressure. The required run rate of 12.5 is significantly higher than the current rate of 8.45. With only 8 balls remaining and 4 wickets down...",
    "batting_strategy": "Rohit Sharma should continue aggressive approach as the situation demands quick runs. Suryakumar Yadav should provide support...",
    "run_rate_analysis": "Current RR is 8.45, need 12.5. The team needs to accelerate and score 21 runs in the last 8 balls to win..."
  }
}
```

**What to look for:**
- ✅ Status is "success"
- ✅ Shows pressure level
- ✅ Suggests aggressive/cautious approach
- ✅ Contains run rate analysis
- ✅ Predictions are realistic

---

### Test 4: Match Prediction Endpoint

**URL:**
```
http://127.0.0.1:8000/prediction
```

**Expected Response (with AI Predictions):**
```json
{
  "status": "success",
  "match_id": "IPL2024_001",
  "teams": "Mumbai Indians vs Royal Challengers Bangalore",
  "overs_left": 1.3,
  "predictions": {
    "final_score_prediction": "Projected Final Score: 177-182 with 65% confidence. Best case scenario (aggressive batting): 185+ runs. Worst case scenario (2-3 more wickets fall): 172-175 runs...",
    "winning_probability": "RCB has approximately 35% chance of winning based on current match situation. Mumbai needs to defend this score, and RCB would need to accelerate significantly...",
    "key_player_performance": "Rohit Sharma is likely to score 50+ runs. Jasprit Bumrah has 75% chance of taking a wicket in his remaining overs. Suryakumar Yadav may play a supporting role..."
  }
}
```

**What to look for:**
- ✅ Status is "success"
- ✅ Contains score prediction with range
- ✅ Shows winning probability percentage
- ✅ Predicts key player performance
- ✅ Includes confidence levels

---

### Test 5: Commentary Endpoint

**URL:**
```
http://127.0.0.1:8000/commentary
```

**Expected Response (Exciting Commentary):**
```json
{
  "status": "success",
  "match_summary": "Mumbai Indians vs Royal Challengers Bangalore",
  "current_status": "156/4 (18.3 overs)",
  "commentary": {
    "live_commentary": "OH WHAT A SHOT! THAT'S A SCREAMER OF A SIX OVER LONG-OFF! Rohit is ON FIRE! The batsman is absolutely DOMINATING this bowler! The crowd is going absolutely MAD!",
    "situation_analysis": "THIS IS DRAMA AT ITS FINEST! Mumbai needs 21 runs in just 8 balls! Can they pull off this MIRACULOUS chase? The tension is UNBEARABLE! Every ball could be the difference!",
    "batsman_description": "Rohit Sharma is BATTING OUT OF HIS SKIN! Strike rate of 140%! He's absolutely FLUENT in his strokeplay! The man is a BATTING GENIUS today!",
    "bowler_analysis": "Mohammed Siraj is STRUGGLING to contain this onslaught! The bowler is being taken apart! He needs to find some answers quickly or face a difficult day at the office!"
  }
}
```

**What to look for:**
- ✅ Status is "success"
- ✅ Live commentary is dramatic and engaging
- ✅ Uses cricket terminology correctly
- ✅ Situation analysis is exciting
- ✅ Batsman and bowler descriptions are vivid

---

## 🧪 Testing Different Match IDs

### Test Match 1 (Mumbai Indians)
```
http://127.0.0.1:8000/match?match_id=IPL2024_001
http://127.0.0.1:8000/bowling?match_id=IPL2024_001
http://127.0.0.1:8000/batting?match_id=IPL2024_001
```

### Test Match 2 (Delhi Capitals)
```
http://127.0.0.1:8000/match?match_id=IPL2024_002
http://127.0.0.1:8000/bowling?match_id=IPL2024_002
http://127.0.0.1:8000/batting?match_id=IPL2024_002
http://127.0.0.1:8000/prediction?match_id=IPL2024_002
http://127.0.0.1:8000/commentary?match_id=IPL2024_002
```

**Expected:** Both matches should return different data and analysis

---

## 📚 Testing in Swagger UI

### Step 1: Open Swagger UI
```
http://127.0.0.1:8000/docs
```

### Step 2: Test Each Endpoint

For each endpoint:
1. Find it in the list (match, bowling, batting, prediction, commentary)
2. Click on it to expand
3. Click "Try it out"
4. Optional: Edit match_id parameter
5. Click "Execute"
6. See the response below

### Step 3: Check Response

- Look for "status": "success"
- Check data is cricket-related
- Verify JSON format is correct
- Read AI analysis

---

## 🐍 Testing with Python

### Test 1: Direct Function Call

```python
# In Python terminal or script

from utils import fetch_live_match_data, validate_match_data
from agents.bowling_agent import get_bowling_analysis

# Get match data
match_data = fetch_live_match_data("IPL2024_001")

# Check if valid
if validate_match_data(match_data):
    print("✓ Match data is valid")
else:
    print("✗ Match data is invalid")

# Get bowling analysis
analysis = get_bowling_analysis(match_data)

# Print results
print("\nBatsman Weakness:")
print(analysis["batsman_weakness"])

print("\nNext Bowler Suggestion:")
print(analysis["next_bowler"])

print("\nBowling Strategy:")
print(analysis["bowling_strategy"])
```

### Test 2: Test All Agents

```python
from utils import fetch_live_match_data
from agents.bowling_agent import get_bowling_analysis
from agents.batting_agent import get_batting_analysis
from agents.prediction_agent import get_match_prediction
from agents.commentary_agent import get_match_commentary

match_data = fetch_live_match_data("IPL2024_001")

# Test each agent
bowling = get_bowling_analysis(match_data)
batting = get_batting_analysis(match_data)
prediction = get_match_prediction(match_data)
commentary = get_match_commentary(match_data)

print("✓ Bowling Analysis:", bowling["batsman_weakness"][:50] + "...")
print("✓ Batting Analysis:", batting["pressure_analysis"][:50] + "...")
print("✓ Prediction:", prediction["final_score_prediction"][:50] + "...")
print("✓ Commentary:", commentary["live_commentary"][:50] + "...")
```

### Test 3: Test API Endpoints with requests

```python
import requests

# Test /match endpoint
response = requests.get("http://127.0.0.1:8000/match")
print("Match endpoint:", response.status_code)
print(response.json()["batting_team"]["team_name"])

# Test /bowling endpoint
response = requests.get("http://127.0.0.1:8000/bowling")
print("\nBowling endpoint:", response.status_code)
print(response.json()["analysis"]["batsman_weakness"][:100])

# Test /prediction endpoint
response = requests.get("http://127.0.0.1:8000/prediction")
print("\nPrediction endpoint:", response.status_code)
print(response.json()["predictions"]["final_score_prediction"][:100])

# Test with different match
response = requests.get("http://127.0.0.1:8000/match?match_id=IPL2024_002")
print("\nMatch 2:", response.json()["batting_team"]["team_name"])
```

---

## ✅ Response Validation Checklist

### For All Endpoints:
- [ ] HTTP Status Code is 200 (success)
- [ ] Response is valid JSON
- [ ] Contains "status": "success"
- [ ] No "error" or "detail" fields (unless intentional)
- [ ] Response time is < 5 seconds

### For /match:
- [ ] Has batting_team with team_name, runs, wickets
- [ ] Has bowling_team with team_name
- [ ] Has current_batsman with name, runs, strike_rate
- [ ] Has current_bowler with name, economy
- [ ] Has required_run_rate and overs_left

### For /bowling:
- [ ] Has batsman_weakness analysis (multiple sentences)
- [ ] Has next_bowler_suggestion (with reasoning)
- [ ] Has bowling_strategy (actionable tips)
- [ ] AI mentions specific bowler names
- [ ] Analysis is cricket-specific

### For /batting:
- [ ] Has pressure_analysis (describes urgency)
- [ ] Has batting_strategy (suggests approach)
- [ ] Has run_rate_analysis (mathematical)
- [ ] Contains pressure level (LOW/MEDIUM/HIGH)
- [ ] Strategy is context-specific

### For /prediction:
- [ ] Has final_score_prediction (with range)
- [ ] Has winning_probability (percentage)
- [ ] Has key_player_performance
- [ ] Includes confidence levels
- [ ] Mentions specific scenarios (best/worst case)

### For /commentary:
- [ ] Has live_commentary (exciting language)
- [ ] Has situation_analysis (drama-focused)
- [ ] Has batsman_description (vivid details)
- [ ] Has bowler_analysis (performance critique)
- [ ] Uses cricket terminology correctly

---

## 🐛 Debugging Guide

### Error: "ModuleNotFoundError: No module named 'utils'"
**Cause:** Python can't find utils.py
**Fix:** Make sure utils.py is in backend folder (same level as main.py)

### Error: "No module named 'agents'"
**Cause:** agents/__init__.py is missing
**Fix:** Create agents/__init__.py file

### Error: "ValueError: GEMINI_API_KEY not found"
**Cause:** API key not in .env file
**Fix:** Add to .env: `GEMINI_API_KEY=your_actual_key`

### Error: "Invalid match data"
**Cause:** Match data structure is wrong
**Fix:** Check SAMPLE_MATCH_DATA in utils.py

### Error: "500 Internal Server Error"
**Cause:** Something failed in agent processing
**Fix:** Check server logs for detailed error message

### Error: "Response too long"
**Cause:** Gemini response is very large
**Fix:** It's okay, just take longer time. Gemini API calls can take 2-5 seconds

### Error: "Connection refused"
**Cause:** Server not running
**Fix:** Start server: `python -m uvicorn main:app --reload`

### Error: "Port 8000 already in use"
**Cause:** Another app using port 8000
**Fix:** Use different port: `python -m uvicorn main:app --reload --port 8001`

---

## 📊 Performance Testing

### Response Times

Expected response times:

| Endpoint | Time | Reason |
|----------|------|--------|
| /match | < 100ms | Just fetch mock data |
| /bowling | 2-5s | Calls Gemini AI (multiple functions) |
| /batting | 2-5s | Calls Gemini AI (multiple functions) |
| /prediction | 3-6s | Calls Gemini AI (complex analysis) |
| /commentary | 2-5s | Calls Gemini AI (multiple functions) |

**Note:** Gemini API calls take time because:
- Request sent to Google servers
- AI generates response
- Response sent back
- Total latency: network + processing

### Load Testing (Multiple Requests)

```python
import time
import requests

endpoints = [
    "http://127.0.0.1:8000/match",
    "http://127.0.0.1:8000/bowling",
    "http://127.0.0.1:8000/batting",
]

for endpoint in endpoints:
    start = time.time()
    response = requests.get(endpoint)
    duration = time.time() - start
    
    print(f"{endpoint}: {duration:.2f}s - {response.status_code}")
```

---

## ✨ Advanced Testing

### Test Error Handling

```python
# Test with invalid match_id
response = requests.get("http://127.0.0.1:8000/match?match_id=INVALID")
print(response.status_code)  # Should still work (returns mock data)

# Test with missing parameter (should use default)
response = requests.get("http://127.0.0.1:8000/match")
print(response.json()["match_id"])  # Should return IPL2024_001
```

### Test Data Consistency

```python
# Get same match twice
match1 = requests.get("http://127.0.0.1:8000/match?match_id=IPL2024_001").json()
match2 = requests.get("http://127.0.0.1:8000/match?match_id=IPL2024_001").json()

# Should be identical
assert match1 == match2
print("✓ Data consistency verified")
```

---

## 📋 Complete Testing Workflow

### Phase 1: Basic Testing (5 min)
1. Test /match endpoint
2. Verify JSON response
3. Check data is present

### Phase 2: AI Agent Testing (15 min)
1. Test /bowling endpoint
2. Test /batting endpoint
3. Test /prediction endpoint
4. Test /commentary endpoint
5. Verify AI generated content

### Phase 3: Advanced Testing (10 min)
1. Test different match IDs
2. Test in Swagger UI
3. Test with Python requests library
4. Check response times

### Phase 4: Integration Testing (5 min)
1. Test all endpoints in sequence
2. Verify data consistency
3. Check error handling

**Total Time:** ~35 minutes to fully test the system

---

## 🎉 Success Criteria

Your cricket AI system is working correctly if:

✅ All 5 endpoints return HTTP 200
✅ All responses are valid JSON
✅ All responses contain "status": "success"
✅ Bowling analysis mentions batsman weakness
✅ Batting analysis mentions required run rate
✅ Prediction includes winning probability
✅ Commentary uses cricket terminology
✅ Different match IDs return different data
✅ Response times are < 6 seconds
✅ No error messages in responses

---

That's it! You now have complete testing instructions! 🏏✨
