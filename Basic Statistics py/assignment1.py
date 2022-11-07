2 + 2 # Function F9
# works as calculator

# Python Libraries (Packages)
# pip install <package name> - To install library (package), execute the code in Command prompt
# pip install pandas

import pandas as pd

# Read data into Python
book = pd.read_csv("C:\\Users\\Acer\\Downloads\\module4\\WC.csv")

# C:\Users\Desktop\education.csv - this is windows default file path with a '\'
# C:\\Users\\Desktop\\education.csv - change it to '\\' to make it work in Python

#Exploratory Data Analysis for Points column
#Measures of Central Tendency / First moment business decision
book.MPG.mean() # '$' is used to refer to the variables within object
book.WT.median()
book.AT.mode()

from scipy import stats
stats.mode(book.Measure)

# Measures of Dispersion / Second moment business decision
book.Measure.var() # variance
book.MPG.std()#standard deviation
range = max(module.Points) - min(module.Points) # range
print(range)


#Exploratory Data Analysis for Score column
module.Score.mean() # '$' is used to refer to the variables within object
module.Score.median()
module.Score.mode()

from scipy import stats
stats.mode(module.Score)

# Measures of Dispersion / Second moment business decision
module.Score.var() # variance
module.Score.std()#standard deviation
range = max(module.Score) - min(module.Score) # range
range

#Exploratory Data Analysis for Weigh column
module.Weigh.mean() # '$' is used to refer to the variables within object
module.Weigh.median()
book.Waist.mode()

from scipy import stats
stats.mode(module.Weigh)

# Measures of Dispersion / Second moment business decision
module.Weigh.var() # variance
module.Weigh.std()#standard deviation
range = max(module.Weigh) - min(module.Weigh) # range
range


#Third moment business decision
book.AT.skew()

#Fourth moment business decision
book.WT.kurt()

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np

plt.bar(height = module.Points, x = np.arange(1,33,1)) # initializing the parameter

plt.hist(book.AT) #histogram

plt.boxplot(book.Waist) #boxplot

#Normal Quantile-Quantile Plot
import scipy.stats as stats
import pylab

# Checking Whether data is normally distributed
stats.probplot(book.Waist, dist="norm",plot=pylab)

stats.probplot(education.workex,dist="norm",plot=pylab)

#transformation to make workex variable normal
import numpy as np
stats.probplot(np.log(education.workex),dist="norm",plot=pylab)

#z-distribution (UNTUK DPT P(X>1), KENA BUAT 1-jwpn yg dpt)
# cdf => cumulative distributive function; # similar to pnorm in R (prob yg kita kira,mean,std dev)
stats.norm.cdf(20,34.422,9.1314)    # given a value, find the probability
#untuk yg ada interval: contoh P(20<X<50)
stats.norm.cdf(20,34.422,9.1314) - stats.norm.cdf(50,34.422,9.1314) #DPT NEGATIVE SBB TERBALIK
# ppf => Percent point function; # similar to qnorm in R
stats.norm.ppf(0.975,0,1) # given probability, find the Z value

#t-distribution
stats.t.cdf(1.98,139) # given a value, find the probability; # similar to pt in R
stats.t.ppf(0.975, 139) # given probability, find the t value; # similar to qt in R

help(stats.t.ppf) 


