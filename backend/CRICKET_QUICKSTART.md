# ⚡ Cricket AI System - Quick Start

## 🚀 Setup (3 minutes)

### 1. Install Package
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Start Server
```powershell
python -m uvicorn main:app --reload
```

### 3. Test Endpoints
Open in browser:
- `http://127.0.0.1:8000/match` - Match data
- `http://127.0.0.1:8000/bowling` - Bowling analysis
- `http://127.0.0.1:8000/batting` - Batting analysis
- `http://127.0.0.1:8000/prediction` - Match predictions
- `http://127.0.0.1:8000/commentary` - Cricket commentary

---

## 📊 Sample Responses

### /match
Returns live match data:
```json
{
  "batting_team": "Mumbai Indians",
  "score": "156/4 (18.3 overs)",
  "run_rate": 8.45
}
```

### /bowling
AI bowling analysis:
```json
{
  "batsman_weakness": "Struggles against yorkers...",
  "next_bowler": "Suggest Bumrah because...",
  "bowling_strategy": "Bowl tight lines..."
}
```

### /batting
AI batting strategy:
```json
{
  "pressure": "Under MEDIUM pressure",
  "strategy": "Continue aggressive approach...",
  "run_rate": "Need 12.5 RR..."
}
```

### /prediction
AI match predictions:
```json
{
  "final_score": "178-182 projected",
  "winning_chance": "65% for batting team",
  "key_player": "Rohit likely 50+..."
}
```

### /commentary
Exciting IPL commentary:
```json
{
  "live": "WHAT A SHOT! Six over long-off!",
  "situation": "Drama! 21 runs needed in 8 balls!",
  "batsman": "On FIRE with SR of 140%",
  "bowler": "Struggling to contain attack"
}
```

---

## 🧪 Test in Swagger UI

Go to: `http://127.0.0.1:8000/docs`

Click any endpoint → "Try it out" → "Execute"

---

## 🔄 Try Different Matches

```
/match?match_id=IPL2024_001
/match?match_id=IPL2024_002
```

---

## 📁 File Structure

```
agents/
├── bowling_agent.py
├── batting_agent.py
├── prediction_agent.py
└── commentary_agent.py

utils.py        # Cricket data
main.py         # Routes
```

---

## 🐛 Troubleshooting

| Issue | Fix |
|-------|-----|
| ModuleNotFoundError: requests | `pip install requests` |
| Server won't start | Check Gemini API key in .env |
| Agents not working | Check utils.py has mock data |
| JSON parse errors | Check .env file exists |

---

See **CRICKET_AI_GUIDE.md** for detailed documentation!
