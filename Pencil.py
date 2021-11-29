# Get string length:

from typing import List

def strLen(str):
    upperCaseCount = 0;
    for i in str:  
        if(i>="A" and i<="Z"):
            upperCaseCount = upperCaseCount + 1;
    return upperCaseCount+len(str);


def getSpace(num):
    s= "";
    for i in range(0, num):
        s= s+" ";
    return s;

def getTextByCount(str, n):
    s= "";
    count = 0;
    for i in str:  
        if(i>="A" and i<="Z"):
            count += 2;
        else:
            count += 1;
        if(count <= n):
            s += i
        else:
            return s;
    return s;

currentLen = 0;
currentStr = "";
durability = 10;
def write(inputStr):
    global currentStr, currentLen
    # print(currentStr);
    inputLen = strLen(inputStr);
    # print("Input str = ", inputStr, "Input Len = ", inputLen);
    if(currentLen > durability):
        currentStr = currentStr + getSpace(inputLen);
    elif(currentLen + inputLen <= durability):
        currentStr = currentStr + inputStr
    else:
        balance = durability - currentLen
        partialText = getTextByCount(inputStr, balance)
        currentStr += partialText
        currentStr += getSpace(inputLen - balance)
    currentLen += inputLen    
    return currentStr

        
s = write("Hello")
print("s=", s, "/len=", currentLen)
s = write("Sathya")
print("s=", s, "/len=", currentLen)
s = write("to Herndon")
print("s=", s, "/len=", currentLen)



# Initial length of pencil is (j) = 10 cm.
# let i is the length after it got sharpened.

# for j in range(10, -1, -1):
#     for i in range(40000, 0, -1):
#         print(i);
#     print(j);





