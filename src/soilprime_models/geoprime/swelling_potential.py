from typing import List

from pydantic import BaseModel


class SwellingPotentialData(BaseModel):
    """Represents the swelling potential data for a soil layer."""

    layer_center: float  # The center depth of the layer in meters
    effective_stress: float  # The effective stress at the center of the layer in ton/m2
    delta_stress: float  # The change in stress due to the foundation load in ton/m2
    swelling_pressure: float  # The calculated swelling pressure for the layer in ton/m2
    is_safe: bool  # Indicates whether the swelling pressure is safe compared to the effective stress


class SwellingPotentialResult(BaseModel):
    """Represents the result of the swelling potential calculation."""

    data: List[SwellingPotentialData]  # Swelling potential data for each layer
    net_foundation_pressure: float  # The net foundation pressure in ton/m2
    is_safe: bool  # Overall safety status based on swelling pressures
