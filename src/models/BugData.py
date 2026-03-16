from typing import Optional

from pydantic import BaseModel


class BugData(BaseModel):
    title: str
    description: str
    component: str
    version: str
    created_time: Optional[str] = ""
