# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 10:56:28 2025

@author: joseph
"""
import cv2
import numpy as np
from PIL import Image

def segment_leaf(image_path):
    image = cv2.imread(image_path)

    # Convert to HSV for color filtering
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define green range for the leaf
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])
    leaf_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Define gray/silver range for the coin
    lower_coin = np.array([0, 0, 120])
    upper_coin = np.array([180, 50, 255])
    coin_mask = cv2.inRange(hsv, lower_coin, upper_coin)

    # Find contours for leaf and coin
    contours_leaf, _ = cv2.findContours(leaf_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_coin, _ = cv2.findContours(coin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours_leaf or not contours_coin:
        raise ValueError("Could not detect both leaf and coin!")

    leaf_contour = max(contours_leaf, key=cv2.contourArea)
    coin_contour = max(contours_coin, key=cv2.contourArea)

    leaf_area_px = cv2.contourArea(leaf_contour)
    ref_area_px = cv2.contourArea(coin_contour)

    # Create segmented mask for visualization
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [leaf_contour], -1, 255, -1)
    segmented = cv2.bitwise_and(image, image, mask=mask)
    segmented_rgb = cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)

    return Image.fromarray(segmented_rgb), ref_area_px, leaf_area_px
