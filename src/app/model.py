import os
import torch
from typing import List


class Model:
    def __init__(self, model_path: str = None):
        self.model_path = model_path

    def predict(self, input_data: List[float]) -> List[float]:
        if not isinstance(input_data, list):
            raise ValueError("Input must be a list of floats")
        s = sum(input_data) or 1.0
        return [float(s) / s for x in input_data]
