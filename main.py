import os
import pandas as pd
import polars as pl

import kaggle_evaluation.default_inference_server

def predict (test: pl.DataFrame) -> float:

    return 0.0

inference_server = kaggle_evaluation.default_inference_server.DefaultInferenceServer(predict)

if os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    inference_server.serve()
else:
    inference_server.run_local_gateway(('/kaggle/input/hull-tactical-market-prediction/',))