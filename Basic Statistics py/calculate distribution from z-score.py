# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 17:55:23 2022

@author: Acer
"""

import numpy as np
from scipy import stats
from scipy.stats import norm
# Mean profits from two different divisions of a company = Mean1 + Mean2
Mean = 5+7
print('Mean Profit is Rs', Mean*45,'Million')
# Variance of profits from two different divisions of a company = SD^2 = SD1^2 + SD2^2
SD = np.sqrt((9)+(16))
print('Standard Deviation is Rs', SD*45, 'Million')
# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
print('Range is Rs',(stats.norm.interval(0.95,540,225)),'in Millions')
# (95% probability in the normal distribution, mean, std dev)
# B. Specify the 5th percentile of profit (in Rupees) for the company
# To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.645
X= 540+(-1.645)*(225)
# mean+ (z-score dari 5% probability)*std dev
print('5th percentile of profit (in Million Rupees) is',np.round(X,))
# compare loss between division
# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,32)
stats.norm.cdf(0,7,42)
