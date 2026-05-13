"""
Cricket data provider layer.

The platform can use a live cricket API when credentials are configured, while
keeping a reliable local fallback for development, demos, and failed providers.
"""

from __future__ import annotations

import os
from datetime import UTC, datetime, timedelta
from typing import Any, Literal

import requests

from utils import get_mock_match_data

MatchType = Literal["all", "live", "upcoming", "past"]


def _now() -> datetime:
    return datetime.now(UTC)


def _iso(days: int, hour: int = 14) -> str:
    value = _now() + timedelta(days=days)
    return value.replace(hour=hour, minute=0, second=0, microsecond=0).isoformat()


def _score_from_team(team: dict[str, Any]) -> str:
    runs = team.get("total_runs", 0)
    wickets = team.get("total_wickets", 0)
    overs = team.get("overs_played", 0)
    return f"{runs}/{wickets} ({overs})"


def _mock_match_card(match_data: dict[str, Any], status: str, starts_at: str) -> dict[str, Any]:
    batting = match_data["batting_team"]
    bowling = match_data["bowling_team"]

    return {
        "id": match_data.get("match_id", "IPL2024_001"),
        "name": match_data.get("match_name", f"{batting['team_name']} vs {bowling['team_name']}"),
        "status": status,
        "venue": match_data.get("venue", "TBC"),
        "starts_at": starts_at,
        "teams": [batting["team_name"], bowling["team_name"]],
        "score": _score_from_team(batting) if status != "upcoming" else "Fixture",
        "source": "mock",
    }


def get_mock_matches(match_type: MatchType = "all") -> list[dict[str, Any]]:
    primary = get_mock_match_data("IPL2026_057")
    secondary = get_mock_match_data("IPL2026_058")

    matches = [
        _mock_match_card(primary, "live", "2026-05-13T14:00:00+00:00"),
        {
            "id": "IPL2026_058",
            "name": "Punjab Kings vs Chennai Super Kings",
            "status": "upcoming",
            "venue": "HPCA Stadium, Dharamshala",
            "starts_at": "2026-05-14T14:00:00+00:00",
            "teams": ["Punjab Kings", "Chennai Super Kings"],
            "score": "Fixture",
            "source": "mock",
        },
        {
            "id": "IPL2026_059",
            "name": "Lucknow Super Giants vs Gujarat Titans",
            "status": "upcoming",
            "venue": "BRSABV Ekana Cricket Stadium, Lucknow",
            "starts_at": "2026-05-15T14:00:00+00:00",
            "teams": ["Lucknow Super Giants", "Gujarat Titans"],
            "score": "Fixture",
            "source": "mock",
        },
        {
            "id": "IPL2026_060",
            "name": "Kolkata Knight Riders vs Royal Challengers Bengaluru",
            "status": "upcoming",
            "venue": "Eden Gardens, Kolkata",
            "starts_at": "2026-05-16T14:00:00+00:00",
            "teams": ["Kolkata Knight Riders", "Royal Challengers Bengaluru"],
            "score": "Fixture",
            "source": "mock",
        },
        {
            "id": "IPL2026_056",
            "name": "Gujarat Titans vs Sunrisers Hyderabad",
            "status": "past",
            "venue": "Narendra Modi Stadium, Ahmedabad",
            "starts_at": "2026-05-12T14:00:00+00:00",
            "teams": ["Gujarat Titans", "Sunrisers Hyderabad"],
            "score": "GT 168/5 beat SRH 86 by 82 runs",
            "source": "mock",
        },
        {
            "id": "IPL2026_055",
            "name": "Punjab Kings vs Delhi Capitals",
            "status": "past",
            "venue": "HPCA Stadium, Dharamshala",
            "starts_at": "2026-05-11T14:00:00+00:00",
            "teams": ["Punjab Kings", "Delhi Capitals"],
            "score": "DC 216/7 beat PBKS 210/5 by 6 runs",
            "source": "mock",
        },
        {
            "id": "IPL2026_054",
            "name": "Royal Challengers Bengaluru vs Mumbai Indians",
            "status": "past",
            "venue": "Shaheed Veer Narayan Singh International Stadium, Raipur",
            "starts_at": "2026-05-10T14:00:00+00:00",
            "teams": ["Royal Challengers Bengaluru", "Mumbai Indians"],
            "score": "RCB 167/8 beat MI 166/7 by 1 run",
            "source": "mock",
        },
    ]

    if match_type == "all":
        return matches
    return [match for match in matches if match["status"] == match_type]


def _normalize_cricapi_match(raw: dict[str, Any]) -> dict[str, Any]:
    status_text = str(raw.get("status") or "").lower()
    match_started = bool(raw.get("matchStarted"))
    match_ended = bool(raw.get("matchEnded"))

    if match_ended or "won" in status_text or "draw" in status_text:
        status = "past"
    elif match_started or "live" in status_text or "need" in status_text:
        status = "live"
    else:
        status = "upcoming"

    teams = raw.get("teams") or []
    score = raw.get("score") or []
    score_text = "Fixture"
    if isinstance(score, list) and score:
        innings = []
        for item in score:
            if isinstance(item, dict):
                innings.append(
                    f"{item.get('inning', 'Innings')}: {item.get('r', 0)}/{item.get('w', 0)} ({item.get('o', 0)})"
                )
        score_text = " | ".join(innings) or str(raw.get("status") or "Live")
    elif raw.get("status"):
        score_text = str(raw["status"])

    return {
        "id": raw.get("id") or raw.get("unique_id") or raw.get("match_id"),
        "name": raw.get("name") or raw.get("title") or "Cricket match",
        "status": status,
        "venue": raw.get("venue") or "Venue TBC",
        "starts_at": raw.get("dateTimeGMT") or raw.get("date") or "",
        "teams": teams,
        "score": score_text,
        "source": "cricapi",
    }


def _request_cricapi(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    api_key = os.getenv("CRICAPI_KEY") or os.getenv("CRICKETDATA_API_KEY")
    if not api_key:
        raise RuntimeError("CRICAPI_KEY is not configured.")

    base_url = os.getenv("CRICAPI_BASE_URL", "https://api.cricapi.com/v1").rstrip("/")
    request_params = {"apikey": api_key, **(params or {})}
    response = requests.get(f"{base_url}/{path.lstrip('/')}", params=request_params, timeout=10)
    response.raise_for_status()
    return response.json()


def _fetch_cricapi_matches(match_type: MatchType) -> list[dict[str, Any]]:
    paths = ["currentMatches"] if match_type == "live" else ["currentMatches", "matches"]
    items: list[dict[str, Any]] = []

    for path in paths:
        payload = _request_cricapi(path, {"offset": 0})
        data = payload.get("data") or []
        if isinstance(data, list):
            items.extend(_normalize_cricapi_match(match) for match in data if isinstance(match, dict))

    seen: set[str] = set()
    unique = []
    for match in items:
        match_id = str(match.get("id") or match.get("name"))
        if match_id not in seen:
            seen.add(match_id)
            unique.append(match)

    series_filter = [
        item.strip().lower()
        for item in os.getenv("CRICKET_SERIES_FILTER", "ipl,indian premier league,t20").split(",")
        if item.strip()
    ]
    if series_filter:
        filtered = [
            match
            for match in unique
            if any(term in f"{match.get('name', '')} {match.get('venue', '')}".lower() for term in series_filter)
        ]
        unique = filtered or unique

    if match_type == "all":
        return unique
    return [match for match in unique if match["status"] == match_type]


def list_matches(match_type: MatchType = "all") -> dict[str, Any]:
    provider = os.getenv("CRICKET_DATA_PROVIDER", "auto").lower()

    if provider in {"auto", "cricapi"}:
        try:
            matches = _fetch_cricapi_matches(match_type)
            if matches:
                return {"provider": "cricapi", "status": "ready", "matches": matches}
        except Exception as exc:
            if provider == "cricapi":
                return {
                    "provider": "cricapi",
                    "status": "error",
                    "error": str(exc),
                    "matches": get_mock_matches(match_type),
                }

    return {"provider": "mock", "status": "fallback", "matches": get_mock_matches(match_type)}


def get_match_detail(match_id: str | None = None) -> dict[str, Any]:
    if match_id in {None, "", "IPL2026_057", "IPL2024_001"}:
        return get_mock_match_data("IPL2026_057")

    if match_id in {"IPL2026_058", "IPL2024_002"}:
        return get_mock_match_data("IPL2026_058")

    matches = get_mock_matches("all")
    card = next((match for match in matches if match["id"] == match_id), None)
    if card and card["status"] in {"upcoming", "past"}:
        data = get_mock_match_data("IPL2026_057")
        home, away = card["teams"]
        data["match_id"] = card["id"]
        data["match_name"] = card["name"]
        data["venue"] = card["venue"]
        data["match_status"] = card["status"]
        data["batting_team"]["team_name"] = home
        data["batting_team"]["team_short"] = "".join(word[0] for word in home.split()[:3]).upper()
        data["bowling_team"]["team_name"] = away
        data["bowling_team"]["team_short"] = "".join(word[0] for word in away.split()[:3]).upper()
        if card["status"] == "past":
            data["batting_team"]["total_runs"] = 0
            data["batting_team"]["total_wickets"] = 0
            data["batting_team"]["overs_played"] = 20.0
            data["required_run_rate"] = 0.0
            data["overs_left"] = 0.0
        return data

    return get_mock_match_data("IPL2026_057")


def platform_summary() -> dict[str, Any]:
    all_matches = list_matches("all")
    matches = all_matches["matches"]

    return {
        "provider": all_matches["provider"],
        "status": all_matches["status"],
        "counts": {
            "live": len([match for match in matches if match["status"] == "live"]),
            "upcoming": len([match for match in matches if match["status"] == "upcoming"]),
            "past": len([match for match in matches if match["status"] == "past"]),
            "all": len(matches),
        },
        "featured": matches[:6],
    }
