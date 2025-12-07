from typing import List, Optional

from pydantic import BaseModel


class Settlement(BaseModel):
    """Represents the consolidation settlement calculation result."""

    settlement_per_layer: List[float]  # Settlement for each layer in cm
    total_settlement: float  # Total settlement in cm
    qnet: float  # Net foundation pressure in t/m²


class SettlementResults(BaseModel):
    foundation_pressure: float
    total_settlements: List[float]
    total_settlement: float
    elastic_settlement: Optional[Settlement]
    consolidation_settlement: Optional[Settlement]
    allowable_settlement: float
    is_safe: bool
