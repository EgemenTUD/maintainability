import pandas as pd
from scipy.stats import shapiro

# Data from the user (Include your data here) (random data given as an example)
data = {
    "A": [3,4,5],
    "B": [2,4,6],
    "C": [1,4,5],
}

# Perform Shapiro-Wilk test for normality on each metric
results = {metric: shapiro(values) for metric, values in data.items()}

# Format results
shapiro_results = pd.DataFrame({
    "Metric": list(results.keys()),
    "W Statistic": [res.statistic for res in results.values()],
    "p-value": [res.pvalue for res in results.values()],
    "Normality": ["Yes" if res.pvalue > 0.05 else "No" for res in results.values()]
})

# Check the final column for normality results.
shapiro_results