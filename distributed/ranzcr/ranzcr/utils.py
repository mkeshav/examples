import os

import torch
import torch.distributed as dist

from sklearn.metrics import roc_auc_score


WORLD_SIZE = int(os.environ.get('WORLD_SIZE', 1))


def should_distribute() -> bool:
    return dist.is_available() and WORLD_SIZE > 1


def is_distributed() -> bool:
    return dist.is_available() and dist.is_initialized()


def get_score(labels: torch.Tensor, predictions: torch.Tensor) -> float:
    """Calculates the AUC score for each binary target variable.

    Args:
        labels: the ground truth
        predictions: the predictions
    Returns:
        score: the AUC score
    """
    score = roc_auc_score(labels.reshape(-1), predictions.reshape(-1))
    return score