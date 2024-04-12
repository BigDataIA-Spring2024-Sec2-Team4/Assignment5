from fastapi import FastAPI, HTTPException, Response
from typing import Optional
import boto3

# Initialize FastAPI app
app = FastAPI()

# Define AWS S3 bucket names and file names
BUCKET_MAPPING = {
    "Set A": "bucket_setA",
    "Set B": "bucket_setB"
}
FILE_MAPPING = {
    "Set A": "setA.csv",
    "Set B": "setB.csv"
}

# Function to fetch CSV file from AWS S3 bucket
def fetch_csv(bucket_name: str, file_name: str) -> Optional[str]:
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching file from S3: {str(e)}")

# Route to fetch CSV file for a specific bucket
@app.get("/csv/{option}", response_class=Response)
def get_csv(option: str) -> Optional[str]:
    bucket_name = BUCKET_MAPPING.get(option)
    file_name = FILE_MAPPING.get(option)
    if not bucket_name or not file_name:
        raise HTTPException(status_code=404, detail=f"Bucket or file not found for option: {option}")
    
    csv_content = fetch_csv(bucket_name, file_name)
    if csv_content:
        return Response(content=csv_content, media_type="text/csv")
    else:
        raise HTTPException(status_code=404, detail=f"CSV file not found for option: {option}")
