from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="EMPLOYEE API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def pod():
    return 'Hello Pod World!'


@app.get("v1/docs")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/emp/", response_model=list[schemas.Emp])
def read_items(db: Session = Depends(get_db)):
    emp = crud.get_items(db)
    return emp


# @app.get("/emp/{EMPLOYEE_NUMBER}", response_model=list[schemas.Emp])
# def emp_by_id(EMPLOYEE_NUMBER: int, session: Session = Depends(get_db)) -> Emp:
#     emp = session.get(Emp, EMPLOYEE_NUMBER)
#     if emp:
#         return emp
#     else:
#         raise HTTPException(status_code=404, detail=f"No car with id={id}.")
