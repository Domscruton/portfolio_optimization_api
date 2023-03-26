from enum import Enum


class StockDataSourceEnum(str, Enum):
    AlphaVantage = "Alpha Vantage"
    Yahoo = "Yahoo"
