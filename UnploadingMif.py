import os
import re
import numpy as np
from Data import MifObject, NewMifCadObject

def transform_data(item):
    numbers = []
    count = 0
    for sub_item in item:
        if count >= 4:
            break
        if isinstance(sub_item, str):
            sub_item = sub_item.replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("_", ":").replace("mif", "")
            if sub_item.isdigit():
                numbers.append(sub_item)
                count += 1
            elif ":" in sub_item:
                numbers.extend(sub_item.split(":"))
                count += len(sub_item.split(":"))
        elif isinstance(sub_item, int):
            numbers.append(str(sub_item))
            count += 1
    result = ":".join(numbers)
    return result

def clear_list(lst):
    lst.clear()

def UnpackingMif(path_directory: str):
    NewMifCadObject.clear()
    try:
        x, y = [], []
        for filename in os.scandir(path_directory):
            if filename.name.endswith(".mif"):
                cad_number = filename.name.split(" ")
                cad_number = transform_data(cad_number)
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
            if check_float(ch[0]) and check_float(ch[1]):   
                y.append(round(float(ch[0]), 2))
                x.append(round(float(ch[1]), 2))
            else:
                continue

def Square(x, y):
    return round(0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))), 0)

def check_float(var):
    try:
        float(var)
    except ValueError:
        return False
    return True