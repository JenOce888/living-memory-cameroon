# Living Memory of Cameroon

**INF232 EC2 — Data collection and descriptive analysis application**

An application to archive oral testimonies, myths/legends/proverbs,
and medicinal plant knowledge collected from Cameroonian elders.

## Features
- Collect historical testimonies (text + audio recording)
- Collect oral histories: myths, legends, proverbs, folktales, traditions
- Collect medicinal plants (description + photo + usage context)
- Store elder profiles with explicit consent tracking
- Descriptive statistics dashboard (charts by region, ethnic group, period, language)
- Search across all records

## Tech stack
- **Backend**: Python + Flask + SQLAlchemy
- **Database**: SQLite (local) / PostgreSQL (production on Render)
- **Media storage**: Cloudinary (audio, photos)
- **Analysis**: Pandas
- **Deployment**: Render.com (free tier)

## Run locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create your environment file
cp .env.example .env
# Edit .env with your Cloudinary credentials

# 3. Start the app
python app.py
# Open http://localhost:5000
```

## Deploy on Render

1. Push this project to a GitHub repository
2. Go to render.com → "New Web Service" → connect your repo
3. Render will detect render.yaml automatically
4. Add your CLOUDINARY_* variables in the Render dashboard (Environment tab)
5. Deploy — Render gives you a public URL to send to your professor
