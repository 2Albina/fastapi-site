from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
   prefix="/tasks",
   tags=["Таски"],
)


@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return {"data": tasks}