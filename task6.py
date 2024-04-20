import numpy as np
from scipy.stats import ttest_1samp, ttest_ind

sample_data = np.random.normal(loc=10, scale=2, size=100) 
sample_data_1 = np.random.normal(loc=10, scale=2, size=100)  
sample_data_2 = np.random.normal(loc=12, scale=2, size=100) 

null_hypothesis_1 = "nimushis sashualo tolia 10is"
alternative_hypothesis_1 = "nimushis sashualo ar udris 10s"

t_statistic_1, p_value_1 = ttest_1samp(sample_data, 10)

print("t-test Results:")
print("H0:", null_hypothesis_1)
print("H1:", alternative_hypothesis_1)
print("t-statistic:", t_statistic_1)
print("p-value:", p_value_1)
if p_value_1 < 0.05:
    print("Result: Reject ")
else:
    print("Result: Fail to reject ")


null_hypothesis_2 = "ori nimushis sashualo tolia"
alternative_hypothesis_2 = "ori nimushis sashualo gansxvavdeba"

t_statistic_2, p_value_2 = ttest_ind(sample_data_1, sample_data_2)

print("\n2 t-test Results:")
print("2 H0:", null_hypothesis_2)
print("2 H1:", alternative_hypothesis_2)
print("2 t-statistic:", t_statistic_2)
print("2 p-value:", p_value_2)
if p_value_2 < 0.05:
    print("Result: Reject ")
else:
    print("Result: Fail to reject")
