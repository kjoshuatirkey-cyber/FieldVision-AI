"""
Commentary Agent
Uses Gemini AI to generate exciting IPL-style cricket commentary
"""

from ai import ask_ai
from typing import Dict, Any


def generate_live_commentary(match_data: Dict[str, Any]) -> str:
    """
    Generate exciting live match commentary using AI
    
    Args:
        match_data: Current match data
        
    Returns:
        AI-generated exciting commentary
    """
    batsman = match_data["current_batsman"]
    bowler = match_data["current_bowler"]
    batting_team = match_data["batting_team"]
    recent_balls = match_data.get("recent_balls", [])
    
    # Convert recent balls to readable format
    recent_summary = ""
    for i, ball in enumerate(recent_balls[-6:], 1):
        if ball["type"] == "dot":
            recent_summary += f"Ball {i}: DOT, "
        elif ball["type"] == "four":
            recent_summary += f"Ball {i}: FOUR, "
        elif ball["type"] == "six":
            recent_summary += f"Ball {i}: SIX, "
        else:
            runs = ball.get("runs", 1)
            recent_summary += f"Ball {i}: {runs} run(s), "
    
    prompt = f"""
    You are an exciting IPL cricket commentator. Generate live match commentary for this moment.
    
    Match Situation:
    - Batsman: {batsman['name']} ({batsman['runs']} runs off {batsman['balls_faced']} balls, SR: {batsman['strike_rate']}%)
    - Bowler: {bowler['name']} ({bowler['overs_bowled']} overs, {bowler['economy']:.2f} economy)
    - {batting_team['team_name']}: {batting_team['total_runs']}/{batting_team['total_wickets']} in {batting_team['overs_played']} overs
    - Required RR: {match_data['required_run_rate']:.2f}
    
    Last 6 Balls: {recent_summary}
    
    Please generate:
    1. An exciting commentary of the current over (in the style of famous IPL commentators)
    2. Key observations and drama
    3. Predictions for the next ball
    4. Keep it to 2-3 sentences maximum
    5. Make it thrilling and engaging!
    
    Remember: Use phrases like "OH THAT'S A SCREAMER!", "BATTER STRUGGLING", "WHAT A DELIVERY!"
    """
    
    commentary = ask_ai(prompt)
    return commentary


def generate_situation_commentary(match_data: Dict[str, Any]) -> str:
    """
    Generate commentary on overall match situation
    
    Args:
        match_data: Current match data
        
    Returns:
        AI-generated situation commentary
    """
    batting_team = match_data["batting_team"]
    bowling_team = match_data["bowling_team"]
    required_rr = match_data["required_run_rate"]
    current_rr = batting_team["run_rate"]
    
    prompt = f"""
    As an IPL cricket expert commentator, provide analysis of the current match situation.
    
    Match Context:
    - {batting_team['team_name']} vs {bowling_team['team_name']}
    - Score: {batting_team['total_runs']}/{batting_team['total_wickets']} ({batting_team['overs_played']} overs)
    - Required RR: {required_rr:.2f} | Current RR: {current_rr:.2f}
    - Overs Left: {match_data['overs_left']}
    
    Provide exciting match situation commentary covering:
    1. Current phase of the match
    2. Drama and tension level
    3. Key turning points so far
    4. What happens next?
    
    Make it exciting and dramatic, like a real IPL match!
    Keep it to 3-4 sentences.
    """
    
    situation = ask_ai(prompt)
    return situation


def generate_batsman_description(match_data: Dict[str, Any]) -> str:
    """
    Generate descriptive commentary about current batsman
    
    Args:
        match_data: Current match data
        
    Returns:
        AI-generated batsman description
    """
    batsman = match_data["current_batsman"]
    
    prompt = f"""
    Write an exciting IPL-style description of the batsman currently at the crease.
    
    Batsman: {batsman['name']}
    Runs: {batsman['runs']} off {batsman['balls_faced']} balls
    Strike Rate: {batsman['strike_rate']}%
    
    Include:
    1. Current form assessment
    2. Playing style (aggressive/cautious)
    3. Body language observations
    4. Likelihood of scoring in next delivery
    
    Make it dramatic and engaging! Use phrases like "on fire", "fighting back", "building an innings"
    Keep it to 2-3 sentences.
    """
    
    description = ask_ai(prompt)
    return description


def generate_bowler_analysis_commentary(match_data: Dict[str, Any]) -> str:
    """
    Generate exciting commentary about current bowler
    
    Args:
        match_data: Current match data
        
    Returns:
        AI-generated bowler analysis
    """
    bowler = match_data["current_bowler"]
    batsman = match_data["current_batsman"]
    
    prompt = f"""
    Provide exciting IPL-style commentary about the current bowler's performance.
    
    Bowler: {bowler['name']}
    Overs Bowled: {bowler['overs_bowled']}
    Runs Given: {bowler['runs_given']}
    Wickets: {bowler['wickets_taken']}
    Economy: {bowler['economy']:.2f}
    
    Facing: {batsman['name']} (SR: {batsman['strike_rate']}%)
    
    Analyze:
    1. Bowling performance so far
    2. Is the bowler getting it right?
    3. What's the challenge ahead?
    4. Predictions for next delivery
    
    Make it thrilling! Use cricket phrases and dramatic language.
    Keep it to 2-3 sentences.
    """
    
    analysis = ask_ai(prompt)
    return analysis


def get_match_commentary(match_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get complete match commentary using AI agents
    
    Args:
        match_data: Current match data
        
    Returns:
        Dictionary with various commentary
    """
    return {
        "live_commentary": generate_live_commentary(match_data),
        "situation_commentary": generate_situation_commentary(match_data),
        "batsman_description": generate_batsman_description(match_data),
        "bowler_analysis": generate_bowler_analysis_commentary(match_data),
        "match_summary": f"{match_data['batting_team']['team_name']} vs {match_data['bowling_team']['team_name']}",
        "current_status": f"{match_data['batting_team']['total_runs']}/{match_data['batting_team']['total_wickets']} ({match_data['batting_team']['overs_played']} overs)"
    }
