from typing import Optional

from pydantic import BaseModel


class Building(BaseModel):
    building_type: Optional[str] = ""
    building_usage_class: Optional[str] = ""
    building_importance_factor: Optional[str] = ""
    building_height_class: Optional[str] = ""
    basement_floor_number: Optional[str] = ""
    total_floor_number: Optional[str] = ""
    construction_area: Optional[str] = ""
    building_height: Optional[str] = ""
    structural_system: Optional[str] = ""
