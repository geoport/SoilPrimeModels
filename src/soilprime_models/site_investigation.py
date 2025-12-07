from typing import List

from pydantic import BaseModel


class BoreHole(BaseModel):
    depth: float
    number: str


class SiteInvestigation(BaseModel):
    bore_holes: List[BoreHole]
    total_depth: float
    investigation_date_start: str
    investigation_date_end: str
    investigation_category: str
