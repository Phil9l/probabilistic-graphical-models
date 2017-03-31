from collections import defaultdict


__all__ = ['NaiveBayesClassifier']


class NaiveBayesClassifier:
    def __init__(self):
        self._class_data = defaultdict(dict)

    def train(self, data, cls):
        raise NotImplementedError

    def predict(self, data):
        raise NotImplementedError
