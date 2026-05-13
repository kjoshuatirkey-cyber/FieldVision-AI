"""
FieldVision AI Backend Server
Main FastAPI application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai import get_ai_response, ask_ai
from utils import fetch_live_match_data, validate_match_data, get_match_summary
from agents.bowling_agent import get_bowling_analysis
from agents.batting_agent import get_batting_analysis
from agents.prediction_agent import get_match_prediction
from agents.commentary_agent import get_match_commentary

# Create the FastAPI application instance
app = FastAPI(
    title="FieldVision AI Backend",
    description="Backend server for FieldVision AI analysis",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing) to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint - test if server is running
@app.get("/")
def home():
    """Welcome endpoint to verify the server is running"""
    return {"message": "FieldVision AI Backend Running"}

# Test Gemini AI endpoint
@app.get("/test-ai")
def test_ai():
    """
    Test endpoint to verify Gemini AI integration is working
    
    This sends a simple test prompt to Gemini and returns the response.
    Use this to verify your API key is working correctly.
    
    Returns:
        JSON with test results from Gemini
        
    Example response:
        {
            "status": "success",
            "prompt": "What is the capital of France?",
            "response": "The capital of France is Paris..."
        }
    """
    try:
        # Simple test prompt
        test_prompt = "What is the capital of France? Answer in one sentence."
        
        # Call the AI function
        ai_response = ask_ai(test_prompt)
        
        # Return success response
        return {
            "status": "success",
            "message": "Gemini AI is working correctly!",
            "prompt": test_prompt,
            "response": ai_response
        }
    
    except Exception as e:
        # If there's an error, return error details
        raise HTTPException(
            status_code=500,
            detail=f"Gemini API Error: {str(e)}"
        )

# AI analysis endpoint
@app.post("/analyze")
def analyze(text: str):
    """
    Analyze text using Gemini AI
    
    Args:
        text: The text to analyze
        
    Returns:
        Analysis result from Gemini
        
    Example:
        POST /analyze?text=Explain%20machine%20learning
    """
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

# ============================================================
# CRICKET AI AGENT ENDPOINTS
# ============================================================

# Get live match data endpoint
@app.get("/match")
def get_match_data(match_id: str = "IPL2024_001"):
    """
    Get live cricket match data
    
    Args:
        match_id: ID of the match (default: IPL2024_001)
        
    Returns:
        Match data with current statistics
        
    Example:
        GET /match?match_id=IPL2024_001
    """
    try:
        # Fetch match data
        match_data = fetch_live_match_data(match_id)
        
        # Validate the data
        if not validate_match_data(match_data):
            raise ValueError("Invalid match data structure")
        
        return {
            "status": "success",
            "match_id": match_data.get("match_id"),
            "match_name": match_data.get("match_name"),
            "batting_team": match_data["batting_team"],
            "bowling_team": match_data["bowling_team"],
            "current_batsman": match_data["current_batsman"],
            "current_bowler": match_data["current_bowler"],
            "required_run_rate": match_data.get("required_run_rate"),
            "overs_left": match_data.get("overs_left"),
            "match_status": match_data.get("match_status")
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching match data: {str(e)}"
        )

# Bowling analysis endpoint
@app.get("/bowling")
def get_bowling_recommendation(match_id: str = "IPL2024_001"):
    """
    Get AI-powered bowling analysis and recommendations
    
    Uses Gemini AI to analyze:
    - Current batsman weakness
    - Best next bowler to select
    - Overall bowling strategy
    
    Args:
        match_id: ID of the match
        
    Returns:
        Bowling analysis with AI recommendations
        
    Example:
        GET /bowling?match_id=IPL2024_001
    """
    try:
        # Fetch match data
        match_data = fetch_live_match_data(match_id)
        
        # Validate data
        if not validate_match_data(match_data):
            raise ValueError("Invalid match data")
        
        # Get bowling analysis from AI agent
        bowling_analysis = get_bowling_analysis(match_data)
        
        return {
            "status": "success",
            "match_id": match_id,
            "bowling_team": match_data["bowling_team"]["team_name"],
            "current_batsman": bowling_analysis["current_batsman"],
            "current_bowler": bowling_analysis["current_bowler"],
            "analysis": {
                "batsman_weakness": bowling_analysis["batsman_weakness"],
                "next_bowler_suggestion": bowling_analysis["next_bowler"],
                "bowling_strategy": bowling_analysis["bowling_strategy"]
            }
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Bowling analysis error: {str(e)}"
        )

# Batting analysis endpoint
@app.get("/batting")
def get_batting_recommendation(match_id: str = "IPL2024_001"):
    """
    Get AI-powered batting analysis and strategy
    
    Uses Gemini AI to analyze:
    - Batting pressure and urgency
    - Suggested batting strategy
    - Run rate analysis
    
    Args:
        match_id: ID of the match
        
    Returns:
        Batting analysis with AI recommendations
        
    Example:
        GET /batting?match_id=IPL2024_001
    """
    try:
        # Fetch match data
        match_data = fetch_live_match_data(match_id)
        
        # Validate data
        if not validate_match_data(match_data):
            raise ValueError("Invalid match data")
        
        # Get batting analysis from AI agent
        batting_analysis = get_batting_analysis(match_data)
        
        return {
            "status": "success",
            "match_id": match_id,
            "batting_team": batting_analysis["batting_team"],
            "current_score": batting_analysis["current_score"],
            "analysis": {
                "pressure_analysis": batting_analysis["pressure_analysis"],
                "batting_strategy": batting_analysis["batting_strategy"],
                "run_rate_analysis": batting_analysis["run_rate_analysis"]
            }
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Batting analysis error: {str(e)}"
        )

# Match prediction endpoint
@app.get("/prediction")
def get_match_prediction_analysis(match_id: str = "IPL2024_001"):
    """
    Get AI-powered match prediction and analysis
    
    Uses Gemini AI to predict:
    - Final score of batting team
    - Winning probability
    - Key player performance
    
    Args:
        match_id: ID of the match
        
    Returns:
        Match prediction with AI analysis
        
    Example:
        GET /prediction?match_id=IPL2024_001
    """
    try:
        # Fetch match data
        match_data = fetch_live_match_data(match_id)
        
        # Validate data
        if not validate_match_data(match_data):
            raise ValueError("Invalid match data")
        
        # Get predictions from AI agent
        predictions = get_match_prediction(match_data)
        
        return {
            "status": "success",
            "match_id": predictions["match_id"],
            "teams": predictions["teams"],
            "overs_left": predictions["overs_left"],
            "predictions": {
                "final_score": predictions["final_score_prediction"],
                "winning_probability": predictions["winning_probability"],
                "key_player_performance": predictions["key_player_performance"]
            }
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

# Commentary endpoint
@app.get("/commentary")
def get_match_commentary_analysis(match_id: str = "IPL2024_001"):
    """
    Get AI-powered IPL-style cricket commentary
    
    Uses Gemini AI to generate:
    - Live match commentary
    - Situation analysis
    - Player descriptions
    - Bowler analysis
    
    Args:
        match_id: ID of the match
        
    Returns:
        Exciting cricket commentary
        
    Example:
        GET /commentary?match_id=IPL2024_001
    """
    try:
        # Fetch match data
        match_data = fetch_live_match_data(match_id)
        
        # Validate data
        if not validate_match_data(match_data):
            raise ValueError("Invalid match data")
        
        # Get commentary from AI agent
        commentary = get_match_commentary(match_data)
        
        return {
            "status": "success",
            "match_summary": commentary["match_summary"],
            "current_status": commentary["current_status"],
            "commentary": {
                "live_commentary": commentary["live_commentary"],
                "situation_analysis": commentary["situation_commentary"],
                "batsman_description": commentary["batsman_description"],
                "bowler_analysis": commentary["bowler_analysis"]
            }
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Commentary generation error: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
def health_check():
    """Check if the server is healthy"""
    return {"status": "healthy", "service": "FieldVision AI Backend"}

if __name__ == "__main__":
    import uvicorn
    # This allows running: python main.py
    uvicorn.run(app, host="127.0.0.1", port=8000)
