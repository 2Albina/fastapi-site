from database import TaskTable, new_session
from sqlalchemy import select
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskTable(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id
        
    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model.__dict__) for task_model in task_models]
            return tasks