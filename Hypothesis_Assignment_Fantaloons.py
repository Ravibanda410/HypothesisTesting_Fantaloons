# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:51:15 2020

@author: RAVI
"""

import pandas as pd

from scipy import stats

import numpy as np

Fantaloons=pd.read_excel("C:\RAVI\Data science\Assignments\Modue 5 Hypothesis\Fantaloons.xlsx")
Fantaloons

from statsmodels.stats.proportion import proportions_ztest

tab1= Fantaloons.Weekdays.value_counts()
tab1
tab2=Fantaloons.Weekend.value_counts()
tab2

pd.crosstab(Fantaloons.Weekdays,Fantaloons.Weekend)

count = np.array([47,167])
nobs = np.array([113,287])

#Ho= Proportions of Male and Female are same
#Ha= Proportions of Male and Female are not same

stats,pval=proportions_ztest(count,nobs,alternative='two-sided')
print(pval)
# p-value = 0.0027 < 0.05 accept alternate hypothesis i.e. Unequal proportions

#find out whose proportion is higher
#Ho= Proportions of Male is less than Female
#Ha= Proportions of Male is greater than Female
stats,pval1=proportions_ztest(count,nobs,alternative='larger')
print(pval1)        
# p-value = 0.998 > 0.05 accept null hypothesis


#Proportions of Male is walking into store less than Female