# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 10:58:21 2025

@author: joseph
"""
import boto3

def log_to_dynamodb(leaf_id, timestamp, area_cm2, s3_key):
    db = boto3.resource('dynamodb')
    table = db.Table('LeafAreaLogs')  # Replace with your actual table name
    table.put_item(Item={
        'leaf_id': leaf_id,
        'timestamp': timestamp,
        'area_cm2': area_cm2,
        's3_key': s3_key
    })

