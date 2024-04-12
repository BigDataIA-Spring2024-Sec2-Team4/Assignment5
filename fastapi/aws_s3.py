from fastapi import FastAPI, HTTPException
import boto3
from botocore.exceptions import ClientError
import pandas as pd
from io import StringIO
from typing import List, Dict
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Define the mapping of dropdown options to bucket names
BUCKET_MAPPING = {
    "Big Data Projects": "bigdataprojects1",
    "Backtesting & Simulation": "backtesting2",
    "Branded Image Link Added to Refresher Reading": "brandedimage"
}

# Function to fetch markdown files from AWS S3 bucket
def fetch_markdown(bucket_name: str) -> List[Dict[str, str]]:
    try:
        # Initialize S3 client
        s3 = boto3.client('s3',
                          aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                          aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
        
        # Get all objects in the bucket with .md extension
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix='', Delimiter='.md')

        # Fetch contents of .md files and concatenate them into a single string
        combined_content = ""
        for obj in response.get('Contents', []):
            key = obj['Key']
            if key.endswith('.md'):
                file_content = s3.get_object(Bucket=bucket_name, Key=key)['Body'].read().decode('utf-8')
                combined_content += file_content + "\n"

        return combined_content

        # # Convert combined content to a list of dictionaries
        # df = pd.read_csv(StringIO(combined_content), delimiter="\n", header=None, names=["Content"])
        # data = df.to_dict(orient="records")
        # return data

    except ClientError as e:
        # Raise HTTPException if there's an error fetching data from S3
        raise HTTPException(status_code=500, detail=f"Error fetching markdown files: {str(e)}")

# Route to fetch markdown files for a specific bucket and return as list of dictionaries
@app.get("/markdown/{option}", response_model=List[Dict[str, str]])
def get_markdown(option: str) -> List[Dict[str, str]]:
    bucket_name = BUCKET_MAPPING.get(option)
    if not bucket_name:
        raise HTTPException(status_code=404, detail=f"Bucket name not found for option: {option}")
    
    # Fetch markdown files from S3 bucket and return as list of dictionaries
    data = fetch_markdown(bucket_name)
    return data
