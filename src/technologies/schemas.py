from uuid import UUID

from pydantic import BaseModel, Field
from enum import Enum


class TechLevel(str, Enum):
    Hold = "Hold"
    Assess = "Assess"
    Trial = "Trial"
    Adopt = "Adopt"


class TechGroups(str, Enum):
    Languages_and_frameworks = "Languages and frameworks"
    Data_management = "Data management"
    Tools = "Tools"
    Platforms_and_infrastructure = "Platforms and infrastructure"


class TechnologiesSchema(BaseModel):
    label: str
    level: TechLevel
    using_num: int = Field(le=3, ge=1)
    group: TechGroups
    description: str


class TechnologiesModelSchema(BaseModel):
    label: str
    x: int
    y: int
    group: str
    level: str
    description: str


class TechnologiesUpdateSchema(BaseModel):
    id: UUID
    data: TechnologiesModelSchema
