# ETL Pipeline

This folder contains a simple **Extract-Transform-Load** pipeline in Python:

- **Extract**: Fetch JSON data from a public API
- **Transform**: Convert to a pandas DataFrame, rename columns, drop unneeded columns
- **Load**: Save final data to a local CSV file

## How to Run

1. **Install dependencies** (ideally inside a virtual environment):
   ```bash
   pip install -r requirements.txt
