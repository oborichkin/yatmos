from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud
from .schema import Run, RunUpdate
from ..dependencies import get_db

router = APIRouter(prefix="/run", tags=["Run"])


@router.get("/{id}", response_model=Run, response_description="Run retrieved")
def get_run(id: int, db: Session = Depends(get_db)):
    run = crud.get_run(db, run_id=id)
    if not run:
        raise HTTPException(404, "run not found")
    return run


@router.delete("/{id}")
def delete_run(id: int, db: Session = Depends(get_db)):
    run = crud.delete_run(db, run_id=id)
    return run


@router.patch("/{id}")
def update_run(id: int, run: RunUpdate, db: Session = Depends(get_db)):
    return crud.update_run(db, id, run)