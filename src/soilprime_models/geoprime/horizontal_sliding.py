from pydantic import BaseModel


class HorizontalSlidingResult(BaseModel):
    """Result of horizontal sliding calculations."""

    rth: float  # Resistance from friction/cohesion
    ptv: float  # Total vertical pressure
    rpk_x: float  # Passive resistance in x direction
    rpk_y: float  # Passive resistance in y direction
    rpt_x: float  # Reduced passive resistance in x direction
    rpt_y: float  # Reduced passive resistance in y direction
    sum_x: float  # Total resistance in x direction
    sum_y: float  # Total resistance in y direction
    is_safe_x: bool  # Safety check in x direction
    is_safe_y: bool  # Safety check in y direction
    ac: float  # Foundation area
    vth_x: float  # Horizontal load in x direction
    vth_y: float  # Horizontal load in y direction
