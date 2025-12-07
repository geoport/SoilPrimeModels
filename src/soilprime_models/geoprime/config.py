from pydantic import BaseModel


class AnalysisOptions(BaseModel):
    bc_by_vesic: bool = False
    bc_by_vesic_short_term: bool = False
    bc_by_vesic_long_term: bool = False
    bc_by_tezcan_ozdemir: bool = False
    by_by_point_load_test: bool = False
    consolidation_by_mv: bool = False
    consolidation_by_compression_index: bool = False
    elastic_settlement_by_boussinesq: bool = False
    effective_depth: bool = False
    horizontal_sliding: bool = False
    liquefaction_spt_seed_idriss: bool = False
    liquefaction_vs_andrus_stokoe: bool = False
    lsc_by_spt: bool = False
    lsc_by_vs: bool = False
    lsc_by_cu: bool = False
    soil_coefficient_by_bc: bool = False
    soil_coefficient_by_settlement: bool = False
    swelling_potential: bool = False

    settlement: bool = False
    bearing_capacity: bool = False
    liquefaction: bool = False
    local_soil_class: bool = False
    soil_coefficient: bool = False


class PageOptions(BaseModel):
    cover: bool = False
    introduction: bool = False
    construction_field: bool = False
    structural_information: bool = False
    site_investigation: bool = False
    additional_site_investigation: bool = False
    idealized_soil: bool = False
    parameter_selection: bool = False
    seismicity: bool = False
    building_soil_interaction: bool = False
    shallow_foundation: bool = False
    deep_foundation: bool = False
    ground_improvement: bool = False
    foundation_suggestion: bool = False
    retaining_system: bool = False
    results: bool = False
    referances: bool = False
