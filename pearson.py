from scipy.stats import pearsonr

def pearson_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient and p-value between two arrays.

    Parameters:
        x (list or array-like): First set of data.
        y (list or array-like): Second set of data.

    Returns:
        corr (float): Pearson correlation coefficient.
        p_value (float): Two-tailed p-value.
    """
    corr, p_value = pearsonr(x, y)
    return corr, p_value

# Edit the following lines to set your parameters
if __name__ == "__main__":
    x = []
    y = []
    corr, p = pearson_correlation(x, y)
    print(f"Pearson correlation: {corr:.3f}, p-value: {p:.3g}")