from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class FieldData(BaseModel):
    parsel_area: Optional[str] = ""
    land_slope: Optional[str] = ""
    field_coordinates: Optional[List[Dict[str, str]]] = Field(default_factory=list)
    north_parsel_info: Optional[str] = ""
    south_parsel_info: Optional[str] = ""
    east_parsel_info: Optional[str] = ""
    west_parsel_info: Optional[str] = ""
    north_structural_info: Optional[str] = ""
    south_structural_info: Optional[str] = ""
    east_structural_info: Optional[str] = ""
    west_structural_info: Optional[str] = ""
