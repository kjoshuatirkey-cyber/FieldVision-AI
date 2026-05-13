"""
Bowling Analysis Agent
Uses Gemini AI to analyze bowling strategies and suggest next bowler
"""

from ai import ask_ai
from typing import Dict, Any


def analyze_batsman_weakness(match_data: Dict[str, Any]) -> str:
    """
    Analyze current batsman's weakness using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI analysis of batsman weakness
    """
    batsman = match_data["current_batsman"]
    recent_balls = match_data.get("recent_balls", [])
    
    # Create a prompt for Gemini to analyze
    prompt = f"""
    Analyze the batting weakness of {batsman['name']} based on this data:
    
    Current Stats:
    - Runs: {batsman['runs']}
    - Balls Faced: {batsman['balls_faced']}
    - Strike Rate: {batsman['strike_rate']}%
    - Fours: {batsman.get('fours', 'N/A')}
    - Sixes: {batsman.get('sixes', 'N/A')}
    
    Recent Balls: {recent_balls}
    
    Please identify:
    1. Which type of balls does the batsman struggle against?
    2. Is the batsman aggressive or cautious?
    3. What are the weaknesses?
    4. Suggest the bowling strategy to exploit these weaknesses.
    
    Keep the response concise and actionable.
    """
    
    # Get analysis from Gemini
    analysis = ask_ai(prompt)
    return analysis


def suggest_next_bowler(match_data: Dict[str, Any]) -> str:
    """
    Suggest the best bowler for the next over using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI suggestion for next bowler
    """
    current_bowler = match_data["current_bowler"]
    batsman = match_data["current_batsman"]
    bowling_team = match_data["bowling_team"]
    batting_team = match_data["batting_team"]
    
    # Example available bowlers (in real app, would come from squad data)
    available_bowlers = [
        {"name": "Jasprit Bumrah", "type": "fast", "economy": 6.5},
        {"name": "Yuzuki Chahal", "type": "spinner", "economy": 6.8},
        {"name": "Hardik Pandya", "type": "all-rounder", "economy": 7.2},
        {"name": "Anrich Nortje", "type": "fast", "economy": 7.0},
    ]
    
    prompt = f"""
    As a cricket analyst, suggest the best bowler for the next over.
    
    Current Situation:
    - Current Bowler: {current_bowler['name']} ({current_bowler['economy']:.2f} economy)
    - Overs Bowled: {current_bowler['overs_bowled']}
    - Current Batsman: {batsman['name']} (SR: {batsman['strike_rate']}%)
    - Match Situation: {batting_team['team_name']} needs {match_data['required_run_rate']:.2f} RR
    
    Available Bowlers:
    {str(available_bowlers)}
    
    Recommend the best bowler for the next over and explain why.
    Consider:
    1. Bowler's economy rate
    2. Batsman's weakness
    3. Match situation (aggressive vs defensive)
    
    Format: "Best Choice: [Bowler Name] because [reason]"
    """
    
    suggestion = ask_ai(prompt)
    return suggestion


def suggest_bowling_strategy(match_data: Dict[str, Any]) -> str:
    """
    Suggest overall bowling strategy using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI suggestion for bowling strategy
    """
    batting_team = match_data["batting_team"]
    bowling_team = match_data["bowling_team"]
    required_rr = match_data["required_run_rate"]
    
    prompt = f"""
    As an IPL cricket strategist, provide bowling strategy for {bowling_team['team_name']}.
    
    Match Status:
    - Batting Team: {batting_team['team_name']}
    - Current Score: {batting_team['total_runs']}/{batting_team['total_wickets']}
    - Overs Played: {batting_team['overs_played']}
    - Required Run Rate: {required_rr:.2f}
    - Overs Left: {match_data['overs_left']}
    
    Provide:
    1. Overall bowling strategy
    2. Field placement suggestions
    3. Risk areas to cover
    4. Key bowlers to focus on
    
    Keep response concise and practical.
    """
    
    strategy = ask_ai(prompt)
    return strategy


def get_bowling_analysis(match_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get complete bowling analysis using AI agents
    
    Args:
        match_data: Current match data
        
    Returns:
        Dictionary with bowling analysis
    """
    return {
        "batsman_weakness": analyze_batsman_weakness(match_data),
        "next_bowler": suggest_next_bowler(match_data),
        "bowling_strategy": suggest_bowling_strategy(match_data),
        "current_bowler": match_data["current_bowler"]["name"],
        "current_batsman": match_data["current_batsman"]["name"]
    }
