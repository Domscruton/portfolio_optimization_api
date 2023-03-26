from pydantic import BaseModel


class stock_data_point(BaseModel):
    ticker: str
    value: float
