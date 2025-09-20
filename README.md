# Hull Tactical Market Prediction Competition

This repository contains my submission for the Hull Tactical Market Prediction competition on Kaggle.

## Overview

The Hull Tactical Market Prediction competition challenges participants to predict market movements using various financial indicators and data sources. This submission implements a machine learning approach to forecast market behavior.

## Project Structure

```
├── main.py              # Main submission file with prediction function
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore patterns
```

## Setup

1. Clone this repository:
```bash
git clone <your-repo-url>
cd hull-tactical-competition
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The main prediction logic is implemented in `main.py`. The script:
- Defines a `predict()` function that takes a Polars DataFrame and returns a float prediction
- Uses the Kaggle evaluation inference server for submission
- Can run locally or in the competition environment

### Local Testing
```bash
python main.py
```

### Competition Submission
The script automatically detects when running in the Kaggle competition environment and serves the model accordingly.

## Model Approach

Currently implements a baseline approach returning 0.0. This should be replaced with your actual prediction logic.

## Dependencies

- pandas: Data manipulation and analysis
- polars: Fast DataFrame library
- kaggle-evaluation: Kaggle competition evaluation tools

## Development

To improve the model:
1. Replace the placeholder logic in the `predict()` function
2. Add feature engineering and data preprocessing
3. Implement your chosen machine learning algorithm
4. Test locally before submission

## Competition Details

- **Competition**: Hull Tactical Market Prediction
- **Platform**: Kaggle
- **Objective**: Predict market movements with high accuracy

## License

This project is for competition purposes only.
