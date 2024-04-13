import openpyxl
from Data import ZuObject, NewZuObject

def UploadingZu(path:str, _sheet:str):
    
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[_sheet]
    
    rows = sheet.iter_rows(values_only=True)
    next(rows)
    
    NewZuObject.clear()
    
    for row in rows:
        if row[0] == None:
            workbook.close()
            return True
        NewZuObject.append(
            ZuObject(
                zu=row[1],
                oks=row[3]
            )
        )
        
    return True