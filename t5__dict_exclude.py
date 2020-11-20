from pydantic import BaseModel, Field, StrictStr


class Data(BaseModel):
    name: str
    age: int
    value: float


d = Data(name="n1", age=11, value=3.3)
print(d.dict(exclude={"age"}))
# {'name': 'n1', 'value': 3.3}
