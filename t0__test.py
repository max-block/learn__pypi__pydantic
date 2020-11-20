from pydantic import BaseModel, Field, StrictStr


class Data(BaseModel):
    from_address: StrictStr


d = Data(**{"from_address": 0x123})
print(d.dict())
# {"from_": "123"}
