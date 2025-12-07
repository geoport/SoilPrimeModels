from pydantic import BaseModel


class EffectiveDepthResults(BaseModel):
    qmax: float
    depth_by_dimension: float
    depth_by_pressure: float
    selected_depth: float
