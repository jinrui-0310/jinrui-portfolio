# Jinrui Li Portfolio

A bilingual personal portfolio built with Flask and Plotly for analytics, business intelligence, forecasting, and supply chain roles.

## What's inside

- English home page at `/`
- Chinese home page at `/zh`
- Dedicated project pages with interactive charts
- Resume file bundled at `static/files/Jinrui_Li_Resume.pdf`
- Heroku-ready app entry via `Procfile`

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Then open:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/zh`

## Deploy to Heroku

This repo already includes:

- `Procfile`
- `requirements.txt`
- `runtime.txt`

Typical steps:

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

If needed, scale the web dyno:

```bash
heroku ps:scale web=1
```

## Main files

- `app.py`: Flask routes and portfolio content
- `templates/`: English and Chinese page templates
- `static/css/style.css`: site styling
- `static/js/script.js`: mobile nav, reveal animation, chart rendering
- `static/files/Jinrui_Li_Resume.pdf`: downloadable resume
