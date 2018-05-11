import numpy as np

def log_base_2_for_entropy(x):
    """
    For entropy calculations we define 0 * log(0) == 0
    """
    return 0 if x == 0 else np.log2(x)

def entropy(p):
    """
    p is the proportion of positive examples in training set S;
    1 - p is the proportion of negative examples in training set S;
    0 * log(0) == 0
    """
    p_pos = p
    p_neg = 1 - p
    
    pos_term = -p_pos * log_base_2_for_entropy(p_pos)
    neg_term = -p_neg * log_base_2_for_entropy(p_neg)
    
    return pos_term + neg_term  