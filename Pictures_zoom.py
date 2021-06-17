# -*- coding: utf-8 -*-

import json
import os
import sys
from sys import path
import time

import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

# 定义赋值
define = {
    "define_set_zoom_value": 0,
    "define_set_width_and_height_value": 1
}


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi()
        self.Button_status()
        self.Users()

    def Users(self):
        # 在源地址运行进行和在其他的地址运行
        # #path = os.path.abspath(__file__)  #显示当前文件的地址
        try:
            path = os.path.dirname(__file__)  # 显示当前文件的地址

            self.fp = open('{}/user.json'.format(path), 'r+', encoding='utf-8')
            self.user = json.loads(self.fp.read())

        except FileNotFoundError:
            self.fp = open('./user.json', 'r+', encoding='utf-8')
            self.user = json.loads(self.fp.read())

        self.language = self.user["default"]['language']
        self.define_name = self.user['interface_name'][0][self.language][0]
        
        self.setWindowTitle(self.define_name['setWindowTitle'])
        self.select_file.setText(self.define_name['select_file'])
        self.select_folder.setText(self.define_name['select_folder'])
        self.do_task_pushButton.setText(self.define_name['go_task_pushButton'])
        self.cls_pushButton.setText(self.define_name['cls_pushButton'])
        self.set_value_zoom.setText(self.define_name['set_value_zoom'])
        self.set_value_height.setText(self.define_name['set_value_height'])
        self.set_value_width.setText(self.define_name['set_value_width'])
        self.label.setText(self.define_name['status'])
        self.value_height.setText(self.define_name['value_height'])
        self.value_width.setText(self.define_name['value_width'])
        self.value_zoom.setText(self.define_name['value_zoom'])
        self.language_button.setText(self.define_name['setlanguage'])
        self.set_default_height = self.user["default"]["height"]
        self.set_default_width = self.user["default"]["width"]
        self.value = self.user["dialog"][0][self.language][0]['value'] 
        self.input_error = self.user["dialog"][0][self.language][0]["input_error"] 

    def setupUi(self):
        self.resize(350, 300)
        self.setMinimumSize(350, 300)
        self.setMaximumSize(350, 300)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 180, 200))
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 220, 181, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.select_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_file.setObjectName("select_file")
        self.gridLayout.addWidget(self.select_file, 1, 0, 1, 1)
        self.select_folder = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_folder.setObjectName("select_folder")
        self.gridLayout.addWidget(self.select_folder, 1, 1, 1, 1)
        self.do_task_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.do_task_pushButton.setObjectName("do_task_pushButton")
        self.gridLayout.addWidget(self.do_task_pushButton, 2, 0, 1, 1)
        self.cls_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cls_pushButton.setObjectName("cls_pushButton")
        self.gridLayout.addWidget(self.cls_pushButton, 2, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 120, 77, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.set_value_zoom = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.set_value_zoom.setObjectName("set_value_zoom")
        self.verticalLayout.addWidget(self.set_value_zoom)
        self.set_value_height = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        self.set_value_height.setObjectName("set_value_height")
        self.verticalLayout.addWidget(self.set_value_height)
        self.set_value_width = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.set_value_width.setObjectName("set_value_width")
        self.verticalLayout.addWidget(self.set_value_width)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 120, 31, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.value_zoom = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.value_zoom.setAlignment(QtCore.Qt.AlignCenter)
        self.value_zoom.setObjectName("value_zoom")
        self.verticalLayout_2.addWidget(self.value_zoom)
        self.value_height = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.value_height.setTextFormat(QtCore.Qt.AutoText)
        self.value_height.setAlignment(QtCore.Qt.AlignCenter)
        self.value_height.setObjectName("value_height")
        self.verticalLayout_2.addWidget(self.value_height)
        self.value_width = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.value_width.setAlignment(QtCore.Qt.AlignCenter)
        self.value_width.setObjectName("value_width")
        self.verticalLayout_2.addWidget(self.value_width)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(200, 20, 150, 80))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.value_zoom.setText(" ")
        self.value_width.setText(" ")
        self.value_height.setText(" ")

        self.language_button = QtWidgets.QPushButton(self)
        self.language_button.setGeometry(QtCore.QRect(200, 222, 75, 25))
        self.language_button.setObjectName('set_language')
        QtCore.QMetaObject.connectSlotsByName(self)

    def Button_status(self):
        self.select_folder.setEnabled(1)  # folder select
        # self.language_button.setEnabled(0) #  language choose
        self.language_button.clicked.connect(self.set_language_clicked)
        self.do_task_pushButton.clicked.connect(self.GO_task)
        self.cls_pushButton.clicked.connect(self.cls_task)
        self.set_value_zoom.clicked.connect(self.set_zoom_button_clicked)
        self.set_value_height.clicked.connect(self.set_height_button_clicked)
        self.set_value_width.clicked.connect(self.set_width_button_clicked)
        self.select_file.clicked.connect(self.file_button_clicked)
        self.select_folder.clicked.connect(self.select_folder_clicked)

    # 处理前，即状态，根据状态进行判断，传递下面处理事件函数

    def GO_task(self):
        if self.value_zoom.text() != ' ':
            self.TASK(0)
            print(0)
        elif self.value_width.text() != ' ' and self.value_height.text() != ' ':
            print(1)
            self.TASK(1)
        else:
            set_width_height_or_zoom_value = self.user["dialog"][0][self.language][0]['set_width_height_or_zoom_value']
            QtWidgets.QMessageBox.information(self, '', set_width_height_or_zoom_value)

    # 处理时

    def TASK(self, index):
        Sized = ""
        out_list =[]
        # 判断是否缩放值，则多少
        if index == define["define_set_zoom_value"]:
            Sized = (float(self.value_zoom.text()))
        # 判断宽高度的多少
        elif index == define["define_set_width_and_height_value"]:
            Sized = (int(self.value_width.text()),
                     int(self.value_height.text()))

        print(Sized)
        # 抽取数据，列表
        lis = self.textEdit.toPlainText().split('\n')


        # print(lis)
        # 替换

        for i in range(0, len(lis)):
            if lis[i][-4:] == '.jpg':
                out_list.append(lis[i].replace('.jpg', '_out.jpg'))
            elif lis[i][-4:] == '.png':
                out_list.append(lis[i].replace('.png', '_out.png'))
            else:
                pass

        self.alter_size(lis, out_list, Sized, index)

    def alter_size(self, img, out, size, tastus):

        After_setting_the_size = self.user["dialog"][0][self.language][0]['After_setting_the_size'] 
        for i in range(0, len(img)):
            time.sleep(0.5)
            Img = Image.open(img[i])
            # set zoom
           
            if tastus == define["define_set_zoom_value"]:
                h = int(Img.height/size)
                w = int(Img.width/size)
                # 处理jpg
                if img[i][-3:] == 'jpg':
                    # print(h,w)
                    
                    self.label.setText(After_setting_the_size.format(w, h))
                    out_img = Img.resize((w, h), Image.ADAPTIVE)
                    out_img = out_img.convert('RGB')
                    Img.close()
                    out_img.save(out[i])
                # 处理png
                elif img[i][-3:] == 'png':
                    self.label.setText(After_setting_the_size.format(w, h))
                    out_img = Img.resize((w, h), Image.ADAPTIVE)
                    out_img = out_img.convert('RGBA')
                    Img.close()
                    out_img.save(out[i])

            # set the width and the height
            elif tastus == define["define_set_width_and_height_value"]:
                w = int(Img.width/size(0))
                h = int(Img.height/size(1))
                # 处理jpg
                if img[i][-3:] == 'jpg':
                    # print(h,w)
                    self.label.setText(After_setting_the_size.format(w, h))
                    out_img = Img.resize((w, h), Image.ADAPTIVE)
                    out_img = out_img.convert('RGB')
                    Img.close()
                    out_img.save(out[i])
                # 处理png
                elif img[i][-3:] == 'png':
                    self.label.setText(After_setting_the_size.format(w, h))
                    out_img = Img.resize((w, h), Image.ADAPTIVE)
                    out_img = out_img.convert('RGBA')
                    Img.close()
                    out_img.save(out[i])
            else:
                print("Unknown bug!")

    def cls_task(self):
        Cleaned_up = self.user["dialog"][0][self.language][0]['Cleaned_up'] 
        self.value_height.setText(' ')
        self.value_width.setText(' ')
        self.value_zoom.setText(' ')
        self.textEdit.clear()
        self.set_value_height.setEnabled(1)
        self.set_value_width.setEnabled(1)
        self.set_value_zoom.setEnabled(1)
        self.label.setText(Cleaned_up)

    def set_zoom_button_clicked(self):
        input_zoom_value = self.user["dialog"][0][self.language][0]['input_zoom_value'] 
        text, ok = QtWidgets.QInputDialog.getText(
            self, input_zoom_value, self.value, QtWidgets.QLineEdit.Normal, '')
        if ok:
            try:
                value_zoom = float(text)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, '', self.input_error)
            else:
                self.value_zoom.setText(str(value_zoom))
                self.reesh_setting(0)

    def set_height_button_clicked(self):
        input_height_value = self.user["dialog"][0][self.language][0]['input_height_value'] 
        text, ok = QtWidgets.QInputDialog.getText(
            self, input_height_value, self.value, QtWidgets.QLineEdit.Normal, '')
        if ok:
            try:
                value_height = int(text)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, '', self.input_error)
            else:
                self.value_height.setText(str(value_height))
                self.reesh_setting(1)

    def set_width_button_clicked(self):
        input_width_value = self.user["dialog"][0][self.language][0]['input_width_value'] 
        text, ok = QtWidgets.QInputDialog.getText(
            self, input_width_value, self.value, QtWidgets.QLineEdit.Normal, '')
        if ok:
            try:
                value_width = int(text)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, '', self.input_error)
            else:
                self.value_width.setText(str(value_width))
                self.reesh_setting(1)

    def reesh_setting(self, kind):
        Width_and_height_cannot_be_set = self.user["dialog"][0][self.language][0]['Width_and_height_cannot_be_set'] 
        zoom_cannot_be_set = self.user["dialog"][0][self.language][0]['zoom_cannot_be_set'] 

        if kind == 0:
            self.set_value_height.setEnabled(0)
            self.set_value_width.setEnabled(0)
            self.value_height.setText(' ')
            self.value_width.setText(' ')
            self.label.setText(Width_and_height_cannot_be_set)
        elif kind == 1:
            self.set_value_zoom.setEnabled(0)
            self.value_zoom.setText(' ')
            self.label.setText(zoom_cannot_be_set)
    def select_folder_clicked(self):
        self.foldername =QtWidgets.QFileDialog.getExistingDirectory(self,"选择文件夹",'/')
        print(self.foldername)
        imgs_path =[]
        out_list=[]
        for i in os.listdir(self.foldername):
            imgs_path.append(self.foldername+'/'+i)
            # self.textEdit.append(self.foldername+'/'+i+'\n')
            # lis = self.foldername+'/'+i
        print(imgs_path)
        for i in range(0,len(imgs_path)):
            if imgs_path[i][-4:] == '.JPG':
                out_list.append(imgs_path[i].replace('.JPG', '_out.jpg'))
           
        
        size = 13.44
        for i in range(0, len(imgs_path)):
            Img = Image.open(imgs_path[i])
            # set zoom
            h = int(Img.height/size)
            w = int(Img.width/size)
 
            out_img = Img.resize((w, h), Image.ADAPTIVE)
            out_img = out_img.convert('RGB')
            Img.close()
            out_img.save(out_list[i])


    def file_button_clicked(self):
        
        self.filename, ok = QtWidgets.QFileDialog.getOpenFileName(self, self.user['interface_name'][0][self.language][0]['select_file'],
                                                                  filter='ALL FILES(*.*);;JPEG Files(*.jpg);;PNG Files(*.png)')
        if ok:
            self.img = self.get_image_size(self.filename)
            if self.img == 'error':
                image_format = self.user["dialog"][0][self.language][0]['image_format'] 
                self.label.setText(image_format)
            # print(s.size) # 元组
            # print(s.mode) # 模式
            # print(s.format) # 原格式
            # print(s.width, s.height) # 宽度、高度
            else:

                self.textEdit.append(self.filename)
                
                pic_info_log = self.user["dialog"][0][self.language][0]['pic_info_log']                
                label_status = pic_info_log.format(str(self.img.size), str(self.img.mode),
                                                                             str(self.img.format))
                self.label.setText(label_status)

    def get_image_size(self, path):
        try:
            im = Image.open(path)
            return im
        except:
            return 'error'

    # 设置语言
    def set_language_clicked(self):
        Enter_serial_number = self.user["dialog"][0][self.language][0]['Enter_serial_number'] 
        current_language_list = self.user["dialog"][0][self.language][0]['current_language_list'] 
        It_is_No_configuration_required = self.user["dialog"][0][self.language][0]['It_is_No_configuration_required'] 
        input_out_of_range = self.user["dialog"][0][self.language][0]['input_out_of_range'] 
        Illegal_grammar = self.user["dialog"][0][self.language][0]['Illegal_grammar'] 
        tmp = self.user["default"]['language']
        text, ok = QtWidgets.QInputDialog.getText(
            self, Enter_serial_number, current_language_list, QtWidgets.QLineEdit.Normal, '')
        if ok:
            try:
                value_language = int(text)
                if value_language == 0:
                    if self.language == "ZH":
                        self.label.setText(It_is_No_configuration_required.format(tmp))
                    else:
                        self.user["default"]['language'] = "ZH"
                        self.fp.seek(0)  # rewind
                        json.dump(self.user, self.fp, ensure_ascii=False)
                        self.fp.truncate()
                        self.restrat_program()
                        print("ZH")
                    print(value_language)
                elif value_language == 1:
                    if self.language == "English":
                        self.label.setText(It_is_No_configuration_required.format(tmp))
                    else:
                        self.user["default"]['language'] = "English"
                        self.fp.seek(0)  # rewind
                        json.dump(self.user, self.fp, ensure_ascii=False)
                        self.fp.truncate()
                        print("English")
                        self.restrat_program()
                    print(value_language)
                    
                else:
                    QtWidgets.QMessageBox.warning(
                        self, self.input_error, input_out_of_range)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, self.input_error, Illegal_grammar)

    # 重启程序，加载
    def restrat_program(self):
        QtWidgets.QMessageBox.information(self, 'Please wait a moment', 'Restart program')
        python = sys.executable
        os.execl(python, python, * sys.argv)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    uf = Ui_Form()
    uf.show()
    sys.exit(app.exec_())
