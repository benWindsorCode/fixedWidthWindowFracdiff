import pandas as pd


class Fracdiff:
    def __init__(self, path: str) -> None:
        self.path = path
        self.data = self.load_data(self.path)

    // load in time series, using column name 'Date' for index and assume other data in next column over
    def load_data(self, path: str):
        loaded = pd.read_csv(path)
        loaded.set_index('Date')
        return loaded.iloc[:,:2]
