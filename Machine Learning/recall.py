import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    tp = np.sum([(y_true[i] == 1 and y_pred[i]==1) for i in range(len(y_true))])
    fn = np.sum([(y_true[i] == 1 and y_pred[i]==0) for i in range(len(y_true))])

    recall = tp / (tp + fn)

    return recall if (tp+fn != 0) else 0.0

