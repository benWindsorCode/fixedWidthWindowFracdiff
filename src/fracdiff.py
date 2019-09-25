import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Fracdiff:
    def __init__(self, path: str) -> None:
        self.path = path
        self.data = self.load_data(self.path)
        self.weights = []
        self.threshold = 0.00001
        self.d = None
        self.threshold_pos = None
        self.diff_series = None

    # load in data and restrict to index col and next col over for simplicity
    def load_data(self, path: str, index_name = 'Date'):
        loaded = pd.read_csv(path)
        loaded.set_index(index_name)
        return loaded.iloc[:,:2]

    # once weight is smaller than threshold then no longer compute
    def compute_weights(self, d):
        weights = [0] * self.data.shape[0]
        weights[0] = [1]
        for i in range(self.data.shape[0]):
            k = i+1
            new_val = (-1*weights[i]*((d-k+1)/k))
            if abs(new_val) >= self.threshold:
                weights[i] = new_val
            else:
                self.threshold_pos = i-1
                break
        return weights

    def compute_series(self, d):
        new_vals = [0]*self.data.shape[0]
        for i in range(self.data.shape[0]-self.threshold_pos-1, self.data.shape[0]):
            sum = 0
            for j in range(self.threshold_pos):
                sum += self.weights[j]*self.data.iloc[i-j]
            new_vals[i] = sum

    def plot_weights():
        plt.scatter(range(len(self.weights)), self.weights)
        plt.show()

    def plot_series():
        pass

