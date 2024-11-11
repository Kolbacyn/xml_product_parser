from pydantic import BaseModel, Field


class SalesReportBase(BaseModel):
    report: str = Field(..., min_length=1, max_length=1000)
    date: str = Field(..., max_length=10)


class SalesReportCreate(SalesReportBase):
    pass
