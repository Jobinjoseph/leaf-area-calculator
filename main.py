# -*- coding: utf-8 -*-
"""
@author: joseph
"""
# main.py
from image_processing.leaf_segmenter import segment_leaf
from image_processing.area_calculator import calculate_leaf_area
from aws.s3_handler import upload_to_s3
from aws.dynamodb_logger import log_to_dynamodb
from utils.uuid_gen import generate_uuid
import os
from datetime import datetime


def process_leaf_image(image_path, reference_object_diameter_cm):
    print("[INFO] Starting leaf image processing...")

    segmented_image, ref_area_px, leaf_area_px = segment_leaf(image_path)
    leaf_area_cm2 = calculate_leaf_area(leaf_area_px, ref_area_px, reference_object_diameter_cm)

    print(f"[INFO] Calculated leaf area: {leaf_area_cm2:.2f} cm^2")

    leaf_id = generate_uuid()
    timestamp = datetime.utcnow().isoformat()

    # Save segmented image
    output_path = f"output/{leaf_id}_segmented.jpg"
    os.makedirs("output", exist_ok=True)
    segmented_image.save(output_path)

    # Upload to S3
    s3_key = upload_to_s3(output_path, leaf_id)
    # s3_key = "test/mock_key.jpg"

    # Log to DynamoDB
    log_to_dynamodb(leaf_id, timestamp, leaf_area_cm2, s3_key)

    print("[INFO] Processing complete.")


if __name__ == "__main__":
    test_image = "examples/leaf1.jpg"
    reference_object_diameter_cm = 2.4  # coin size in cm
    process_leaf_image(test_image, reference_object_diameter_cm)

