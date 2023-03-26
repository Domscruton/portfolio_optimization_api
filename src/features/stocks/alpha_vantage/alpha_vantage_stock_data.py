import logging

from stocks.models import StockDataSourceEnum
from stocks.stock_data import StockData


class AlphaVantageStockData(StockData):
    def __init__(self, settings: AlphaVantageSettings) -> None:
        self._logger = logging.getLogger()
        self._settings = settings

    def provider_name(self) -> str:
        return StockDataSourceEnum.AlphaVantage.value
    # see the provider files under credit_management as an example
