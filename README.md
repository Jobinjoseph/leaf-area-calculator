# README.md

## Leaf Area Calculator (SLAC)

This project calculates the **leaf area from a photograph** using computer vision and uploads results to **AWS**. It requires:

- Python (modular structure)
- OpenCV (image segmentation)
- TensorFlow (optional classification)
- AWS EC2 (deployment), S3 (image storage), DynamoDB (metadata logging)

---

### Project Structure
```
leaf_area_calculator/
├── main.py                         # Main orchestrator
├── image_processing/
│   ├── leaf_segmenter.py          # OpenCV-based segmentation
│   └── area_calculator.py         # Area computation using reference object
├── aws/
│   ├── s3_handler.py              # Uploads image to S3
│   └── dynamodb_logger.py         # Logs leaf info to DynamoDB
├── utils/
│   └── uuid_gen.py                # Generates UUIDs
├── examples/                      # Sample input image(s)
├── output/                        # Segmented output images
└── README.md                      # This file
```

---

### Getting Started

#### 1. Clone the Repository
```bash
git clone https://github.com/jobinjoseph/leaf-area-calculator.git
cd leaf-area-calculator
```

#### 2. Install Requirements
```bash
pip install -r requirements.txt
```

#### 3. Configure AWS Credentials
Make sure EC2 instance or local environment is configured with an IAM role or credentials with access to:
- Amazon S3
- Amazon DynamoDB

configure via:
```bash
aws configure
```

---

### Usage Example
```python
python main.py
```
Edit `main.py` to change the input image or reference object size (e.g., coin = 2.4 cm diameter).

---

### How It Works
1. **Segment Leaf and Reference**: OpenCV detects contours in the image.
2. **Compute Area**: Calculates leaf area using pixel ratio to a known object.
3. **Save and Upload**: Result is saved and pushed to AWS S3.
4. **Log**: DynamoDB logs the leaf ID, timestamp, area, and image key.

---

### Example DynamoDB Entry
```json
{
  "leaf_id": "b9fa0f80-65ac-4bda-a26c-fc0bd7a1b04b",
  "timestamp": "2025-06-16T14:20:10Z",
  "area_cm2": 35.72,
  "s3_key": "leaf_images/b9fa0f80-65ac-4bda-a26c-fc0bd7a1b04b.jpg"
}
```

---

### To Do / Optional Extensions
- Add TensorFlow classifier to identify leaf species
- Create a Streamlit or Flask UI
- Add SNS notifications or webhooks

---

### License
MIT License – feel free to fork and adapt.
