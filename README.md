# daily-dragon

## Local Development
### Install dependencies for API
```bash
pip install -r requirements.txt
```

### Install dependencies for UI
```bash
npm install
```

### Run tests with coverage
```bash
pytest --cov=.
```

### Run API locally
```bash
uvicorn daily_dragon.daily_dragon_app:app --reload
```

### Run UI locally
```bash
npm run dev
```