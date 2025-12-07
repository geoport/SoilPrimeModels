from typing import Optional

from pydantic import BaseModel


class ProjectData(BaseModel):
    city: Optional[str] = ""
    county: Optional[str] = ""
    neighborhood: Optional[str] = ""
    pafta: Optional[str] = ""
    ada: Optional[str] = ""
    parsel: Optional[str] = ""
    reporter: Optional[str] = ""
    report_date: Optional[str] = ""
    geology_engineer: Optional[str] = ""
    geophysic_engineer: Optional[str] = ""
    architect: Optional[str] = ""
    static_project_owner: Optional[str] = ""
    contractor: Optional[str] = ""
    project_name: Optional[str] = ""
    owner: Optional[str] = ""
    report_footer: Optional[str] = ""
