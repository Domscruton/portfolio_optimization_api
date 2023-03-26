import requests


class StockData:
    """
    BaseModel for all stock data, independent of the API datasource used

    Therefore may need to convert the results from different API providers into
    a result set that can be generalized to the StockData class
    """
