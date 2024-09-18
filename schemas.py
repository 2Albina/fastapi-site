from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str | None = None  # Optional[str] = None  


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
    