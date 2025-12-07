from typing import Optional

from pydantic import BaseModel


class SpectralCoordinates(BaseModel):
    ss: float
    fs: float
    s1: float
    f1: float
    sds: float
    sd1: float
    ta: float
    tb: float
    tad: float
    tbd: float


class Seismicity(BaseModel):
    dyhd: Optional[str] = ""
    pga: Optional[str] = ""
    local_soil_class: Optional[str] = ""
    earthquake_design_class: Optional[str] = ""
    mw: Optional[str] = ""
