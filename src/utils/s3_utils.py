import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

"""
For Synchronous Events
"""


class S3Events:

    # s3 details
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    S3_Bucket = os.getenv("S3_Bucket")

    if (
        not AWS_ACCESS_KEY_ID
        or not AWS_SECRET_ACCESS_KEY
        or not AWS_REGION
        or not S3_Bucket
    ):
        raise Exception("AWS Credentials not set")

    @classmethod
    def upload_file_obj(cls, file_Object=None, key=None, extension=None):
        """Upload a file to an S3 bucket
        :param key:
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if key is None:
            return False

        # Upload the file
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=cls.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=cls.AWS_SECRET_ACCESS_KEY,
        )

        try:
            s3_client.upload_file(file_Object.name, cls.S3_Bucket, key)

        except ClientError:
            return False
        return True

    @classmethod
    def process_and_upload(cls, subdir, file, file_path):

        # Process and upload file
        file_name = os.path.basename(file_path)
        ext = file_name.split(".")[1]
        uploads_to_bucket = cls.upload_file_obj(
            key=subdir + file_name, file_Object=file, extension=ext
        )

        if uploads_to_bucket:
            s3_url = f"https://{cls.S3_Bucket}.s3.amazonaws.com/{subdir}{file_name}"
            return s3_url
        return False

    @classmethod
    def delete_file_object(cls, key):

        # delete the file
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=cls.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=cls.AWS_SECRET_ACCESS_KEY,
        )
        response = s3_client.delete_file_object(Bucket=cls.S3_Bucket, Key=key)

        if response["ResponseMetadata"]["HTTPStatusCode"] == 204:
            return True
        return False
