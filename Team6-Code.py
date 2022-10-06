import makeDictionary
import random
def Code(txtFile):
    myTxtFile = open(txtFile)
    randomNum = random.randint(1,5)
    myStr = myTxtFile.read()
    asciiList = []
    binaryList = []
    for i in myStr:
        asciiList.append(ord(i))
    for i in asciiList:
        binaryList.append(str(int(bin(i)[2:])))
    binaryStr = ''.join(binaryList)
    myDec = 0
    myKey = makeDictionary.getCodeMap('Char2Bin')
    for i in myStr:
        temp = str(myKey.get(i))
        print("temp:",temp)
        myDec = str(myDec)
        myDec = bin(int(myDec,2) + int(temp,2))[2:]
    myDec = int(myDec,2)
    myDecStr = str(myDec)
    myOutput = myDecStr+"."+binaryStr
    out_file = open('bin_output.txt','w+')
    out_file.write(myOutput)
    print("word:",myStr)
    print("Decimal val:", myDecStr)
    print("Binary val:", binaryStr)
    print(myOutput)

Code("sample.txt")



