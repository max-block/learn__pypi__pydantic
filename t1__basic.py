from typing import Optional

from pydantic import BaseModel, Field


class Data1(BaseModel):
    id: Optional[int] = Field(None, alias="_id")
    name: str


class Data2(BaseModel):
    id: Optional[int] = Field(..., alias="_id")
    name: str


d1 = Data1(_id=1, name="d1")

d2 = Data2(_id=2, name="d2")

print(d1)
print(d2)
