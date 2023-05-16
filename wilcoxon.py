from scipy.stats import wilcoxon

# Emotional support
eff_e = [6,5,7,6,6,7,5,5]
use_e = [7,5,6,6,6,7,6,6]
ben_e = [6,4,6,5,6,7,5,5]
well_e = [7,5,5,4,5,7,4,5]

# Practical advice
eff_p = [7,3,7,6,6,7,6,5]
use_p = [6,3,6,6,7,7,6,6]
ben_p = [6,5,7,6,6,7,6,6]
well_p = [7,4,6,6,6,7,6,5]

# Perform Wilcoxon signed-rank test for emotional support vs practical advice
stat, p = wilcoxon([sum(eff_e), sum(use_e), sum(ben_e), sum(well_e)], 
                   [sum(eff_p), sum(use_p), sum(ben_p), sum(well_p)])

print("Wilcoxon signed-rank test results:")
print("Statistic =", stat)
print("p-value =", p)

