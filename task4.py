import scipy.stats as stats

mean_income = 3000  
std_dev_income = 500  
income_limit = 2000  

cumulative_prob = stats.norm.cdf(income_limit, mean_income, std_dev_income)

percentage_less_than_2000 = cumulative_prob * 100

print(f"kumulaciuri albatoba naklebi {income_limit} evroze aris: {cumulative_prob:.4f}")
print(f"momxmarebelta procentuli raodenoba {income_limit} evroze naklebit: {percentage_less_than_2000:.2f}%")
