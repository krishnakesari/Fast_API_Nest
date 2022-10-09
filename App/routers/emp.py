from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from ..database import get_session
from ..schemas import Emp

router = APIRouter(prefix="/api/emp")

@router.get("/")
def get_cars(size: str | None = None, doors: int | None = None,
             session: Session = Depends(get_session)) -> list:
    query = select(Car)
    if size:
        query = query.where(Car.size == size)
    if doors:
        query = query.where(Car.doors >= doors)
    return session.exec(query).all()

@router.get("/{id}", response_model=CarOutput)
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    car = session.get(Car, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")