from enum import IntEnum

XML_FILE = 'report.xml'
LLL_MODEL = 'gpt-3.5-turbo'
TIMEZONE = 'Europe/Moscow'
TOKENS_QUANTITY = 500


class Numerics(IntEnum):
    ANALYTICS_LENGTH = 2000
    ANALYTICS_MIN = 1
    DATE_LENGTH = 10
    TOKENS_QUANTITY = 500
    TASK_HOURS = 1
    TASK_MINUTES = 30
