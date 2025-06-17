# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 10:57:46 2025

@author: joseph
"""
import boto3

def upload_to_s3(file_path, leaf_id):
    s3 = boto3.client('s3')
    bucket = 'your-s3-bucket-name'  # Replace with your actual bucket name
    s3_key = f"leaf_images/{leaf_id}.jpg"
    s3.upload_file(file_path, bucket, s3_key)
    return s3_key

