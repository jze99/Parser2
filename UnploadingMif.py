import os
import re
import numpy as np
from Data import MifObject, NewMifCadObject


def UnploadingMif(pathDirectori: str):
    
    NewMifCadObject.clear()
    
    try:
        x=[]
        y=[]
        for filename in os.scandir(pathDirectori):
            if filename.name.endswith(".mif"):
                CadNumber = filename.name
                CadNumber = CadNumber.split(" ")
                if '_' in CadNumber[0]:
                    CadNumber = str(CadNumber[0])
                    CadNumber = CadNumber.replace("_", ":")
                else:
                    CadNumber = str(CadNumber[0]+":"+CadNumber[1]+":"+CadNumber[2]+":"+CadNumber[3])
                readMif(filename.path, x=x, y=y)
                NewMifCadObject.append(MifObject(CadNumber=CadNumber, x=x, y=y, square=Square(x,y)))
                x.clear()
                y.clear()
        if NewMifCadObject:        
            return True
        else:
            return False
    except FileNotFoundError:
        return False
            
def readMif(path: str, x, y):
    t=[]
    file = open(path)
    region = False
    for h in file:
        if 'Region' in h:
            region = True
            continue
        if region == True:
            t.append(h)
    t.pop(0)
    t.pop()
    t.pop()
    t.pop()
    for ch in t:
        ch = re.sub('[\n]', '', ch)
        ch=ch.split(" ")
        y.append(round(float(ch[0]),2))
        x.append(round(float(ch[1]),2))
        
def Square(x,y):
   return round(0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1))),0)
            