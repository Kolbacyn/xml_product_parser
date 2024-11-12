from pydantic import BaseModel, Field


class SalesReportBase(BaseModel):
    date: str = Field(..., max_length=10)
    report: str = Field(..., min_length=1, max_length=1000)


class SalesReportCreate(SalesReportBase):
    pass


class SalesReportDB(SalesReportBase):
    report: str
