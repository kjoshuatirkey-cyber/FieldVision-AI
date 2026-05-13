"""
Cricket Data Utils
Handles fetching and providing cricket match data
"""

import requests
from typing import Dict, Any

# Sample IPL Match Data (Mock Data for Testing)
# In a real application, this would come from a live cricket API
SAMPLE_MATCH_DATA = {
    "match_id": "IPL2026_057",
    "match_name": "Royal Challengers Bengaluru vs Kolkata Knight Riders",
    "venue": "Shaheed Veer Narayan Singh International Stadium, Raipur",
    "date": "2026-05-13",
    "toss_winner": "Royal Challengers Bengaluru",
    "toss_decision": "bat",
    
    # Batting Team (Currently batting)
    "batting_team": {
        "team_name": "Royal Challengers Bengaluru",
        "team_short": "RCB",
        "total_runs": 142,
        "total_wickets": 3,
        "overs_played": 16.2,
        "run_rate": 8.69,
    },
    
    # Bowling Team (Currently bowling)
    "bowling_team": {
        "team_name": "Kolkata Knight Riders",
        "team_short": "KKR",
    },
    
    # Current Batsmen
    "current_batsman": {
        "name": "Virat Kohli",
        "runs": 58,
        "balls_faced": 39,
        "strike_rate": 148.7,
        "fours": 6,
        "sixes": 2,
    },
    
    "non_striker": {
        "name": "Rajat Patidar",
        "runs": 31,
        "balls_faced": 22,
        "strike_rate": 140.9,
        "fours": 2,
        "sixes": 2,
    },
    
    # Current Bowler
    "current_bowler": {
        "name": "Sunil Narine",
        "overs_bowled": 3.2,
        "runs_given": 24,
        "wickets_taken": 1,
        "economy": 7.2,
    },
    
    # Recent Balls
    "recent_balls": [
        {"type": "run", "runs": 1},
        {"type": "dot"},
        {"type": "four"},
        {"type": "run", "runs": 2},
        {"type": "dot"},
        {"type": "six"},
    ],
    
    # Match Status
    "match_status": "ongoing",
    "overs_left": 3.4,
    "required_run_rate": 9.8,
    "balls_left": 22,
    
    # Powerplay/Fielding Info
    "powerplay_overs": 6,
    "fielding_restrictions": "5 fielders in circle",
    
    # Recent Wickets
    "recent_wickets": [
        {
            "player": "Ishan Kishan",
            "runs_scored": 25,
            "dismissal": "caught by Rinku Singh, bowled by Varun Chakaravarthy",
            "over": 9
        },
        {
            "player": "Glenn Maxwell",
            "runs_scored": 19,
            "dismissal": "caught by Andre Russell, bowled by Sunil Narine",
            "over": 14
        }
    ]
}

# Alternative Sample Match Data (Different Scenario)
SAMPLE_MATCH_DATA_2 = {
    "match_id": "IPL2026_058",
    "match_name": "Punjab Kings vs Chennai Super Kings",
    "venue": "HPCA Stadium, Dharamshala",
    "date": "2026-05-14",
    
    "batting_team": {
        "team_name": "Punjab Kings",
        "team_short": "PBKS",
        "total_runs": 0,
        "total_wickets": 0,
        "overs_played": 0.0,
        "run_rate": 0.0,
    },
    
    "bowling_team": {
        "team_name": "Chennai Super Kings",
        "team_short": "CSK",
    },
    
    "current_batsman": {
        "name": "Prabhsimran Singh",
        "runs": 0,
        "balls_faced": 0,
        "strike_rate": 0.0,
    },
    
    "non_striker": {
        "name": "Shashank Singh",
        "runs": 0,
        "balls_faced": 0,
        "strike_rate": 0.0,
    },
    
    "current_bowler": {
        "name": "Matheesha Pathirana",
        "overs_bowled": 0.0,
        "runs_given": 0,
        "wickets_taken": 0,
        "economy": 0.0,
    },
    
    "match_status": "upcoming",
    "overs_left": 20.0,
    "required_run_rate": 0.0,
}


def get_mock_match_data(match_id: str = "IPL2024_001") -> Dict[str, Any]:
    """
    Get mock cricket match data for testing
    
    Args:
        match_id: ID of the match (for routing to different matches)
        
    Returns:
        Dictionary containing match data
        
    Example:
        >>> data = get_mock_match_data("IPL2024_001")
        >>> print(data["batting_team"]["team_name"])
        "Mumbai Indians"
    """
    if match_id in {"IPL2026_058", "IPL2024_002"}:
        return SAMPLE_MATCH_DATA_2
    return SAMPLE_MATCH_DATA


def fetch_live_match_data(match_id: str = None) -> Dict[str, Any]:
    """
    Fetch live cricket match data
    
    In a real application, this would:
    1. Call a live cricket API (like Cricketdata.org, RapidAPI, etc.)
    2. Parse the JSON response
    3. Return formatted data
    
    For now, we use mock data for testing.
    
    Args:
        match_id: Optional match ID to fetch specific match
        
    Returns:
        Match data as dictionary
        
    Raises:
        Exception: If API call fails or data is invalid
    """
    try:
        # In production, this would be a real API call:
        # response = requests.get(
        #     "https://api.cricketdata.org/live-match",
        #     params={"match_id": match_id},
        #     headers={"Authorization": "Bearer YOUR_API_KEY"}
        # )
        # response.raise_for_status()
        # return response.json()
        
        from cricket_data import get_match_detail

        return get_match_detail(match_id)
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch match data: {str(e)}")
    except ValueError as e:
        raise Exception(f"Invalid match data format: {str(e)}")


def get_match_summary(match_data: Dict[str, Any]) -> str:
    """
    Create a text summary of current match status
    
    Args:
        match_data: Match data dictionary
        
    Returns:
        Formatted summary string
    """
    batting = match_data["batting_team"]
    bowling = match_data["bowling_team"]
    batsman = match_data["current_batsman"]
    bowler = match_data["current_bowler"]
    
    summary = f"""
    MATCH SUMMARY
    =============
    
    {batting["team_name"]} vs {bowling["team_name"]}
    
    BATTING: {batting["team_name"]}
    Score: {batting["total_runs"]}/{batting['total_wickets']} in {batting['overs_played']} overs
    Run Rate: {batting['run_rate']:.2f} | Required RR: {match_data['required_run_rate']:.2f}
    
    BATSMEN:
    - {batsman['name']}: {batsman['runs']} ({batsman['balls_faced']} balls) | SR: {batsman['strike_rate']}%
    - {match_data['non_striker']['name']}: {match_data['non_striker']['runs']} ({match_data['non_striker']['balls_faced']} balls)
    
    BOWLER:
    - {bowler['name']}: {bowler['overs_bowled']} overs, {bowler['runs_given']} runs, {bowler['wickets_taken']} wickets
    
    STATUS: {match_data['match_status']} | {match_data['overs_left']} overs left
    """
    return summary


def validate_match_data(match_data: Dict[str, Any]) -> bool:
    """
    Validate that match data has all required fields
    
    Args:
        match_data: Match data to validate
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = [
        "batting_team",
        "bowling_team",
        "current_batsman",
        "current_bowler",
        "match_status"
    ]
    
    for field in required_fields:
        if field not in match_data:
            return False
    
    return True
