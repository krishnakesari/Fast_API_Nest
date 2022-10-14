from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

class PerformanceInput(SQLModel):
    id: int
    start: str
    End: str


class PerformanceOutput(PerformanceInput):
    id: int


class Performance(PerformanceInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    start: str = Field(foreign_key="emp.EMPLOYEE_NUMBER")
    emp: "Emp" = Relationship(back_populates="performances")


class Emp_Input(SQLModel):
    EMPLOYEE_NAME: Optional[str] = Field(index=True)
    ORGANIZATION: Optional[str]
    ORGANIZATION: Optional[str]
    SALARY: Optional[float] = Field(default=None, index=True)

    class Config:
        schema_extra = {
            "example": {
                "EMPLOYEE_NAME": "ABC",
                "ORGANIZATION": "DEF",
                "ORGANIZATION": "XYZ",
                "SALARY": 20.4
            }
        }


class Emp(Emp_Input, table=True):
    EMPLOYEE_NUMBER: Optional[int] | None = Field(primary_key=True, default=None)
    performances: list[Performance] = Relationship(back_populates="emp")


class EmpOutput(Emp_Input):
    EMPLOYEE_NUMBER: Optional[int]
    performances: list[PerformanceOutput] = []
