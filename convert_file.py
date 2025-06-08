import boto3, os, pypandoc, typing, json, utils
from mypy_boto3_s3 import S3Client
from dotenv import load_dotenv
from pathlib import Path

load_dotenv() # remove when uploading to lambda

s3: S3Client = boto3.client("s3")
BUCKET_NAME: str = os.environ.get("BUCKET_NAME")

if not BUCKET_NAME:
    raise RuntimeError("BUCKET_NAME is not set in the environment.")

for item in Path(".").iterdir():
    if item.is_file() and item.suffix.lower() in utils.EXTENSION_TO_FORMAT.keys():
        utils.convert_file(item, "pdf")