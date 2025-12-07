from typing import Optional

from pydantic import BaseModel


class BearingCapacityFactors(BaseModel):
    """Bearing capacity factors according to Terzaghi, Meyerhof, Hansen, etc."""

    nc: float
    nq: float
    ng: float  # sometimes denoted as Nγ


class ShapeFactors(BaseModel):
    """Shape modification factors used in bearing capacity equations."""

    sc: float
    sq: float
    sg: float


class InclinationFactors(BaseModel):
    """Inclination modification factors for inclined load conditions."""

    ic: float
    iq: float
    ig: float


class BaseFactors(BaseModel):
    """Base inclination factors depending on foundation base angle."""

    bc: float
    bq: float
    bg: float


class GroundFactors(BaseModel):
    """Ground slope modification factors affecting bearing capacity."""

    gc: float
    gq: float
    gg: float


class DepthFactors(BaseModel):
    """Depth modification factors for accounting foundation embedment."""

    dc: float
    dq: float
    dg: float


class SoilParams(BaseModel):
    """Soil parameters used in bearing capacity calculations."""

    friction_angle: float
    cohesion: float
    unit_weight: float


class BearingCapacityResult(BaseModel):
    """Result of bearing capacity calculation."""

    bearing_capacity_factors: BearingCapacityFactors
    shape_factors: ShapeFactors
    depth_factors: DepthFactors
    load_inclination_factors: InclinationFactors
    ground_factors: GroundFactors
    base_factors: BaseFactors
    soil_params: SoilParams
    ultimate_bearing_capacity: float
    allowable_bearing_capacity: float
    is_safe: bool
    qmax: float


class PointLoadTest(BaseModel):
    """Represents the bearing capacity result for a given soil and foundation setup."""

    is50: float  # Is50 value in MPa
    ucs: float  # Uniaxial compressive strength (UCS) in MPa
    c: float  # Generalized value of C
    d: float  # Equivalent core diameter in mm
    allowable_bearing_capacity: float  # Allowable bearing capacity in ton/m2
    qmax: float  # The pressure exerted by the foundation in ton/m2
    df: float  # Indicates the depth at which the bearing capacity is calculated in meters
    is_safe: bool  # Indicates whether the bearing capacity is safe
    safety_factor: float  # Safety factor used in the design


class TezcanOzdemir(BaseModel):
    """Represents the bearing capacity result for a given soil and foundation setup."""

    vs: float  # Shear wave velocity (Vs) in m/s
    unit_weight: float  # Unit weight of the soil in t/m³
    qmax: float  # The pressure exerted by the foundation in ton/m2
    allowable_bearing_capacity: float  # Allowable bearing capacity in ton/m2
    is_safe: bool  # Indicates whether the bearing capacity is safe
    safety_factor: float  # Safety factor used in the design


class BearingCapacityResults:
    selected_bc: float
    qmax: float
    by_vesic: Optional[BearingCapacityResults] = None
    by_point_load_test: Optional[PointLoadTest] = None
    by_tezcan_ozdemir: Optional[TezcanOzdemir] = None
    is_safe: bool = False
    long_term_bc: Optional[float] = None
    short_term_bc: Optional[float] = None
