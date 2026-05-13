param(
    [switch]$Install
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Backend = Join-Path $Root "backend"
$Frontend = Join-Path $Root "fieldvision-ai\frontend"
$VenvPython = Join-Path $Backend "venv\Scripts\python.exe"
$VenvActivate = Join-Path $Backend "venv\Scripts\Activate.ps1"

if (!(Test-Path $VenvPython)) {
    Push-Location $Backend
    python -m venv venv
    Pop-Location
}

if ($Install) {
    Push-Location $Backend
    & $VenvPython -m pip install -r requirements.txt
    Pop-Location

    Push-Location $Frontend
    npm install
    Pop-Location
}

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "cd `"$Backend`"; . `"$VenvActivate`"; python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"
)

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "cd `"$Frontend`"; npm run dev"
)

Write-Host "FieldVision AI is starting locally."
Write-Host "Frontend: http://localhost:3000"
Write-Host "Backend:  http://127.0.0.1:8000"
Write-Host "Docs:     http://127.0.0.1:8000/docs"
