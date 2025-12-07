from typing import List, Optional

from pydantic import BaseModel


class LabExperiment(BaseModel):
    no: Optional[str] = ""
    depth: Optional[str] = ""
    water_content: Optional[str] = ""
    fine_content: Optional[str] = ""
    liquid_limit: Optional[str] = ""
    plastic_limit: Optional[str] = ""
    plasticity_index: Optional[str] = ""
    natural_unit_weight: Optional[str] = ""
    cohesion: Optional[str] = ""
    friction_angle: Optional[str] = ""
    soil_class: Optional[str] = ""


class LabExperiments(BaseModel):
    exps: List[LabExperiment]
