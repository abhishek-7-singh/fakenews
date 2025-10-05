# FakeNewsDetection

This repository contains a small full-stack project for detecting fake news. It includes a Python Flask backend with ML model code and a React frontend.

## Repository structure

- backend/ - Flask backend, model training, and utilities
  - abhishek_flask.py, app.py - Flask app entrypoints
  - model.py, train_model.py - model code and training script
  - vectorizer.pkl, model.pkl - (removed from repository due to size; see note below)
  - cleaned - cleaned.csv, fake.csv - (removed from repository due to size)
- frontend/ - React frontend (create-react-app style)

## Important note about large files

Large binary and dataset files (for example `backend/vectorizer.pkl`, `backend/model.pkl`, and the CSV datasets) were removed from the repository history because they exceed GitHub file-size limits and would bloat the repo. If you need to work with trained models or datasets, either:

- Train the model locally by running `train_model.py` (recommended), or
- Store the binary files in a release, external storage, or use Git LFS and ask the repo owner to re-add them via LFS.

If you want to track large model files in this repo, enable Git LFS and migrate the large files to LFS. See the `Git LFS` section below.

## Setup (backend)

1. Create and activate a Python virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r backend/requirements.txt
```

3. Run the Flask app (example):

```powershell
cd backend
python app.py
```

By default the Flask app will serve the API used by the frontend.

## Setup (frontend)

1. Install dependencies and run the dev server (in a separate terminal):

```powershell
cd frontend
npm install
npm start
```

The React app runs on a different port (usually 3000) and communicates with the backend API.

## Training the model

If you need to recreate the model files, run the training script in the backend:

```powershell
cd backend
python train_model.py
```

This will create the `model.pkl` and `vectorizer.pkl` locally in `backend/` (not checked into git by default).

## Git LFS (optional)

If you prefer to keep model binaries in the repo, use Git LFS:

```powershell
# Install git-lfs from https://git-lfs.github.com/ and enable it for the repo
git lfs install
# Track specific file types
git lfs track "backend/*.pkl"
# Commit the .gitattributes file created by git lfs track
git add .gitattributes
git commit -m "Track model files with Git LFS"
```

After enabling LFS, re-add your large files and push. Note: migrating existing history to LFS involves rewriting history and careful coordination with collaborators.

## Development tips

- Add new models and datasets to `.gitignore` before committing.
- Use environment variables for API URLs and secrets; do not commit `.env` files.

## Contributing

1. Fork the repo
2. Create a branch
3. Make changes and run tests (if any)
4. Open a PR with a clear description

## Contact / License

This repo is a demonstration project. Check the repo owner for licensing and collaboration preferences.
