from machine_learning.helper.metric_calculator import MetricCalculator
from machine_learning.helper.conditions.equal import EqualCondition
import torch

class Accuracy(object):

    @classmethod
    def binary(self, y_pred, y_test):
        y_pred_tag = torch.round(torch.sigmoid(y_pred))

        correct_results_sum = (y_pred_tag == y_test).sum().float()
        accuracy = correct_results_sum/y_test.shape[0]
        accuracy = torch.round(accuracy * 100)
        
        return accuracy

    @classmethod
    def reg(self, y_pred, y_test):
        return MetricCalculator.calculate(y_pred, y_test, EqualCondition)
