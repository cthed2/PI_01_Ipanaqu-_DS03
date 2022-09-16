import numpy as np
import pandas as pd
import numpy as np
import pandas as pd

def encontrar_vacios_2(data):
    df = data
    b = []

    for i in range(0,len(df.columns)):
        k = df.iloc[:,i]
        k = k.squeeze()
        k = k.astype(str)
        mask = k == ""
        z = k[mask]
        z = z.shape[0]
        b.append(z)

    for i in range(0,len(b)):
        if b[i]>0:
            df.iloc[:,i].replace("",np.nan, inplace = True)
          
    
    return df

