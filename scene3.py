import numpy as np
import pandas as pd 


df = pd.DataFrame({"A" : [1, 2, np.nan, 4, 5, np.nan], 
                    "B" : [np.nan, 2, np.nan, 4, np.nan, np.nan], 
                    "C" : [1, 2, 3, 4, 5, np.nan]})


check = df.isnull().sum() / len(df) 

cols = check[check > 0.5].index
df.isnull().sum()*100/len(df)
