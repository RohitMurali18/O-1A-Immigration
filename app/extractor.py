import logging
from typing import Dict, List
from .config import CRITERIA_KEYWORDS

def extract_evidences(cv_text: str) -> Dict[str, List[str]]:
 
    logging.info("Extracting evidences from text...")
    evidences = {criterion: [] for criterion in CRITERIA_KEYWORDS.keys()}

    lines = cv_text.split("\n")
    for line in lines:
        lower_line = line.lower()
        for criterion, keywords in CRITERIA_KEYWORDS.items():
            for kw in keywords:
                if kw in lower_line:
                    # If we find a match, store the original line.
                    evidences[criterion].append(line.strip())
                    break  # Move on to the next line once one keyword matches

    return evidences
