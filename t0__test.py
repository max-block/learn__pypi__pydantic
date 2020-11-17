from pydantic import BaseModel, Field


class Data(BaseModel):
    from_: str = Field(..., alias="from")

    # class Config:
    #     fields = {"from_": "from"}


d = Data(**{"from": 123})
print(d.dict())
# {"from_": "123"}

print(d.dict(by_alias=True))
# {'from': '123'}
