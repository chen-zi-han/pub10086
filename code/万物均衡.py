import pandas as pd
import numpy as np
import os,sys

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
print(father_path)
os.chdir(father_path)
wantpath = father_path


for i in range(1,5):
    csvPath = "testresult/res_" + str(i) + ".csv"
    pdcut0 = pd.read_csv(csvPath, index_col=False)
    
    df1 = pdcut0[pdcut0['label'] == 1]
    df2 = pdcut0[pdcut0['label'] == 0]
    print(len(df1))
    tmpNum = len(df1)*4
    if(tmpNum + len(df1) < len(df2)):
        df2 = df2.sample(n = tmpNum, random_state = 10)
    #打乱
    df1 = df1.sample(frac=1.0, random_state=10).reset_index(drop=True)
    df2 = df2.sample(frac=1.0, random_state=10).reset_index(drop=True)
    print(df1.shape,df2.shape)
    pdcut = pd.concat([df1,df2])
    pdcut = pdcut.sample(frac=1.0, random_state=10).reset_index(drop=True)
    pdcut = pdcut.sample(frac=1.0, random_state=10).reset_index(drop=True)
    witeCsvPath = "testresult/pingheng" + str(i) + ".csv"
    pdcut.to_csv(witeCsvPath, index=False)