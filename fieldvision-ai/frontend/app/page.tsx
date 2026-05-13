"use client";

import { useCallback, useEffect, useMemo, useState } from "react";

type MatchData = {
  status: string;
  match_id: string;
  match_name: string;
  batting_team: {
    team_name: string;
    team_short: string;
    total_runs: number;
    total_wickets: number;
    overs_played: number;
    run_rate: number;
  };
  bowling_team: {
    team_name: string;
    team_short: string;
  };
  current_batsman: {
    name: string;
    runs: number;
    balls_faced: number;
    strike_rate: number;
    fours?: number;
    sixes?: number;
  };
  current_bowler: {
    name: string;
    overs_bowled: number;
    runs_given: number;
    wickets_taken: number;
    economy: number;
  };
  required_run_rate: number;
  overs_left: number;
  match_status: string;
};

type AnalysisPayload = Record<string, unknown>;
type ViewKey = "commentary" | "bowling" | "batting" | "prediction";
type MatchFilter = "all" | "live" | "upcoming" | "past";

type MatchCard = {
  id: string;
  name: string;
  status: MatchFilter;
  venue: string;
  starts_at: string;
  teams: string[];
  score: string;
  source: string;
};

type PlatformSummary = {
  provider: string;
  status: string;
  counts: Record<MatchFilter, number>;
  featured: MatchCard[];
};

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

const views: { key: ViewKey; label: string }[] = [
  { key: "commentary", label: "Live Desk" },
  { key: "bowling", label: "Bowling" },
  { key: "batting", label: "Batting" },
  { key: "prediction", label: "Prediction" },
];

const filters: { key: MatchFilter; label: string }[] = [
  { key: "all", label: "All" },
  { key: "live", label: "Live" },
  { key: "upcoming", label: "Future" },
  { key: "past", label: "Past" },
];

const statusLabels: Record<MatchFilter, string> = {
  all: "All",
  live: "Live",
  upcoming: "Future",
  past: "Result",
};

function textFrom(value: unknown): string {
  if (typeof value === "string") return value;
  if (typeof value === "number") return String(value);
  if (!value) return "Waiting for analysis.";
  return JSON.stringify(value, null, 2);
}

function formatMatchTime(value: string): string {
  if (!value) return "Time TBC";

  try {
    return new Intl.DateTimeFormat("en-IN", {
      day: "numeric",
      month: "short",
      hour: "numeric",
      minute: "2-digit",
      hour12: true,
      timeZone: "Asia/Kolkata",
    }).format(new Date(value));
  } catch {
    return value;
  }
}

function analysisSections(view: ViewKey, payload: AnalysisPayload | null): [string, unknown][] {
  if (!payload) return [];

  if (view === "commentary") {
    const commentary = payload.commentary as AnalysisPayload | undefined;
    return [
      ["Live call", commentary?.live_commentary],
      ["Situation", commentary?.situation_analysis],
      ["Batter watch", commentary?.batsman_description],
      ["Bowler read", commentary?.bowler_analysis],
    ];
  }

  if (view === "bowling") {
    const analysis = payload.analysis as AnalysisPayload | undefined;
    return [
      ["Batter weakness", analysis?.batsman_weakness],
      ["Next bowler", analysis?.next_bowler_suggestion],
      ["Plan", analysis?.bowling_strategy],
    ];
  }

  if (view === "batting") {
    const analysis = payload.analysis as AnalysisPayload | undefined;
    return [
      ["Pressure", analysis?.pressure_analysis],
      ["Strategy", analysis?.batting_strategy],
      ["Run rate", analysis?.run_rate_analysis],
    ];
  }

  const predictions = payload.predictions as AnalysisPayload | undefined;
  return [
    ["Final score", predictions?.final_score],
    ["Win probability", predictions?.winning_probability],
    ["Key player", predictions?.key_player_performance],
  ];
}

export default function Home() {
  const [activeView, setActiveView] = useState<ViewKey>("commentary");
  const [matchFilter, setMatchFilter] = useState<MatchFilter>("all");
  const [activeMatchId, setActiveMatchId] = useState("IPL2026_057");
  const [summary, setSummary] = useState<PlatformSummary | null>(null);
  const [matchFeed, setMatchFeed] = useState<MatchCard[]>([]);
  const [match, setMatch] = useState<MatchData | null>(null);
  const [analysis, setAnalysis] = useState<Record<ViewKey, AnalysisPayload | null>>({
    commentary: null,
    bowling: null,
    batting: null,
    prediction: null,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);

  const loadDashboard = useCallback(async (matchId = activeMatchId) => {
    setLoading(true);
    setError("");

    try {
      const query = new URLSearchParams({ match_id: matchId });
      const [matchResponse, commentaryResponse, bowlingResponse, battingResponse, predictionResponse] =
        await Promise.all([
          fetch(`${API_BASE}/match?${query}`),
          fetch(`${API_BASE}/commentary?${query}`),
          fetch(`${API_BASE}/bowling?${query}`),
          fetch(`${API_BASE}/batting?${query}`),
          fetch(`${API_BASE}/prediction?${query}`),
        ]);

      const responses = [
        matchResponse,
        commentaryResponse,
        bowlingResponse,
        battingResponse,
        predictionResponse,
      ];

      if (responses.some((response) => !response.ok)) {
        throw new Error("Backend returned an error. Check the FastAPI terminal.");
      }

      const [matchJson, commentaryJson, bowlingJson, battingJson, predictionJson] =
        await Promise.all(responses.map((response) => response.json()));

      setMatch(matchJson);
      setAnalysis({
        commentary: commentaryJson,
        bowling: bowlingJson,
        batting: battingJson,
        prediction: predictionJson,
      });
      setLastUpdated(new Date());
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not reach the backend.");
    } finally {
      setLoading(false);
    }
  }, [activeMatchId]);

  const loadPlatform = useCallback(async (filter: MatchFilter = matchFilter) => {
    try {
      const [summaryResponse, matchesResponse] = await Promise.all([
        fetch(`${API_BASE}/platform/summary`),
        fetch(`${API_BASE}/matches?type=${filter}`),
      ]);

      if (!summaryResponse.ok || !matchesResponse.ok) {
        throw new Error("Could not load platform match feed.");
      }

      const [summaryJson, matchesJson] = await Promise.all([
        summaryResponse.json(),
        matchesResponse.json(),
      ]);

      setSummary(summaryJson);
      setMatchFeed(matchesJson.matches ?? []);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not reach the match platform.");
    }
  }, [matchFilter]);

  useEffect(() => {
    const timer = window.setTimeout(() => {
      void loadDashboard();
      void loadPlatform();
    }, 0);

    return () => window.clearTimeout(timer);
  }, [loadDashboard, loadPlatform]);

  const scoreLine = useMemo(() => {
    if (!match) return "--/--";
    return `${match.batting_team.total_runs}/${match.batting_team.total_wickets}`;
  }, [match]);

  const sections = analysisSections(activeView, analysis[activeView]);
  const activeFeedMatch = matchFeed.find((feedMatch) => feedMatch.id === activeMatchId);
  const runRatePressure = match
    ? Math.max(0, Math.min(100, (match.batting_team.run_rate / Math.max(match.required_run_rate, 1)) * 100))
    : 0;

  function selectMatch(matchId: string) {
    setActiveMatchId(matchId);
    void loadDashboard(matchId);
  }

  function selectFilter(filter: MatchFilter) {
    setMatchFilter(filter);
    void loadPlatform(filter);
  }

  return (
    <main className="min-h-screen overflow-hidden bg-[var(--page-bg)] text-[var(--ink)]">
      <section className="scoreboard-shell">
        <div className="scoreboard-topbar">
          <div>
            <p className="eyebrow">FieldVision AI</p>
            <h1>IPL T20 2026 command center</h1>
          </div>
          <div className="topbar-actions">
            <span className={summary?.status === "ready" ? "source-pill ready" : "source-pill"}>
              {summary ? `${summary.provider} ${summary.status}` : "connecting"}
            </span>
            <button className="refresh-button" onClick={() => loadDashboard()} disabled={loading}>
              {loading ? "Syncing" : "Refresh"}
            </button>
          </div>
        </div>

        <div className="match-strip">
          <div>
            <span className="label">Selected fixture</span>
            <strong>{match?.match_name ?? "Connecting to match feed"}</strong>
          </div>
          <div>
            <span className="label">Start</span>
            <strong>{activeFeedMatch ? formatMatchTime(activeFeedMatch.starts_at) : "Loading"}</strong>
          </div>
          <div>
            <span className="label">Coverage</span>
            <strong>
              {summary
                ? `${summary.counts.live} live, ${summary.counts.upcoming} future, ${summary.counts.past} past`
                : "--"}
            </strong>
          </div>
        </div>

        {error ? (
          <div className="error-panel">
            <strong>Backend is not reachable.</strong>
            <span>{error}</span>
            <code>{API_BASE}</code>
          </div>
        ) : null}

        <div className="dashboard-grid">
          <section className="platform-panel">
            <div className="panel-heading">
              <div>
                <span className="label">Match feed</span>
                <h2>IPL fixtures</h2>
              </div>
              <span>{matchFeed.length}</span>
            </div>

            <div className="view-tabs compact" role="tablist" aria-label="Match filters">
              {filters.map((filter) => (
                <button
                  key={filter.key}
                  className={matchFilter === filter.key ? "active" : ""}
                  onClick={() => selectFilter(filter.key)}
                  aria-selected={matchFilter === filter.key}
                  role="tab"
                  type="button"
                >
                  {filter.label}
                </button>
              ))}
            </div>

            <div className="match-list">
              {matchFeed.length === 0 ? (
                <div className="empty-state">
                  <strong>No fixtures found</strong>
                  <span>Try another filter or check the cricket data provider.</span>
                </div>
              ) : matchFeed.map((feedMatch) => (
                <button
                  className={activeMatchId === feedMatch.id ? "match-card active" : "match-card"}
                  key={feedMatch.id}
                  onClick={() => selectMatch(feedMatch.id)}
                  type="button"
                >
                  <div className="match-card-meta">
                    <span className={`status-dot ${feedMatch.status}`}>{statusLabels[feedMatch.status]}</span>
                    <small>{formatMatchTime(feedMatch.starts_at)}</small>
                  </div>
                  <strong>{feedMatch.name}</strong>
                  <span className="match-score">{feedMatch.score}</span>
                  <small className="venue-line">{feedMatch.venue}</small>
                </button>
              ))}
            </div>
          </section>

          <section className="score-panel">
            <div className="score-panel-top">
              <div className="teams-line">
                <span>{match?.batting_team.team_short ?? "BAT"}</span>
                <span>vs</span>
                <span>{match?.bowling_team.team_short ?? "BOWL"}</span>
              </div>
              <span className={`status-dot ${activeFeedMatch?.status ?? "live"}`}>
                {statusLabels[activeFeedMatch?.status ?? "live"]}
              </span>
            </div>
            <div className="score-block">
              <div className="score">{scoreLine}</div>
              <p>
                {match
                  ? `${match.batting_team.team_name} after ${match.batting_team.overs_played} overs`
                  : "Waiting for backend data"}
              </p>
            </div>

            <div className="pressure-band">
              <div>
                <span className="label">Chase pressure</span>
                <strong>{match ? `${Math.round(runRatePressure)}%` : "--"}</strong>
              </div>
              <div className="pressure-track">
                <span style={{ width: `${runRatePressure}%` }} />
              </div>
            </div>

            <div className="metrics-row">
              <div>
                <span>Run rate</span>
                <strong>{match?.batting_team.run_rate.toFixed(2) ?? "--"}</strong>
              </div>
              <div>
                <span>Required</span>
                <strong>{match?.required_run_rate.toFixed(2) ?? "--"}</strong>
              </div>
              <div>
                <span>Bowler economy</span>
                <strong>{match?.current_bowler.economy.toFixed(2) ?? "--"}</strong>
              </div>
            </div>
          </section>

          <section className="player-panel">
            <div className="panel-heading">
              <div>
                <span className="label">Player matchup</span>
                <h2>Crease view</h2>
              </div>
              <span>{lastUpdated ? lastUpdated.toLocaleTimeString("en-IN", { hour: "numeric", minute: "2-digit" }) : "--"}</span>
            </div>
            <div>
              <span className="label">On strike</span>
              <h2>{match?.current_batsman.name ?? "Loading batter"}</h2>
              <p>
                {match
                  ? `${match.current_batsman.runs} from ${match.current_batsman.balls_faced}, SR ${match.current_batsman.strike_rate}`
                  : "Live player card will appear here."}
              </p>
            </div>
            <div>
              <span className="label">Into the attack</span>
              <h2>{match?.current_bowler.name ?? "Loading bowler"}</h2>
              <p>
                {match
                  ? `${match.current_bowler.overs_bowled} overs, ${match.current_bowler.runs_given} runs, ${match.current_bowler.wickets_taken} wickets`
                  : "Bowling card will appear here."}
              </p>
            </div>
          </section>

          <section className="analysis-panel">
            <div className="panel-heading">
              <div>
                <span className="label">AI desk</span>
                <h2>{views.find((view) => view.key === activeView)?.label}</h2>
              </div>
              <span>{loading ? "syncing" : "ready"}</span>
            </div>
            <div className="view-tabs" role="tablist" aria-label="Analysis views">
              {views.map((view) => (
                <button
                  key={view.key}
                  className={activeView === view.key ? "active" : ""}
                  onClick={() => setActiveView(view.key)}
                  aria-selected={activeView === view.key}
                  role="tab"
                  type="button"
                >
                  {view.label}
                </button>
              ))}
            </div>

            <div className="analysis-stack">
              {loading && sections.length === 0 ? (
                <>
                  <article className="analysis-note skeleton-note" />
                  <article className="analysis-note skeleton-note" />
                  <article className="analysis-note skeleton-note" />
                </>
              ) : (
                sections.map(([title, value]) => (
                  <article className="analysis-note" key={title}>
                    <span>{title}</span>
                    <p>{textFrom(value)}</p>
                  </article>
                ))
              )}
            </div>
          </section>
        </div>
      </section>
    </main>
  );
}
