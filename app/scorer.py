import logging
from typing import Dict, List
from .config import RATING_THRESHOLDS

def compute_rating(evidences: Dict[str, List[str]]) -> str:

    logging.info("Computing rating...")
    count_criteria_with_evidence = sum(1 for items in evidences.values() if len(items) > 0)

    high_threshold = RATING_THRESHOLDS["HIGH"]
    medium_threshold = RATING_THRESHOLDS["MEDIUM"]

    if count_criteria_with_evidence >= high_threshold:
        return "high"
    elif count_criteria_with_evidence >= medium_threshold:
        return "medium"
    else:
        return "low"
