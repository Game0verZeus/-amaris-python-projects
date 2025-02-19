import requests
import pandas as pd

def extract_data():
    """
    Extract data from a public JSON API.
    Here we use a placeholder API from JSONPlaceholder (fake posts).
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError if the status != 200
    data = response.json()
    return data  # This is a list of dicts

def transform_data(data):
    """
    Transform the extracted data into a pandas DataFrame,
    and do a simple cleanup or manipulation.
    """
    df = pd.DataFrame(data)
    # For demonstration, let's rename columns or filter out columns
    df.rename(columns={"id": "post_id", "title": "post_title"}, inplace=True)
    # Maybe drop the 'userId' column if we don't need it
    df.drop(columns=["userId"], inplace=True)
    return df

def load_data(df):
    """
    Load the transformed data into a local CSV file.
    """
    df.to_csv("output_data.csv", index=False)
    print("Data successfully loaded into output_data.csv")

def run_etl():
    """ Main function to run the Extract, Transform, Load process """
    print("Starting ETL process...")
    data = extract_data()
    df = transform_data(data)
    load_data(df)
    print("ETL process complete.")

if __name__ == "__main__":
    run_etl()
