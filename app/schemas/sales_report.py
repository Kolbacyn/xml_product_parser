from pydantic import BaseModel, Field

from app.services.constants import Numerics


class SalesReportBase(BaseModel):
    date: str = Field(
        ...,
        max_length=Numerics.DATE_LENGTH
        )
    report: str = Field(
        ...,
        min_length=Numerics.ANALYTICS_MIN,
        max_length=Numerics.ANALYTICS_LENGTH
        )


class SalesReportCreate(SalesReportBase):
    pass


class SalesReportDB(SalesReportBase):
    report: str
