import numpy as np

def effect_size(group1_data, group2_data):
    n1, n2 = len(group1_data), len(group2_data)

    if n1 < 2 or n2 < 2:
        return None

    mean1, mean2 = np.mean(group1_data), np.mean(group2_data)
    std1, std2 = np.std(group1_data, ddof=1), np.std(group2_data, ddof=1) # ddof=1 for sample std dev

    try:
        pooled_std = np.sqrt(((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / (n1 + n2 - 2))
    except ZeroDivisionError:
        return None

    if pooled_std == 0:
        return 0.0

    d = (mean1 - mean2) / pooled_std
    return d

# Data
method_a_scores = []
method_b_scores = []
method_c_scores = []
method_d_scores = []
method_e_scores = []
method_f_scores = []

# Store all other methods in a dictionary for easy iteration
other_methods = {
    "Method B": method_b_scores,
    "Method C": method_c_scores,
    "Method D": method_d_scores,
    "Method E": method_e_scores,
    "Method F": method_f_scores,
}

for name, scores in other_methods.items():
    effect_size_d = effect_size(method_a_scores, scores)
    if effect_size_d is not None:
        print(f"Effect Size Calculation for Method A vs. {name}: {effect_size_d:.3f}")
