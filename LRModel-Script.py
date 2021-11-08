import numpy as np 
import pandas as pd 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
df = pd.DataFrame(d) 
df.head()
df.info()
df.describe().T['std']
df.isnull().sum()
df.corr()
df.corr()['Consumption']

import seaborn as sns
sns.pairplot(df,kind="reg")
sns.jointplot(x="Consumption",y="income",data=df,kind="reg")
sns.jointplot(x="Consumption",y="tax",data=df,kind="reg")

import statsmodels.api as sm
X=df[["tax"]]
X[0:5]
X=sm.add_constant(X)
X[0:5]
y=df["Consumption"]
lm=sm.OLS(y,X)
model=lm.fit()
model.summary()

import statsmodels.formula.api as smf
lm=smf.ols("Consumption ~ tax",df)
model=lm.fit()
model.summary()
model.params
print(model.summary().tables[1])
model.conf_int()
model.f_pvalue
print("f_pvalue: ","%.4f"%model.f_pvalue)
print("fvalue: ","%.2f"%model.fvalue)
print("tvalue: ","%.2f"%model.tvalues[0:1])
print("tvalue: ","%.2f"%model.tvalues[1:2])
model.rsquared_adj

for i in range(10):
    est=(984.6084+(-53.4869*i))
    print("{}".format(i) +". estimation: "+str(est))
print("Consumption of petrol = "+str("%.2f"%model.params[0])+ " + Petrol Tax "+ "* "+ str("%.2f"%model.params[1]))

g = sns.regplot(df["Consumption"], df["tax"], ci=None, scatter_kws={'color':'r', 's':9})
g.set_title("Model Equation: Consumption of petrol = 984.61 + Petrol Tax*-53.49")
g.set_ylabel("Petrol Tax")
g.set_xlabel("Consumption of petrol")
