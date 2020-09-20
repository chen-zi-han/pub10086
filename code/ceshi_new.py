import os,sys
import json
import csv
import pandas as pd
current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
print(father_path)
os.chdir(father_path)
wantpath = father_path 

# print(jsonPath)

jishu = 0
nameList = []

# byteList = []
opList = []
typeList = []


#源文件缺失，换用代码块2
# for root, dirs, files in os.walk("/result", topdown=True):
#     # if(jishu>30):
#     #     break
#     jishu += 1
#     if(jishu==1):
#         nameList = dirs
#     else:
#         # if(jishu%1024==5):
#         #     print(nameList[jishu-2])
#         #     print(root)
#         tmpByte = ""
#         tmpOp = ""
#         for name in files:
#             if name.endswith(".bin"): 
#                 # print(os.path.join(root, name))
#                 with open( os.path.join(root, name), 'r' ) as f:
#                     tmpByte +=  f.read()
#             elif name.endswith(".opcode"): 
#                 with open( os.path.join(root, name), 'r' ) as f:
#                     tmpOp +=  f.read()
#         byteList.append(tmpByte)
#         opList.append(tmpOp)
#             # type_specific_fields
#         # for name in files:
#         #     tmpPath = os.path.join(root,name)
#         #     print('yy',tmpPath)
#             # with open( './result_6/0x0a0ba2b6d7955029653b9f7ce42f7b6760d705ac/0x0a0ba2b6d7955029653b9f7ce42f7b6760d705ac.json', 'r' ) as f:
#             #     print( f.read() ) 
#     # for name in dirs:
#     #     print("ll  ",os.path.join(root, name))

#代码块2
readCsvPath = os.path.join("testresult", "testall.csv")
yuanDfTestall = pd.read_csv(readCsvPath, index_col=False)
ii = 0
for tmpDf in zip(yuanDfTestall['address'], yuanDfTestall['opcode']):
    # if(ii<3):
    #     ii += 1
    #     print(tmpDf[0],type(tmpDf[1]))
    nameList.append(tmpDf[0])
    opList.append(tmpDf[1])



print(len(nameList))
# print(len(byteList))
print(len(opList))
# print(type(nameList[2]))
jsonPath = os.path.join(father_path, "results_wild.json")
# print("jp",jsonPath)
csvhead = ["address","a1","a2","a3","a4","opcode"]
# csvhead = ["地址","重入","算术溢出","时间攻击","未检查低乎","OpCode"]
allList = []
tmpOpCsv = pd.DataFrame(columns=csvhead)
with open(jsonPath, 'r' ) as f :
    jsonFile = json.load(f)
    jsonKeys = jsonFile.keys()

    # 下面有重写的逻辑
    # with open(os.path.join("testresult", "testop0920.csv"),'w',newline='') as g :
    #     g_csv = csv.writer(g)
    #     g_csv.writerow(csvhead)
    #     jishu = 0
    #     for i in range(0,len(nameList)):
    #         if nameList[i] in jsonKeys:
    #             # print("gggg")
    #             jishu += 1
    #             #重入 算术溢出 时间攻击 未检查低乎
    #             tmpTaiList = [0,0,0,0]
    #             tmpJsonDict = jsonFile[nameList[i]]["tools"]["slither"]["categories"]
    #             # print(tmpJsonDict)
    #             if "reentrancy" in tmpJsonDict.keys() :
    #                 tmpTaiList[0] = 1
    #             # if "arithmetic" in tmpJsonDict.keys() :
    #             #     tmpTaiList[1] = 1
    #             if "time_manipulation" in tmpJsonDict.keys() :
    #                 tmpTaiList[2] = 1
    #             if "unchecked_low_calls" in tmpJsonDict.keys() :
    #                 tmpTaiList[3] = 1
    #             tmpJsonDict2 = jsonFile[nameList[i]]["tools"]["mythril"]["categories"]
    #             if "arithmetic" in tmpJsonDict.keys() :
    #                 tmpTaiList[1] = 1
    #             tmpAll = []
    #             tmpAll.append(nameList[i])
    #             for j in range(0,4):
    #                 tmpAll.append(tmpTaiList[j])
    #             # tmpAll.append(byteList[i])
    #             tmpAll.append(opList[i])
    #             g_csv.writerow(tmpAll)

    #重写逻辑
    jishu = 0
    err = 0
    for i in range(0,len(nameList)):
        if nameList[i] in jsonKeys:
            # print("gggg")
            jishu += 1
            if(jishu%1024==0):
                print(tmpOpCsv.shape)
            #重入 算术溢出 时间攻击 未检查低乎
            tmpTaiList = [0,0,0,0]
            tmpJsonDict = jsonFile[nameList[i]]["tools"]["slither"]["categories"]
            # print(tmpJsonDict)
            if "reentrancy" in tmpJsonDict.keys() :
                tmpTaiList[0] = 1
            if "time_manipulation" in tmpJsonDict.keys() :
                tmpTaiList[2] = 1
            if "unchecked_low_calls" in tmpJsonDict.keys() :
                tmpTaiList[3] = 1
            tmpJsonDict2 = jsonFile[nameList[i]]["tools"]["mythril"]["categories"]
            if "arithmetic" in tmpJsonDict2.keys() :
                tmpTaiList[1] = 1
            tmpAll = []
            tmpAll.append(nameList[i])
            for j in range(0,4):
                tmpAll.append(tmpTaiList[j])
            # tmpAll.append(byteList[i])
            tmpAll.append(opList[i])
            tmpOpCsv.loc[jishu-1] = tmpAll
        else:
            err += 1
    print(jishu,'err',err)
witeCsvPath = os.path.join("testresult", "testop0920.csv")
tmpOpCsv.to_csv(witeCsvPath, index=False)