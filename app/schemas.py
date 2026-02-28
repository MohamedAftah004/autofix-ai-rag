from pydantic import BaseModel

class DiagnoseRequest(BaseModel):
    description: str
    car_model: str | None = None