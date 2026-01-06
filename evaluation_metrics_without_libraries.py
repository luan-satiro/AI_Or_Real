import numpy as np

def get_confusion_table(prediction_tensor, truth_tensor) :
    TruePositives = 0
    FalsePositives = 0
    TrueNegatives = 0
    FalseNegatives = 0
    try:
        for i in range(len(prediction_tensor)):
            if prediction_tensor[i] == truth_tensor[i] and prediction_tensor[i] == 1:
                TruePositives+=1
            elif prediction_tensor[i] == truth_tensor[i] and prediction_tensor[i] == 0:
                TrueNegatives+=1
            elif prediction_tensor[i] != truth_tensor[i] and prediction_tensor[i] == 0:
                FalseNegatives+=1
            else:
                FalsePositives+=1
    except Exception as e:
        print('Error! ' + e)
        return None
    
    confusion_table = [[],[]]
    confusion_table[0].insert(0, TruePositives)
    confusion_table[0].insert(1, FalseNegatives)
    confusion_table[1].insert(0, FalsePositives)
    confusion_table[1].insert(1, TrueNegatives)

    return confusion_table

def get_sensibility(confusion_table):
    VP = confusion_table[0][0]
    FN = confusion_table[0][1]

    sensibility = VP / (VP + FN)

    return sensibility

def get_specificity(confusion_table):
    VN = confusion_table[1][1]
    FP= confusion_table[1][0]

    specificity = VN / (VN + FP)

    return specificity

def get_accuracy(confusion_table):
    VP = confusion_table[0][0]
    VN= confusion_table[1][1]
    FP= confusion_table[1][0]
    FN = confusion_table[0][1]

    N = VP + VN + FP + FN

    accuracy = VN + VP / N

    return accuracy

def get_precision(confusion_table):
    VP = confusion_table[0][0]
    FP= confusion_table[1][0]

    precision = VP / (VP + FP)

    return precision

def get_f_score(confusion_table):
    precision = get_precision(confusion_table)
    sensibility = get_sensibility(confusion_table)
    f_score = 2 * (precision * sensibility) / (precision + sensibility)

    return f_score
