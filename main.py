from flet import *

class Main(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.path_kpt = ""
        self.path_mif = ""
        self.path_geodez = ""
        self.path_resul = ""
        
        self.activ_read = False
        
        self.filePickerMif = FilePicker(on_result=self.OnDialogResultMIFPath)
        self.page.overlay.append(self.filePickerMif)
        
        self.mif_path_text = TextField(
            label="MIF директория",
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=14,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerMif.get_directory_path(),
        )
        self.button_mif_path = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=40,
            style=ButtonStyle(
                color="#B85C38",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=lambda _: self.filePickerMif.get_directory_path(),
        )

        self.filePickerKPT = FilePicker(on_result=self.OnDialogResultKPTPath)
        self.page.overlay.append(self.filePickerKPT)
        
        self.kpt_path_text = TextField(
            label="KPT документ",
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=14,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerKPT.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        self.button_kpt_path = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=40,
            style=ButtonStyle(
                color="#B85C38",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=lambda _: self.filePickerKPT.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        
        self.filePickerGeodez = FilePicker(on_result=self.OnDialogResultGeodezPath)
        self.page.overlay.append(self.filePickerGeodez)
        
        self.geodez_path_text = TextField(
            label="документ геодезии",
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=14,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerGeodez.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        self.button_geodez_path = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=40,
            style=ButtonStyle(
                color="#B85C38",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=lambda _: self.filePickerGeodez.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        
        self.list_geodez = Dropdown(
            label = "лист геодезии",
            border_color = "#F05941",
            expand=1,
            text_size=14
        )
        
        self.error_rate_text = TextField(
            label="погрешность",
            width=200,
            border_color="#B85C38",
            value="1",
            dense=True,
            text_size=14,
            multiline=False,
            text_style=TextStyle(
                color="#E0C097",
            ),
        )
        
        self.method_of_determination_text = TextField(
            label="метод определения",
            width=200,
            border_color="#B85C38",
            value="картометрический метод",
            text_size=14,
            expand=1,
            dense=True,
            multiline=False,
            text_style=TextStyle(
                color="#E0C097",
            ),
        )
        
        self.filePickerResult = FilePicker(on_result=self.OnDialogResultResultPath)
        self.page.overlay.append(self.filePickerResult)
        
        self.path_new_file_text = TextField(
            label="путь файла",
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=14,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerResult.pick_files(
                allow_multiple=False,
                allowed_extensions=["xlsx"]
            )
        )
        
        self.filePickerDirectory = FilePicker(on_result=self.OnDialogResultDirectoryPath)
        self.page.overlay.append(self.filePickerDirectory)
        
        self.directory_new_file_text = TextField(
            label="директория нового файла",
            width=300,
            border_color="#B85C38",
            read_only=True,
            value="",
            text_size=14,
            multiline=False,
            expand=1,
            text_style=TextStyle(
                color="#E0C097",
            ),
            dense=True,
            on_focus=lambda _: self.filePickerDirectory.get_directory_path(),
        )
        
        self.finally_File = RadioGroup(
            on_change=self.SelectFinallyFile,
            content=Row(
                controls=[
                Radio(value="1", label="Сохранить в существующий",fill_color="#B85C38"),
                Radio(value="2", label="Создать новый",fill_color="#B85C38"),
                ]
            ),
            value="1",
        )
        
        self.row_text_reslt = Row(
            controls=[
                self.path_new_file_text,
            ]
        )
        
        self.list_result_file = Dropdown(
            label = "лист геодезии",
            border_color = "#F05941",
            expand=1,
            text_size=14
        )
        
    def OnDialogResultMIFPath(self, e: FilePickerResultEvent):
        if e.path == None:
            return
        value_path=e.path
        self.mif_path_text.value = value_path
        self.path_mif = value_path
        self.mif_path_text.update()
        
    def OnDialogResultKPTPath(self, e: FilePickerResultEvent):
        if e.files == None:
            return
        value_path=e.files[0].path
        self.kpt_path_text.value = value_path
        self.path_kpt = value_path
        self.kpt_path_text.update()
    
    def OnDialogResultGeodezPath(self, e: FilePickerResultEvent):
        from UnploadingGeodezia import ReturnList
        self.list_geodez.options.clear()
        if e.files == None:
            return
        value_path=e.files[0].path
        self.geodez_path_text.value = value_path
        self.list_geodez.update()
        self.path_geodez = value_path
        self.geodez_path_text.update()
    
    def OnDialogResultResultPath(self, e: FilePickerResultEvent):
        try:
            
            if self.activ_read == False:
            
                from Uploading_File import ReturnList
                
                self.list_result_file.options.clear()
                self.list_result_file.options.append(dropdown.Option(str("Создать нойвый лист")))
                self.list_result_file.value = self.list_result_file.options[0].key
                
                if e.files == None:
                    return
                value_path=e.files[0].path
                self.path_new_file_text.value = value_path

                self.activ_read = True

                for result_list in ReturnList(path=value_path):
                    self.list_result_file.options.append(dropdown.Option(str(result_list)))
                
                self.list_result_file.update()
                self.path_resul = value_path
                self.path_new_file_text.update()

                self.activ_read = False
            
        except AssertionError:
            return
        
    
    def OnDialogResultDirectoryPath(self, e: FilePickerResultEvent):
        if e.path == None:
            return
        value_path=e.path
        self.directory_new_file_text.value = value_path
        self.path_resul = value_path
        self.directory_new_file_text.update()
    
    def SelectFinallyFile(self, e):
        if self.finally_File.value == "1":
            self.row_text_reslt.controls = [self.path_new_file_text]
            self.list_result_file.visible = True
            self.list_result_file.update()
        if self.finally_File.value == "2":
            self.row_text_reslt.controls = [self.directory_new_file_text]
            self.list_result_file.visible = False
            self.list_result_file.update()
        self.row_text_reslt.update()
    
    def build(self):
        return Column(
      controls=[
            Row(
                controls=[
                  self.mif_path_text,
                  self.button_mif_path
              ]
            ),
            Row(
                controls=[
                    self.kpt_path_text,
                    self.button_kpt_path
                ]
            ),
            Row(
                controls=[
                    self.geodez_path_text,
                    self.button_geodez_path
                ]
            ),
            Row(
                controls=[
                    self.list_geodez
                ]
            ),
            Row(
                controls=[
                    Text(
                        value="Параметры не найденых файлов",
                        size=20
                    )
                ]
            ),
            Row(
                controls=[
                    self.error_rate_text,
                    self.method_of_determination_text
                ]
            ),
            Row(
                controls=[
                    Text(
                        value="Параметры выгрузки данных",
                        size=20
                    )
                ]
            ),
            Row(
                controls=[
                    self.finally_File
                ]  
            ),
            self.row_text_reslt,
            Row(
                controls=[
                    self.list_result_file
                ]
            )
        ],
    )
        
