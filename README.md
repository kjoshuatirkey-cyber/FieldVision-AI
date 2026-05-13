# FieldVision AI

Production-ready MVP for an AI cricket command center.

## Local Development

Quick start:

```powershell
.\scripts\start-local.ps1 -Install
```

After dependencies are installed once, use:

```powershell
.\scripts\start-local.ps1
```

### Backend

```powershell
cd "C:\Users\kjosh\OneDrive\Desktop\FieldVision AI\backend"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Backend URLs:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
```

### Frontend

```powershell
cd "C:\Users\kjosh\OneDrive\Desktop\FieldVision AI\fieldvision-ai\frontend"
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

## Environment

Create local env files from the examples:

```powershell
Copy-Item backend\.env.example backend\.env
Copy-Item fieldvision-ai\frontend\.env.example fieldvision-ai\frontend\.env.local
```

Set `GEMINI_API_KEY` in `backend\.env`.

The frontend uses `NEXT_PUBLIC_API_URL` to call the backend. Locally it should be:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Production Deploy

### Backend on Render

Use the root `render.yaml` blueprint or deploy the `backend` folder directly.

Required Render environment variables:

```text
GEMINI_API_KEY=your_real_key
ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app
ENVIRONMENT=production
GEMINI_MODEL=gemini-1.5-flash-latest
```

Health check:

```text
/health
```

### Frontend on Vercel

Deploy `fieldvision-ai/frontend`.

Required Vercel environment variable:

```text
NEXT_PUBLIC_API_URL=https://your-render-backend.onrender.com
```

Build command:

```text
npm run build
```

## Verification

Backend:

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Frontend:

```powershell
cd fieldvision-ai\frontend
npm run check
```

Security note: never commit `backend\.env` or any real Gemini API key.
