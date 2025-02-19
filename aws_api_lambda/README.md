# AWS Lambda + FastAPI Example

This folder demonstrates a simple **FastAPI** app adapted for **AWS Lambda** using **Mangum**.

## Files
- **main.py**: Contains the FastAPI application code and Mangum adapter (`handler`).
- **requirements.txt**: Dependencies for our project (`fastapi`, `mangum`, `uvicorn`).

## Local Testing
You can test this FastAPI app locally:

```bash
# 1. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run locally
uvicorn main:app --reload
