import tkinter as tk
from tkinter import filedialog
from UnploadingMif import UnpackingMif
from UnploadingKPT import UnploadKPT
from UnploadingGeodezia import UnploadingGeodezia
from CreateMainData import StartPars
from Uploading_File import UploadingFile
from UploadingZu import UploadingZu

def open_directory(event, entry):
    directory_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory_path)
    
def open_directory_fin(event, entry):
    directory_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory_path)
    option_fin.clear()
    drop_var_fin.set("")
    menu_fin = additional_dropdown["menu"]
    menu_fin.delete(0, "end")
    menu_fin.add_command(label=option_fin, command=tk._setit(drop_var_fin, option_fin))

def open_excel_file(event, entry):
    excel_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, excel_path)
    
def geodez(event, entry):
    from UnploadingGeodezia import ReturnList
    
    excel_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, excel_path)
    
    options.clear()
    for result_list in ReturnList(path=excel_path):
        options.append(str(result_list))
    if  len(options)>0:
        drop_var.set(options[0])
        menu = dropdown["menu"]
        menu.delete(0, "end")
        # Добавляем новые варианты
        for option in options:
            menu.add_command(label=option, command=tk._setit(drop_var, option))
            
            
def Zu(event, entry):
    from UnploadingGeodezia import ReturnList
    
    excel_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, excel_path)
    
    options_zu.clear()
    for result_list in ReturnList(path=excel_path):
        options_zu.append(str(result_list))
    if  len(options)>0:
        drop_var_zu.set(options_zu[0])
        menu_zu = dropdown_zu["menu"]
        menu_zu.delete(0, "end")
        # Добавляем новые варианты
        for option in options_zu:
            menu_zu.add_command(label=option, command=tk._setit(drop_var_zu, option)) 
            
    
def fianly(event, entry):
    from UnploadingGeodezia import ReturnList
    
    excel_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, excel_path)
    
    option_fin.clear()
    option_fin.insert(0,"Создать нойвый лист")
    for result_list in ReturnList(path=excel_path):
        option_fin.append(str(result_list))
    if  len(option_fin)>0:
        drop_var_fin.set(option_fin[0])
        menu_fin = additional_dropdown["menu"]
        menu_fin.delete(0, "end")
        # Добавляем новые варианты
        for option in option_fin:
            menu_fin.add_command(label=option, command=tk._setit(drop_var_fin, option))


def Pars():
    if directory_entry.get() != "" and excel_entry.get() != "" and excel_entry2.get() != "" and radio_entry.get() != "":
        empty_button.config(state=tk.DISABLED)
        if UnpackingMif(path_directory=directory_entry.get()) == True: # MIF
            if UnploadKPT(path=excel_entry.get()) == True:
                if UnploadingGeodezia(path=excel_entry2.get(), _sheet=drop_var.get()): 
                    if UploadingZu(path=excel_entry3.get(), _sheet=drop_var_zu.get()):
                        if StartPars(err=err_text.get(), met=met_text.get()) == True:
                            if UploadingFile(path=radio_entry.get(), _sheet=drop_var_fin.get()):
                                empty_button.config(state=tk.NORMAL)
                                return
    empty_button.config(state=tk.NORMAL)
        
        
root = tk.Tk()
root.title("Parser2")

# Увеличиваем шрифт
font = ("Arial", 12)
root.configure(bg="#B85C38")
# Первое поле для выбора директории
directory_label = tk.Label(root, text="Выберите директорию с mif:", font=font)
directory_label.pack(anchor="w")
directory_entry = tk.Entry(root, font=font, width=70)
directory_entry.pack(anchor="w")
directory_entry.bind("<Button-1>", lambda event: open_directory(event, directory_entry))

# Второе поле для выбора файла XLSX
excel_label = tk.Label(root, text="КПТ:", font=font)
excel_label.pack(anchor="w")
excel_entry = tk.Entry(root, font=font, width=70)
excel_entry.pack(anchor="w")
excel_entry.bind("<Button-1>", lambda event: open_excel_file(event, excel_entry))

# Третье поле для еще одного файла XLSX
excel_label2 = tk.Label(root, text="Геодезия:", font=font)
excel_label2.pack(anchor="w")
excel_entry2 = tk.Entry(root, font=font, width=70)
excel_entry2.pack(anchor="w")
excel_entry2.bind("<Button-1>", lambda event: geodez(event, excel_entry2))

# Выпадающий список
options = [""]
drop_var=tk.StringVar()
dropdown = tk.OptionMenu(root, drop_var, *options)
dropdown.pack(anchor="w")

#четвертое поле для Зу
excel_label3 = tk.Label(root, text="Зу:", font=font)
excel_label3.pack(anchor="w")
excel_entry3 = tk.Entry(root, font=font, width=70)
excel_entry3.pack(anchor="w")
excel_entry3.bind("<Button-1>", lambda event: Zu(event, excel_entry3))

# Выпадающий список
options_zu = [""]
drop_var_zu=tk.StringVar()
dropdown_zu = tk.OptionMenu(root, drop_var_zu, *options_zu)
dropdown_zu.pack(anchor="w")


err_lab = tk.Label(root, text="погрешность", font=font)
err_lab.pack(anchor="w")
err_text = tk.Entry(root, font=font)
err_text.insert(tk.END, "1")
err_text.pack(anchor="w")

met_lab = tk.Label(root, text="метод определения", font=font)
met_lab.pack(anchor="w")
met_text = tk.Entry(root, font=font)
met_text.insert(tk.END, "картометрический метод")
met_text.pack(anchor="w")

# Радио кнопки для выбора директории или файла
radio_var = tk.IntVar()
radio_var.set(1)  # Сделаем первую радио кнопку активной
directory_radio = tk.Radiobutton(root, text="Выбрать директорию", variable=radio_var, value=1, font=font)
directory_radio.pack(anchor="w")
file_radio = tk.Radiobutton(root, text="Выбрать XLSX файл", variable=radio_var, value=2, font=font)
file_radio.pack(anchor="w")

# Текстовое поле для выбора директории или файла в зависимости от радио кнопки
radio_entry = tk.Entry(root, font=font, width=70)
radio_entry.pack(anchor="w")
radio_entry.bind("<Button-1>", lambda event: open_directory_fin(event, radio_entry) if radio_var.get() == 1 else fianly(event, radio_entry))

# Дополнительный выпадающий список
option_fin = [""]
drop_var_fin=tk.StringVar()
additional_dropdown = tk.OptionMenu(root, drop_var_fin, *option_fin)
additional_dropdown.pack(anchor="w")

# Кнопка с пустым методом
empty_button = tk.Button(root, text="->", command=Pars, font=font)
empty_button.pack(side="right", padx=10, pady=10)

root.mainloop()