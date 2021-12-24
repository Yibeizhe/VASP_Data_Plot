import pandas as pd
import numpy as np
djf=pd.DataFrame(np.arange(16).reshape(4,4),
                 index=['A','B','V','W'],
                 columns=['d','s','f','h'])
print(djf)
print(djf.loc['B'][1])