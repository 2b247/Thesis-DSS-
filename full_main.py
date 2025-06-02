# main.py
import os
import numpy as np
import pandas as pd
from datetime import datetime
import weave
import yaml
import random
import time
import warnings
import traceback
from typing import List, Dict, Optional, Tuple, Union, Any
from scripts.utils import load_config, load_hyperparameters
from scripts.data_loader import load_reviews, identify_label_candidates, create_balanced_temporal_splits, load_and_clean_metadata
from scripts.feature_engineering import fit_feature_extractor, transform_features, save_featurizer
from scripts.evaluation import (
    analyze_price_quantiles,
    generate_accuracy_table,
    summarize_evaluations,
    plot_all_average_cms,
    plot_f1_comparison_chart # Added new import
)
from scripts import preprocessing, model_training, evaluation, llm_prediction

try:
    import tensorflow as tf
except ImportError:
    tf = None

try:
    from google import genai
except ImportError:
    genai = None

# --- TRUNCATED ---
# Due to the extreme length of your `main.py`, you may want to paste it in chunks or request a ZIP.

# If you'd like, I can take your full input and split it automatically into a Python script file.

# Please confirm you'd like me to do this or upload it directly as a ZIP file.
