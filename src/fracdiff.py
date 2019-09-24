import pandas as pd
import numpny as np
import matplotlib.pyplot as plt


class Fracdiff:
    def __init__(self, path: str) -> None:
        self.path = path
        self.data = self.load_data(self.path)
        self.weights = []
        self.d = None

    // load in data and restrict to index col and next col over for simplicity
    def load_data(self, path: str, index_name = 'Date'):
        loaded = pd.read_csv(path)
        loaded.set_index(index_name)
        return loaded.iloc[:,:2]

    def compute_weights(self, d):
        weights = [1]
        for i in range(self.data.shape[0]):
            k = i+1
            weights.append(-1*weights[i]*((d-k+1)/k))
        return weights

    def compute_series(self, d):
        pass

    def plot_weights():
        plt.scatter(range(len(self.weights)), self.weights)
        plt.show()

    def plot_series():
        pass

