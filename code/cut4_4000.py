import pandas as pd
import os,sys
import re

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
print(father_path)
os.chdir(father_path)
wantpath = father_path


# data_reader = pd.read_csv("testresult/testall.csv",chunksize=2000)

# pdcut0 = pd.DataFrame()
# jishu = 0
# for chunk in data_reader:
#     #连接chunk
#     if(jishu>99):
#         break
#     pdcut0 = pdcut0.append(chunk)
readCsvPath = os.path.join("testresult", "testop0920.csv")
pdcut0 = pd.read_csv(readCsvPath, index_col=False)
pdcut = pdcut0
# pdcut = pdcut0.iloc[4500:5000]
# print(pdcut)
print(len(pdcut['opcode']))
print(type(pdcut['opcode']))

delList = ['DUP1', 'DUP2', 'DUP3', 'DUP4', 'DUP5', 'DUP6', 'DUP7','DUP8', 'DUP9', 'DUP10', 'DUP11', 'DUP12',\
'DUP13','DUP14', 'DUP15', 'DUP16','SWAP1', 'SWAP2', 'SWAP3', 'SWAP4', 'SWAP5','SWAP6', 'SWAP7', \
'SWAP8', 'SWAP9', 'SWAP10','SWAP11', 'SWAP12', 'SWAP13', 'SWAP14', 'SWAP15', 'SWAP16', 'POP' ]

# tmpStr = "3   4"
# tmpStr2 = re.sub(r'\b0[xX][0-9a-fA-F]+\b', "", tmpStr)

avgLen = 0

for i in range(0,len(pdcut)):
    tmpStr = str(pdcut['opcode'][i])
    if(i==22):
        print(len(tmpStr))
    # 序列处理
    tmpStr = re.sub(r'\b0[xX][0-9a-fA-F]+\b', "", tmpStr)
    for kk in delList:
        tmpStr = re.sub(str(kk), "", tmpStr)
    tmpStr = re.sub(r'\s{2,}', " ", tmpStr)
    avgLen += len(tmpStr)
    if(i==22):
        print(len(tmpStr))
    if(len(tmpStr)>2000):
        tmpStr = tmpStr[0:1999]
        tmpStr = tmpStr.rsplit(" ",1)
        pdcut['opcode'][i] = tmpStr[0]
avgLen /= len(pdcut)
print(avgLen)
pdcut0.to_csv("testresult/testop_2000.csv", index=False)

g1 = pd.DataFrame(pdcut, columns = ['opcode','a1'])
g2 = pd.DataFrame(pdcut, columns = ['opcode','a2'])
g3 = pd.DataFrame(pdcut, columns = ['opcode','a3'])
g4 = pd.DataFrame(pdcut, columns = ['opcode','a4'])
g1.columns = ['opcode','label']
g2.columns = ['opcode','label']
g3.columns = ['opcode','label']
g4.columns = ['opcode','label']
g1.to_csv("testresult/res_1.csv", encoding="utf_8_sig",index = False)
g2.to_csv("testresult/res_2.csv", encoding="utf_8_sig",index = False)
g3.to_csv("testresult/res_3.csv", encoding="utf_8_sig",index = False)
g4.to_csv("testresult/res_4.csv", encoding="utf_8_sig",index = False)