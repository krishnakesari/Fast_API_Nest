from sqlalchemy.orm import Session
from . import models, schemas


def get_items(db: Session):
    return db.query(models.Emp).order_by(models.Emp.EMPLOYEE_NUMBER, models.Emp.EMPLOYEE_NAME).all()