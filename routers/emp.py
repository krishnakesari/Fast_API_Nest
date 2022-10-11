from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from database import get_session
from schemas import Emp, EmpOutput

router = APIRouter(prefix="/api/employees")


@router.get("/")
def get_cars(
        # EMPLOYEE_NAME: str | None = None,
        # ORGANIZATION: str | None = None,
        session: Session = Depends(get_session)) -> list:
    query = select(Emp)
    # if EMPLOYEE_NAME:
    #     query = query.where(Emp.EMPLOYEE_NAME == EMPLOYEE_NAME)
    # if ORGANIZATION:
    #     query = query.where(Emp.EMPLOYEE_NUMBER == ORGANIZATION)
    return session.exec(query).all()


@router.get("/{EMPLOYEE_NUMBER}", response_model=EmpOutput)
def Emp_by_id(EMPLOYEE_NUMBER: int, session: Session = Depends(get_session)) -> Emp:
    emp = session.get(Emp, EMPLOYEE_NUMBER)
    if not emp:
        raise HTTPException(status_code=404, detail=f"No employee with id={EMPLOYEE_NUMBER}.")
    return emp
