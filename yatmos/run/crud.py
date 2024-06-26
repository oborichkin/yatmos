from sqlalchemy.orm import Session
from .model import Run
from .schema import RunCreate, RunUpdate
from yatmos.project.model import Project


def get_run(db: Session, run_id: int):
    return db.query(Run).filter(Run.id == run_id).first()


def get_runs(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(Run).filter(Run.project_id == project_id).offset(skip).limit(limit).all()


def create_run(db: Session, run: RunCreate, project_id: int):
    proj = db.query(Project).filter(Project.id == project_id).one()
    return proj.make_run(db, **run.model_dump())


def delete_run(db: Session, run_id: int):
    run = db.query(Run).filter(Run.id == run_id)
    run.delete()
    db.commit()


def update_run(db: Session, run_id: int, run: RunUpdate):
    upd_run = db.query(Run).filter(Run.id == run_id)
    upd_run.update(run.model_dump(exclude_unset=True))
    db.commit()
    upd_run = upd_run.first()
    db.refresh(upd_run)
    return upd_run
