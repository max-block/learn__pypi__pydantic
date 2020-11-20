from pydantic import BaseModel, StrictStr, ValidationError


class Data(BaseModel):
    from_address: StrictStr


print(Data(**{"from_address": "0x123"}))
# from_address='0x123'

try:
    print(Data(**{"from_address": 0x123}))
except ValidationError:
    print("validation error!")
    # validation error!
