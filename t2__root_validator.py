from typing import Optional

from pydantic import BaseModel, root_validator


class Data(BaseModel):
    name: str
    age: int
    other: Optional[str] = None

    @root_validator
    def validate_name_and_age(cls, values):
        if values["age"] < 18 and values["name"] == "Bill":
            raise ValueError("illegal combination of age and name")
        return values


d = Data(name="n1", age=123)
print(d)

d = Data(name="Bill", age=17)
print(d)
