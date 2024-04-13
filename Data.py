class MifObject:
    def __init__(self, CadNumber:str, x, y, square):
        self.CadNumber = CadNumber
        self.x = x.copy()
        self.y = y.copy()
        self.square = square
        
class RowFinaly():
    
    def __init__(self, number_row, x, y, error_rate,
                 method_determining_point, source):
        self.number_row = number_row
        self.x = x
        self.y = y
        self.error_rate = error_rate
        self.method_determining_point = method_determining_point
        self.source = source
        self.adjacent_codastres=[]
        
    def AddAdjacentCodastres(self, cad:str):
        self.adjacent_codastres.append(cad)

class KPTCadObject():
    def __init__(self, CadNumber, type_of_object, square, error_determining_area, presence_coordinates):
        self.CadNumber = CadNumber # кадастровый номер
        self.type_of_object = type_of_object # вид объекта 
        self.square = square # площадь
        self.error_determining_area = error_determining_area # Погрешность определения площади
        self.presence_coordinates = presence_coordinates # Наличие координат
        
        self.point_number = [] # номер точки
        self.x = [] # x
        self.y = [] # y
        self.error_rate = [] # погрешность
        self.method_determining_point = [] # метод определения точки
        self.source = [] # источник
        
    def AddData(self, point_number = 0, x = 0, y = 0, error_rate = 0, method_determining_point=0, source=0):
        self.point_number.append(point_number) # номер точки
        self.x.append(x) # x
        self.y.append(y) # y
        self.error_rate.append(error_rate) # погрешность
        self.method_determining_point.append(method_determining_point) # метод определения точки
        self.source.append(source) # источник 
    
class GeodesyObject:
    def __init__(self, x, y, errorRate, methodDetermination, source):
        self.x=x
        self.y=y
        self.errorRate=errorRate
        self.methodDetermination=methodDetermination
        self.source=source
        
class SuperObjet():
    def __init__(self):
        self.CadNumber = None # кадастровый номер
        self.type_of_object = None # вид объекта 
        self.square_mif = None # площадь mif
        self.square_kpt = None # площадь kpt
        self.error_determining_area = None # Погрешность определения площади
        self.presence_coordinates = None # Наличие координат
        self.deviations = None # отклонение площади
        
        self.point_number = [] # номер точки
        
        self.x_mif = [] # x из миф файла
        self.y_mif = [] # y из миф файла
        
        self.x_kpt = [] # х из кпт файла
        self.y_kpt = [] # y из кпт файда
        
        self.error_rate = [] # погрешность
        self.method_determining_point = [] # метод определения точки
        self.source = [] # источник
        self.finaly_row = []
        
        self.oks=[]

    def AddOks(self, oks:str):
        self.oks.append(oks)

    def AddMif(self, CadNumber, x, y, square_mif):
        self.CadNumber = CadNumber # кадастровый номер
        self.x_mif = x
        self.y_mif = y
        self.square_mif = square_mif # площадь
        
    def AddKPT(self, type_of_object, error_determining_area = 0, presence_coordinates = 0, point_number = 0,
               error_rate = 0, method_determining_point= 0, square_kpt = None, x = 0, y = 0, source=""):
        self.type_of_object =type_of_object # вид объекта 
        self.error_determining_area = error_determining_area # Погрешность определения площади
        self.presence_coordinates = presence_coordinates
        self.point_number = point_number
        self.error_rate = error_rate
        self.method_determining_point = method_determining_point
        self.square_kpt = square_kpt
        self.x_kpt = x
        self.y_kpt = y
        self.deviations = self.Deviations()
        self.source = source

    def AddFinalyRow(self, number_row, x, y, error_rate, 
                     method_determining_point, source):
        self.finaly_row.append(
            RowFinaly(
                number_row=number_row, 
                x=x,
                y=y,
                error_rate=error_rate,
                method_determining_point=method_determining_point,
                source=source
            )
        )
    
    def Deviations(self):
        if self.square_kpt != None and self.square_mif != None and self.square_kpt != 'данные отсутствуют':
            return round((float(self.square_mif)/float(self.square_kpt))*100-100, 2)
        else:
            return "данные отсутствуют"
        
        
class ZuObject():
    def __init__(self, zu, oks):
        self.zu = zu
        self.oks = oks
    

NewMifCadObject = []

NewKPTCadObject = []

NewGeodesyObject = []

NewSuperObject = []

NewZuObject = []