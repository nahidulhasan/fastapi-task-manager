from sqlalchemy.orm import Session
from . import models, schemas
from .core import get_password_hash, verify_password


# -----------------------
# USER CRUD
# -----------------------

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Create user with hashed password."""
    hashed = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    """Verify user exists and password matches."""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


# -----------------------
# TASK CRUD (unchanged)
# -----------------------

def create_task(db: Session, user_id: int, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_task(db: Session, user_id: int, task_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == user_id, models.Task.id == task_id)
        .first()
    )


def update_task(db: Session, db_task, task_update: schemas.TaskUpdate):
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, db_task):
    db.delete(db_task)
    db.commit()
