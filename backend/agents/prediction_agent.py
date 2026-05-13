"""
Match Prediction Agent
Uses Gemini AI to predict match outcomes and final scores
"""

from ai import ask_ai
from typing import Dict, Any
import math


def predict_final_score(match_data: Dict[str, Any]) -> str:
    """
    Predict final score of the batting team using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI prediction of final score
    """
    batting_team = match_data["batting_team"]
    
    # Calculate potential score based on current trajectory
    overs_played = float(batting_team["overs_played"])
    overs_left = float(match_data["overs_left"])
    total_overs = 20
    
    current_runs = batting_team["total_runs"]
    current_rr = batting_team["run_rate"]
    expected_runs_remaining = int(current_rr * overs_left)
    projected_score = current_runs + expected_runs_remaining
    
    prompt = f"""
    Predict the final score for {batting_team['team_name']}.
    
    Current Match Data:
    - Team: {batting_team['team_name']}
    - Current Score: {current_runs}/{batting_team['total_wickets']}
    - Overs Played: {batting_team['overs_played']} out of 20
    - Current Run Rate: {current_rr:.2f}
    - Overs Remaining: {overs_left}
    - Projected Final Score (if RR continues): {projected_score}
    
    Batsman Analysis:
    - Striker: {match_data['current_batsman']['name']} ({match_data['current_batsman']['runs']} runs, SR: {match_data['current_batsman']['strike_rate']}%)
    - Non-Striker: {match_data['non_striker']['name']} ({match_data['non_striker']['runs']} runs)
    
    Wickets Status: {batting_team['total_wickets']}/10 (Still {10 - batting_team['total_wickets']} wickets left)
    
    Please predict:
    1. Most likely final score (with confidence level)
    2. Best case scenario (aggressive batting)
    3. Worst case scenario (wickets fall)
    4. Key factors affecting the prediction
    
    Format the prediction clearly with ranges.
    """
    
    prediction = ask_ai(prompt)
    return prediction


def predict_winning_probability(match_data: Dict[str, Any]) -> str:
    """
    Predict winning probability using AI analysis
    
    Args:
        match_data: Current match data
        
    Returns:
        AI prediction of winning probability
    """
    batting_team = match_data["batting_team"]
    required_rr = match_data["required_run_rate"]
    current_rr = batting_team["run_rate"]
    
    # Simple calculation for context
    rr_difference = required_rr - current_rr
    wickets_left = 10 - batting_team["total_wickets"]
    
    prompt = f"""
    Predict the winning probability for {match_data['bowling_team']['team_name']} 
    in the context of this IPL match.
    
    Situation Analysis:
    - {batting_team['team_name']} needs {required_rr:.2f} RR
    - Currently maintaining {current_rr:.2f} RR
    - RR Difference: {rr_difference:.2f}
    - Overs Left: {match_data['overs_left']}
    - Wickets Remaining: {wickets_left}
    
    Bowling Strength:
    - Current Bowler: {match_data['current_bowler']['name']} ({match_data['current_bowler']['economy']:.2f} economy)
    - Wickets Taken by Bowler: {match_data['current_bowler']['wickets_taken']}
    
    Based on this data, predict:
    1. Winning probability for {match_data['bowling_team']['team_name']} (0-100%)
    2. Key factors influencing this probability
    3. Critical moments/overs ahead
    4. What needs to happen for each team to win?
    
    Be realistic and data-driven in your assessment.
    """
    
    probability = ask_ai(prompt)
    return probability


def predict_key_player_performance(match_data: Dict[str, Any]) -> str:
    """
    Predict performance of key players using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI prediction of key player performance
    """
    batsman = match_data["current_batsman"]
    bowler = match_data["current_bowler"]
    
    prompt = f"""
    Predict key player performances for the remaining overs in this IPL match.
    
    Batsman Analysis:
    - Name: {batsman['name']}
    - Current Runs: {batsman['runs']} off {batsman['balls_faced']} balls
    - Strike Rate: {batsman['strike_rate']}%
    - Fours: {batsman.get('fours', 'N/A')}, Sixes: {batsman.get('sixes', 'N/A')}
    - Form: Looks {('in form' if batsman['strike_rate'] > 130 else 'struggling with timing')}
    
    Bowler Analysis:
    - Name: {bowler['name']}
    - Overs Bowled: {bowler['overs_bowled']}
    - Economy: {bowler['economy']:.2f}
    - Wickets: {bowler['wickets_taken']}
    - Runs Given: {bowler['runs_given']}
    
    Predict:
    1. Will the batsman get a big score (20+, 30+, 40+)?
    2. Will the bowler take a wicket in their remaining overs?
    3. Who is likely to be the match winner/MVP?
    4. Critical performance factors for each player
    
    Provide confident but realistic predictions.
    """
    
    prediction = ask_ai(prompt)
    return prediction


def get_match_prediction(match_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get complete match prediction using AI agents
    
    Args:
        match_data: Current match data
        
    Returns:
        Dictionary with match predictions
    """
    return {
        "final_score_prediction": predict_final_score(match_data),
        "winning_probability": predict_winning_probability(match_data),
        "key_player_performance": predict_key_player_performance(match_data),
        "match_id": match_data.get("match_id"),
        "teams": f"{match_data['batting_team']['team_name']} vs {match_data['bowling_team']['team_name']}",
        "overs_left": match_data["overs_left"]
    }
