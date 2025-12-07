from typing import List, Optional

from pydantic import BaseModel


class NLayerData(BaseModel):
    """Data for a single layer in SPT-based soil classification."""

    thickness: float  # Layer thickness (h) in meters
    n: float  # N-value (N60 or N1_60f) in blows/30cm
    h_over_n: float  # H/N ratio


class SptSoilClassificationResult(BaseModel):
    """Result of SPT-based soil classification."""

    layers: List[NLayerData]  # Per-layer N information
    sum_h_over_n: float  # Sum of h/N values across all layers (unit: m / blows)
    n_30: float  # (N)_30 value calculated from the layers
    soil_class: str  # Final local soil class (e.g., ZE, ZD, ZC)


class VsLayerData(BaseModel):
    """Data for a single layer in VS-based soil classification."""

    thickness: float  # Layer thickness (h) in meters
    vs: float  # Shear wave velocity (Vs) in m/s
    h_over_vs: float  # H/Vs ratio


class VsSoilClassificationResult(BaseModel):
    """Result of VS-based soil classification."""

    layers: List[VsLayerData]  # Per-layer Vs information
    sum_h_over_vs: float  # Sum of h/Vs values across all layers (unit: m / (m/s))
    vs_30: float  # (Vs)_30 value calculated from the layers
    soil_class: str  # Final local soil class (e.g., ZE, ZD, ZC, ZB, ZA)


class CuLayerData(BaseModel):
    """Data for a single layer in Cu-based soil classification."""

    thickness: float  # Layer thickness (h) in meters
    cu: float  # Undrained shear strength (Cu) in t/m²
    h_over_cu: float  # H/Cu ratio


class CuSoilClassificationResult(BaseModel):
    """Result of Cu-based soil classification."""

    layers: List[CuLayerData]  # Per-layer Cu information
    sum_h_over_cu: float  # Sum of h/Cu values across all layers (unit: m / (t/m²))
    cu_30: float  # (Cu)_30 value calculated from the layers
    soil_class: str  # Final local soil class (e.g., ZE, ZD, ZC)


class LscResult(BaseModel):
    by_spt: Optional[SptSoilClassificationResult]
    by_vs: Optional[VsSoilClassificationResult]
    by_cu: Optional[CuSoilClassificationResult]
    calculated: str
    selected: str
