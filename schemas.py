from sqlmodel import SQLModel, Field
from typing import List, Optional


class Emp_Input(SQLModel):
    EMPLOYEE_NAME: Optional[str] = Field(index=True)
    ORGANIZATION: Optional[str]
    LOCATION: Optional[str]
    SALARY: Optional[float] = Field(default=None, index=True)


class Emp(Emp_Input, table=True):
    EMPLOYEE_NUMBER: Optional[int] | None = Field(primary_key=True, default=None)


class EmpOutput(Emp_Input):
    EMPLOYEE_NUMBER: Optional[int]
