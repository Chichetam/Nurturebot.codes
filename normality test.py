from scipy.stats import shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Emotional support
E_eff = [6, 5, 7, 6, 6, 7, 5, 5]
E_use = [7, 5, 6, 6, 6, 7, 6, 6]
E_ben = [6, 4, 6, 5, 6, 7, 5, 5]
E_wel = [7, 5, 5, 4, 5, 7, 4, 5]

# Practical advice
Pr_eff = [7, 3, 7, 6, 6, 7, 6, 5]
Pr_use = [6, 3, 6, 6, 7, 7, 6, 6]
Pr_ben = [6, 5, 7, 6, 6, 7, 6, 6]
Pr_wel = [7, 4, 6, 6, 6, 7, 6, 5]

# Dictionary of variable names and values
variables = {
    "E_eff": E_eff, "E_use": E_use, "E_ben": E_ben, "E_wel": E_wel,
    "Pr_eff": Pr_eff,"Pr_use": Pr_use,"Pr_ben": Pr_ben,"Pr_wel": Pr_wel }

# Perform Shapiro-Wilk test and display distribution plot for each variable
for variable_name, variable in variables.items():
    shapiro_result = shapiro(variable)
    print("The Shapiro test result for " + variable_name + " is: " + str(shapiro_result))
    sns.distplot(variable)
    plt.show()
