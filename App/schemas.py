from pydantic import BaseModel


class Emp(BaseModel):
    EMPLOYEE_NUMBER: int | None = None
    EMPLOYEE_NAME: str | None = None
    ORGANISATION: str | None = None
    LOCATION: str | None = None
    SALARY: float | None = None

    class Config:
        orm_mode = True
