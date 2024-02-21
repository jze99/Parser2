from flet import *
from main import Main
from UnploadingMif import UnploadingMif
from UnploadingKPT import UnploadKPT
from UnploadingGeodezia import UnploadingGeodezia
from CreateMainData import StartPars
from Uploading_File import UploadingFile

error_text = Text(
    size=45,
    value="Что то пошло не так"
)
    
def viewsHendler(page):
    
    main_page = Main(page=page)
    
    def Pars(e):
        if main_page.path_mif != "" and main_page.path_kpt != "" and main_page.path_geodez != "" and main_page.path_resul != "":
            page.go('/loding')
            if UnploadingMif(pathDirectori=main_page.path_mif) == True: # MIF
                if UnploadKPT(path=main_page.path_kpt) == True:
                    if UnploadingGeodezia(path=main_page.geodez_path_text.value, _sheet= main_page.list_geodez.value): 
                        if StartPars(err=main_page.error_rate_text.value, met=main_page.method_of_determination_text.value) == True:
                            if UploadingFile(path=main_page.path_resul, _sheet=main_page.list_result_file.value):
                                page.go('/')
                                return
            page.go('/er')
            
    def Beak(e):
        page.go('/')
    
    button_pars = FloatingActionButton(
            icon=icons.SKIP_NEXT_ROUNDED,
            bgcolor="#B85C38",
            on_click=Pars
        )
    
    button_beak = FloatingActionButton(
            icon=icons.ARROW_LEFT,
            bgcolor="#B85C38",
            on_click=Beak
        )
    
    return {
        '/':View(
            route='/', 
            bgcolor="#2D2424",
            scroll=True,
            padding=5,
            controls=[
                main_page,
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        button_pars
                    ]
                )
            ]
        ),
        '/loding':View(
            route='/loding', 
            bgcolor="#2D2424",
            controls=[
                Text(
                    value="Пожалуйста подождите",
                    size=45,
                )
            ]
        ),
        '/er':View(
            route='/er', 
            bgcolor="#2D2424",
            controls=[
                error_text,
                button_beak
            ]
        ),
    }