"""
Batting Analysis Agent
Uses Gemini AI to analyze batting strategies and suggest tactics
"""

from ai import ask_ai
from typing import Dict, Any


def analyze_batting_pressure(match_data: Dict[str, Any]) -> str:
    """
    Analyze batting pressure and urgency using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI analysis of batting pressure
    """
    batting_team = match_data["batting_team"]
    required_rr = match_data["required_run_rate"]
    current_rr = batting_team["run_rate"]
    
    prompt = f"""
    Analyze the batting pressure in this IPL match.
    
    Current Situation:
    - Team: {batting_team['team_name']}
    - Score: {batting_team['total_runs']}/{batting_team['total_wickets']}
    - Overs Played: {batting_team['overs_played']}
    - Overs Left: {match_data['overs_left']}
    - Current Run Rate: {current_rr:.2f}
    - Required Run Rate: {required_rr:.2f}
    - Pressure Differential: {(required_rr - current_rr):.2f}
    
    Please analyze:
    1. How much pressure is the team under?
    2. Is the situation recoverable?
    3. What is the risk level (low/medium/high)?
    4. Short-term vs long-term strategy needed?
    
    Provide a brief but insightful analysis.
    """
    
    analysis = ask_ai(prompt)
    return analysis


def suggest_batting_strategy(match_data: Dict[str, Any]) -> str:
    """
    Suggest batting strategy using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI suggestion for batting strategy
    """
    batsman = match_data["current_batsman"]
    non_striker = match_data["non_striker"]
    bowling_team = match_data["bowling_team"]
    batting_team = match_data["batting_team"]
    
    prompt = f"""
    As an IPL batting coach, suggest strategy for {batting_team['team_name']}.
    
    Current Batsmen:
    - {batsman['name']}: {batsman['runs']} runs (SR: {batsman['strike_rate']}%)
    - {non_striker['name']}: {non_striker['runs']} runs (SR: {non_striker['strike_rate']}%)
    
    Bowling Attack: {bowling_team['team_name']}
    Current Bowler: {match_data['current_bowler']['name']} ({match_data['current_bowler']['economy']:.2f} economy)
    
    Match Context:
    - Required RR: {match_data['required_run_rate']:.2f}
    - Current RR: {batting_team['run_rate']:.2f}
    - Overs Left: {match_data['overs_left']}
    
    Suggest:
    1. Should batsmen be aggressive or cautious?
    2. Who should take more risk - striker or non-striker?
    3. Target runs for next 3 overs?
    4. Key areas to score (boundaries, singles)?
    
    Keep it practical and tactical.
    """
    
    strategy = ask_ai(prompt)
    return strategy


def analyze_run_rate(match_data: Dict[str, Any]) -> str:
    """
    Analyze run rate and suggest adjustments using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI analysis of run rate
    """
    batting_team = match_data["batting_team"]
    current_rr = batting_team["run_rate"]
    required_rr = match_data["required_run_rate"]
    overs_left = match_data["overs_left"]
    
    prompt = f"""
    Analyze the run rate in this IPL match.
    
    Run Rate Analysis:
    - Current RR: {current_rr:.2f}
    - Required RR: {required_rr:.2f}
    - Difference: {(required_rr - current_rr):.2f}
    - Overs Left: {overs_left}
    - Balls Left: {int(overs_left * 6)}
    
    Team Score: {batting_team['total_runs']}/{batting_team['total_wickets']} ({batting_team['overs_played']} overs)
    
    Please provide:
    1. Is the current run rate sustainable?
    2. Can the team reach the target?
    3. What run rate is needed in remaining overs?
    4. Risk assessment (can they accelerate safely)?
    
    Be analytical and data-driven.
    """
    
    analysis = ask_ai(prompt)
    return analysis


def get_batting_analysis(match_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get complete batting analysis using AI agents
    
    Args:
        match_data: Current match data
        
    Returns:
        Dictionary with batting analysis
    """
    return {
        "pressure_analysis": analyze_batting_pressure(match_data),
        "batting_strategy": suggest_batting_strategy(match_data),
        "run_rate_analysis": analyze_run_rate(match_data),
        "batting_team": match_data["batting_team"]["team_name"],
        "current_score": f"{match_data['batting_team']['total_runs']}/{match_data['batting_team']['total_wickets']}"
    }
