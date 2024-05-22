from sqlalchemy.orm import Session
from database.models import Task
from typing import List


def orm_create_task(db: Session, title: str, description: str = None) -> Task:
    """
    Создание новой задачи.
    """
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def orm_get_task_by_id(db: Session, task_id: int) -> Task:
    """
    Получение информации о задаче по идентификатору.
    """
    return db.query(Task).filter(Task.id == task_id).first()


def orm_get_all_tasks(db: Session) -> List[Task]:
    """
    Получение списка всех задач.
    """
    return db.query(Task).all()


def orm_update_task(db: Session, task_id: int, title: str = None, description: str = None) -> Task:
    """
    Обновление задачи по идентификатору.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        if title:
            task.title = title
        if description:
            task.description = description
        db.commit()
        db.refresh(task)
    return task


def orm_delete_task(db: Session, task_id: int) -> bool:
    """
    Удаление задачи по идентификатору.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
