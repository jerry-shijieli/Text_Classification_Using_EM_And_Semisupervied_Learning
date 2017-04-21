import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB

class Semi_EM_MultinomialNB():
    """
    Naive Bayes classifier for multinomial models for semi-supervised learning.
    
    Use both labeled and unlabeled data to train NB classifier, update parameters
    using unlabeled data, and all data to evaluate performance of classifier. Optimize
    classifier using Expectation-Maximization algorithm.
    """
    def __init__(self, alpha=1.0, fit_prior=True, class_prior=None):
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior

    def fit(self, X_l, y_l, X_u):
        pass

    def partial_fit(self, X_l, y_l, X_u):
        pass

    def predict(self, X):
        pass

    def score(self, X, y):
        pass