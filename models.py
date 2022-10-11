from typing import Optional

from sqlmodel import SQLModel, Field


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


class EmpOutput(Emp_Input):
    EMPLOYEE_NUMBER: Optional[int]
