import os
import re
import numpy as np
from Data import MifObject, NewMifCadObject

def unpack_cad_number(cad_number_parts):
    if '_' in cad_number_parts[0]:
        cad_number = cad_number_parts[0].replace("_", ":")
    else:
        cad_number = ":".join(cad_number_parts[:4]).replace(".mif", "")
    return cad_number

def clear_list(lst):
    lst.clear()

def UnpackingMif(path_directory: str):
    NewMifCadObject.clear()
    try:
        x, y = [], []
        for filename in os.scandir(path_directory):
            if filename.name.endswith(".mif"):
                cad_number = filename.name.split(" ")
                cad_number = unpack_cad_number(cad_number)
                readMif(filename.path, x, y)
                NewMifCadObject.append(MifObject(CadNumber=cad_number, x=x.copy(), y=y.copy(), square=Square(x, y)))
                clear_list(x)
                clear_list(y)
        return bool(NewMifCadObject)
    except FileNotFoundError:
        return False
        
def readMif(path: str, x, y):
    with open(path) as file:
        t = []
        region = False
        for line in file:
            if 'Region' in line:
                region = True
                continue
            if region:
                t.append(line)
        t = t[1:-3]
        for ch in t:
            ch = re.sub('[\n]', '', ch)
            ch = ch.split(" ")
            y.append(round(float(ch[0]), 2))
            x.append(round(float(ch[1]), 2))

def Square(x, y):
    return round(0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))), 0)