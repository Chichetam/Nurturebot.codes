from scipy.stats import mannwhitneyu

# Emotional support
E_eff = [6,5,7,6,6,7,5,5]
E_use = [7,5,6,6,6,7,6,6]
E_ben = [6,4,6,5,6,7,5,5]
E_wel = [7,5,5,4,5,7,4,5]

# Practical advice
Pr_eff = [7,3,7,6,6,7,6,5]
Pr_use = [6,3,6,6,7,7,6,6]
Pr_ben = [6,5,7,6,6,7,6,6]
Pr_wel = [7,4,6,6,6,7,6,5]

# Perform Mann-Whitney U test for emotional support vs practical advice
stat, p = mannwhitneyu([sum(E_eff), sum(E_use), sum(E_ben), sum(E_wel)], 
                   [sum(Pr_eff), sum(Pr_use), sum(Pr_ben), sum(Pr_wel)])

print("Mann-Whitney U test results:")
print("Statistic =", stat)
print("p-value =", p)
