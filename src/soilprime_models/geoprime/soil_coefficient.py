from typing import Optional

from pydantic import BaseModel


class SoilCoefficientResults(BaseModel):
    by_settlement: Optional[float] = None
    by_bc: Optional[float] = None
    selected: Optional[float] = None
