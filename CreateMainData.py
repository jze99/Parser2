from Data import NewGeodesyObject, NewKPTCadObject, NewMifCadObject, NewSuperObject, SuperObjet, NewZuObject

def ParsingMif():
    
    NewSuperObject.clear()
    
    for mif in NewMifCadObject:
        obj = SuperObjet()
        obj.AddMif(
            CadNumber=mif.CadNumber,
            x=mif.x,
            y=mif.y,
            square_mif=mif.square
        )
        NewSuperObject.append(
            obj
        )
    return True
        
def ParsingKPT():
    for sup in NewSuperObject:
        kpt_obj = next(filter(lambda kpt: str(kpt.CadNumber) == str(sup.CadNumber), NewKPTCadObject), None)
        if kpt_obj == None:
            sup.AddKPT(
                type_of_object="данные отсутствуют",
                error_determining_area="данные отсутствуют",
                presence_coordinates="данные отсутствуют",
                point_number="данные отсутствуют",
                error_rate="данные отсутствуют",
                method_determining_point="данные отсутствуют",
                source=None,
                square_kpt="данные отсутствуют",
                x="данные отсутствуют",
                y="данные отсутствуют"
            )
        if kpt_obj != None:
            if str(kpt_obj.CadNumber) == str(sup.CadNumber):
                sup.AddKPT(
                    type_of_object=kpt_obj.type_of_object,
                    error_determining_area=kpt_obj.error_determining_area,
                    presence_coordinates=kpt_obj.presence_coordinates,
                    point_number=kpt_obj.point_number,
                    error_rate=kpt_obj.error_rate,
                    method_determining_point=kpt_obj.method_determining_point,
                    source=kpt_obj.source,
                    square_kpt=kpt_obj.square,
                    x=kpt_obj.x,
                    y=kpt_obj.y
                )
    return True

def EGRNCycle(sup, xmif, ixmif):
    for kpt in NewKPTCadObject:
        for ixkpt, xkpt in enumerate(kpt.x):
            if str(xmif) == str(xkpt) and str(sup.y_mif[ixmif]) == str(kpt.y[ixkpt]) and str(sup.CadNumber) == str(kpt.CadNumber):
                sup.AddFinalyRow(
                    number_row=kpt.point_number[ixkpt],
                    x=float(xkpt),
                    y=float(kpt.y[ixkpt]),
                    error_rate=kpt.error_rate[ixkpt],
                    method_determining_point=kpt.method_determining_point[ixkpt],
                    source="ЕГРН"
                )
                
                return False
    return True

def KPTCycle(sup, xmif, ixmif):
    related = False
    for kpt in NewKPTCadObject:
        for ixkpt, xkpt in enumerate(kpt.x):
            if str(xmif) == str(xkpt) and str(sup.y_mif[ixmif]) == str(kpt.y[ixkpt]) and related == False:
                sup.AddFinalyRow(
                    number_row=kpt.point_number[ixkpt],
                    x=float(xkpt),
                    y=float(kpt.y[ixkpt]),
                    error_rate=kpt.error_rate[ixkpt],
                    method_determining_point=kpt.method_determining_point[ixkpt],
                    source="КПТ"
                )
                related = True
                
            if str(xmif) == str(xkpt) and str(sup.y_mif[ixmif]) == str(kpt.y[ixkpt]) and related == True:
                sup.finaly_row[ixmif].AddAdjacentCodastres(kpt.CadNumber)
                
    if related == True:
        return False 
    else:
        return True
    
    

def GEOCycle(sup, xmif, ixmif):
    for geo in NewGeodesyObject:      
        if str(xmif) == str(geo.x) and str(sup.y_mif[ixmif]) == str(geo.y):
            sup.AddFinalyRow(
                number_row=None,
                x=geo.x,
                y=geo.y,
                error_rate=geo.errorRate,
                method_determining_point=geo.methodDetermination,
                source=geo.source
            )
            return False
    return True



def CycleSuper(err:str, met:str):
    for isup, sup in enumerate(NewSuperObject):
        for ixmif, xmif in enumerate(sup.x_mif):
            if EGRNCycle(sup, xmif, ixmif):
                if KPTCycle(sup, xmif, ixmif):
                    if GEOCycle(sup, xmif, ixmif):
                        sup.AddFinalyRow(
                            number_row=None,
                            x=xmif,
                            y=sup.y_mif[ixmif],
                            error_rate=err,
                            method_determining_point=met,
                            source=""
                        )
                
    return True


def AddZu():
    for zuObj in NewZuObject:
        for sup in NewSuperObject:
            if zuObj.zu == sup.CadNumber:
                sup.AddOks(zuObj.oks)
    return True
    

def StartPars(err:str, met:str):
    if ParsingMif() == True:
        if ParsingKPT() == True:
            if AddZu() == True:
                if CycleSuper(err=err, met=met) == True:
                    return True
            
    