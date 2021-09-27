from pydantic import BaseModel, Field


class Data(BaseModel):
    from_: int = Field(..., alias="from")

    class Config:
        allow_population_by_field_name = True


d = Data(**{"from": 123})
print(d.dict())
# {"from_": 123}

print(d.dict(by_alias=True))
# {'from': 123}


print(Data(from_=321))  # allow_population_by_field_name is required
