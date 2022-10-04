import makeDictionary
import random
def Code(txtFile):
    myTxtFile = open(txtFile)
    randomNum = random.randint(0,3)
    myStr = myTxtFile.readline(randomNum)
    asciiList = []
    binaryList = []
    for i in myStr:
        asciiList.append(ord(i))
    for i in asciiList:
        binaryList.append(str(int(bin(i)[2:])))
    binaryStr = ''.join(binaryList)
    myDec = []
    myKey = makeDictionary.getCodeMap('Char2Bin')
    for i in myStr:
        myDec.append(str(myKey.get(i)))
    myDecStr = ''.join(myDec)
    myOutput = myDecStr+"."+binaryStr
    out_file = open('bin_output.txt','w+')
    out_file.write(myOutput)
    print("word:",myStr)
    print("Decimal val:", myDecStr)
    print("Binary val:", binaryStr)
    print(myOutput)

Code("sample.txt")



