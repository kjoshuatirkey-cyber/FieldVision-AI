"""
Cricket Data Utils
Handles fetching and providing cricket match data
"""

import requests
from typing import Dict, Any

# Sample IPL Match Data (Mock Data for Testing)
# In a real application, this would come from a live cricket API
SAMPLE_MATCH_DATA = {
    "match_id": "IPL2024_001",
    "match_name": "Mumbai Indians vs Royal Challengers Bangalore",
    "venue": "Wankhede Stadium, Mumbai",
    "date": "2024-05-13",
    "toss_winner": "Mumbai Indians",
    "toss_decision": "bat",
    
    # Batting Team (Currently batting)
    "batting_team": {
        "team_name": "Mumbai Indians",
        "team_short": "MI",
        "total_runs": 156,
        "total_wickets": 4,
        "overs_played": 18.3,
        "run_rate": 8.45,
    },
    
    # Bowling Team (Currently bowling)
    "bowling_team": {
        "team_name": "Royal Challengers Bangalore",
        "team_short": "RCB",
    },
    
    # Current Batsmen
    "current_batsman": {
        "name": "Rohit Sharma",
        "runs": 45,
        "balls_faced": 32,
        "strike_rate": 140.6,
        "fours": 4,
        "sixes": 1,
    },
    
    "non_striker": {
        "name": "Suryakumar Yadav",
        "runs": 38,
        "balls_faced": 28,
        "strike_rate": 135.7,
        "fours": 3,
        "sixes": 1,
    },
    
    # Current Bowler
    "current_bowler": {
        "name": "Mohammed Siraj",
        "overs_bowled": 3.3,
        "runs_given": 28,
        "wickets_taken": 0,
        "economy": 8.4,
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
    "overs_left": 1.3,
    "required_run_rate": 12.5,
    "balls_left": 8,
    
    # Powerplay/Fielding Info
    "powerplay_overs": 6,
    "fielding_restrictions": "5 fielders in circle",
    
    # Recent Wickets
    "recent_wickets": [
        {
            "player": "Ishan Kishan",
            "runs_scored": 25,
            "dismissal": "caught by Virat Kohli, bowled by Yuzuki Chahal",
            "over": 10
        },
        {
            "player": "Hardik Pandya",
            "runs_scored": 18,
            "dismissal": "LBW, bowled by Mohammed Siraj",
            "over": 15
        }
    ]
}

# Alternative Sample Match Data (Different Scenario)
SAMPLE_MATCH_DATA_2 = {
    "match_id": "IPL2024_002",
    "match_name": "Delhi Capitals vs Kolkata Knight Riders",
    "venue": "Arun Jaitley Stadium, Delhi",
    "date": "2024-05-14",
    
    "batting_team": {
        "team_name": "Delhi Capitals",
        "team_short": "DC",
        "total_runs": 89,
        "total_wickets": 5,
        "overs_played": 12.2,
        "run_rate": 7.25,
    },
    
    "bowling_team": {
        "team_name": "Kolkata Knight Riders",
        "team_short": "KKR",
    },
    
    "current_batsman": {
        "name": "Rishabh Pant",
        "runs": 22,
        "balls_faced": 18,
        "strike_rate": 122.2,
    },
    
    "non_striker": {
        "name": "Axar Patel",
        "runs": 8,
        "balls_faced": 15,
        "strike_rate": 53.3,
    },
    
    "current_bowler": {
        "name": "Varun Chakaravarthy",
        "overs_bowled": 2.2,
        "runs_given": 15,
        "wickets_taken": 1,
        "economy": 6.43,
    },
    
    "match_status": "ongoing",
    "overs_left": 7.4,
    "required_run_rate": 14.8,
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
    if match_id == "IPL2024_002":
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
        
        # For now, return mock data
        return get_mock_match_data(match_id)
        
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
