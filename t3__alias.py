from pydantic import BaseModel, Field


class Data(BaseModel):
    from_: int = Field(..., alias="from")


d = Data(**{"from": 123})
print(d.dict())
# {"from_": 123}

print(d.dict(by_alias=True))
# {'from': 123}


# d = Data(from_=321) <-- can't do it. It required {"from": 123}
