# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 10:57:15 2025

@author: joseph
"""
def calculate_leaf_area(leaf_px, ref_px, ref_diameter_cm):
    ref_radius_cm = ref_diameter_cm / 2
    ref_area_cm2 = 3.1416 * (ref_radius_cm ** 2)
    cm2_per_px = ref_area_cm2 / ref_px
    return leaf_px * cm2_per_px

