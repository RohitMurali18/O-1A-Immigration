import os
from typing import Dict, List


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
PORT = int(os.getenv("PORT", 8000))



CRITERIA_KEYWORDS: Dict[str, List[str]] = {
    "Awards": ["award", "honor", "prize", "medal", "recognition"],
    "Membership": ["member", "membership", "board", "committee"],
    "Press": ["press", "article", "media", "featured", "interview"],
    "Judging": ["judge", "judged", "panel", "jury", "evaluation"],
    "Original Contribution": ["invented", "created", "contributed", "patent", "discovery"],
    "Scholarly Articles": ["publication", "journal", "scholarly", "conference", "paper"],
    "Critical Employment": ["critical role", "lead role", "executive", "founder", "chief"],
    "High Remuneration": ["salary", "compensation", "remuneration", "high pay"]
}



RATING_THRESHOLDS = {
    "HIGH": 6,
    "MEDIUM": 3
}
