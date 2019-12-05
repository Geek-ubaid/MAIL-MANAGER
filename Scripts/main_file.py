import csv
from PyQt5 import QtGui,QtWidgets,QtCore
from GUI.login import Ui_loginwindow
from GUI.mail_window import Ui_MainWindow
from GUI.popup_win import Ui_popup
from GUI.popup_msg import Ui_message_box
import mailto
import sqlite3
import pandas as pd
from pretty_form import *
from read_message import *
from list_messages import *
from read_message import *
from insert import *
import create_db

class Popupwin(QtWidgets.QDialog,Ui_popup):
    global df1
    def __init__(self,df1=pd.DataFrame(),parent=None):
        super(Popupwin, self).__init__(parent)
        self._df1 = df1
        self.setupUi(self)
        self.goback.pressed.connect(self.closeevent)
        model = PandasModel(self._df1)
        self.popup_view.setModel(model)
    def closeevent(self):
        self.close()

class Popupmsg(QtWidgets.QDialog,Ui_message_box):
    def __init__(self,mail="",parent=None):
        super(Popupmsg, self).__init__(parent)
        self.setupUi(self)
        self.goback.pressed.connect(self.closeevent)
        self.messagebox.setText(mail)
     
    def closeevent(self):
        self.close()
class Loginwindow(QtWidgets.QDialog,Ui_loginwindow):

    def __init__(self,parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowTitle("Mail Manager")
        self.login.clicked.connect(self.logincheck)
        self.reset.clicked.connect(self.resetcheck)


    def logincheck(self):
        passget = self.pass_input.text()
        userget = self.user.text()
        if (userget == "rudranshuganjoo@gmail.com" and passget == "rudransh"):
            self.window= Automater(self)
            self.close()
            self.window.show()
            # try:
            #     if(showmessagebox(11) == ok):
            #         pass          
            # except:
            #     pass

        else:
            if(showmessagebox(1) == Close):
                if(showmessagebox(4) == Yes):
                    print(3)
                    sys.exit()
                else:
                    pass
    def resetcheck(self):
        self.passw.setText("")
        self.user.setText("")

Yes=QtWidgets.QMessageBox.Yes
ok=QtWidgets.QMessageBox.Ok
Close=QtWidgets.QMessageBox.Close
    
def showmessagebox(x):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Status Window")
    msg.setIcon(QtWidgets.QMessageBox.Information)
    if x == 1:
        msg.setText('Invalid Credentials')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
    elif x == 2:
        msg.setText('Erorr in login!!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 3:
        msg.setText('Contacts Extracted!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 4:
        msg.setText('Are you sure you wanna exit?')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    elif x == 5:
        msg.setText('File no longer exists!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 6:
        msg.setText('Size of file exceeded! Select another file')
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 7:
        msg.setText('All Mail sent successfully')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 8:
        msg.setText('Invalid Input')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 9:
        msg.setText('Unable to read Message')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 10:
        msg.setText('Record Not Found')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 11:
        msg.setText('Welcome to MAIL MANAGER')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 12:
        msg.setText('Update Succesfuly')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 13:
        msg.setText('Error Updating')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
    return msg.exec_()
    


class Automater(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Automater, self).__init__(parent)
        self.setupUi(self)
        self.filePath = False
        self.setWindowIcon(QtGui.QIcon(r'logo.png'))
        self.setWindowTitle("Mail Manager")
        self.extract_Email_recipients.clicked.connect(self.Email_extract)
        self.search.clicked.connect(self.search_mail)
        self.folder_stats.pressed.connect(self.show_stat)
        self.show_all.pressed.connect(self.showall)
        self.update.pressed.connect(self.update_all)
        self.read_button.clicked.connect(self.read_mail)
        self.attachment.clicked.connect(self.open_file)
        self.send_Email.clicked.connect(self.sendmail)
        self.folders_list.activated[str].connect(self.view_folder)
        self.tableView.doubleClicked.connect(self.attach_stats)
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.closeEvent)
        

    def closeEvent(self, event):
        close=showmessagebox(4)
        if close == Yes:
            event.accept()
        else:
            event.ignore()
            self.close()
            self.window = Automater()
            self.window.show()

    def open_file(self):
        
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File to upload", "","All Files;; JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);;Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)", options=options)
        print(self.filePath)
        try:
            file_size=os.path.getsize(self.filePath)
            if (file_size> 26214400):
                showmessagebox(6)
                self.close()
            else:
                self.file_name = self.filePath.split("/")[-1]
                print("file attached")
        except:
            pass


    def Email_extract(self):
        mail_rec = self.recipients_Email.text()
        if (("." in mail_rec) and (mail_rec.split(".")[1] == "txt") ):
            with open(mail_rec, "r") as file:
                self.email_id={}
                for i in file.readlines():
                    l = i.split(" ")
                    self.email_id[l[2].strip()] = (l[0].strip(), l[1].strip())

                try:
                    if(showmessagebox(3) == ok):
                        pass
                        
                except:
                    pass

        else:
            print("wrong file")
            try:
                if(showmessagebox(5) == ok):
                    self.close()
            except:
                pass

    
    def sendmail(self):
        try:
            sub = self.subject.text()        
        except:
            print("Subject Not passed")
        msg = self.message_Email.toPlainText()
        sender="rudranshuganjoo@gmail.com"
        print(self.email_id)
        for i in self.email_id.keys():
            data={"name":self.email_id[i][0],"regno":self.email_id[i][1]}

            try:
                message = mailto.gen_message(data["name"],data["regno"],msg,"Ubaid")
                print(message)
              
                mailto.email(sender,i,message,sub,self.filePath)
               


                if(showmessagebox(7)==ok):
                    pass
            except:
                print("mail not sent")
       
    def showall(self):
        df = pd.read_excel("message.xlsx","Sheet1")
        df = pretty_format(df)
        df = df.loc[:,['MID','Subject','Date','Time','From','From_Name','Label1','Attachment','Snippet']]
        df.sort_index(by='Date',ascending=False,inplace=True)
        df.reset_index(inplace=True)
        del df['index']
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.clicked.connect(self.get_cell_Value)


    def show_stat(self):
        db = sqlite3.connect("Mailing.db")
        df1 = pd.read_sql_query("SELECT * FROM Folder", db)
        
        stat_table = Popupwin(df1)
        stat_table.exec_()
        db.close()

    def attach_stats(self):
        db = sqlite3.connect("Mailing.db")
        df1 = pd.read_sql_query("SELECT * FROM Attach", db)
        df1 = df1.loc[df1['MID'] == self.message_id]
        del df1['index']
        del df1['level_0']
        df1.index = range(len(df1))
        stat_table = Popupwin(df1)
        stat_table.exec_()
        db.close()
        
    def update_all(self):
        try:
            self.completed = 0
            list_message()
            df = update()
            print(df)
##            df = pd.read_excel("message.xlsx","Sheet1")
##            df = df.drop_duplicates(keep='first')
            print(2)
            while self.completed < 100:
                self.completed += 0.0001
                self.progressBar.setValue(self.completed)
            print(1)
            try:
                showmessagebox(12)
                return
            except:
                return
          
        except:
            showmessagebox(13)
            
        
        
    def read_mail(self):
        try:
            text_db = pd.read_excel("text.xlsx","Sheet1")
            print(text_db.columns)
            text = text_db.loc[text_db['MID'] == self.message_id]['Message'].str.strip().values[0]
            print(2)
            mail = text.replace('\\n','\n')
            win = Popupmsg(mail)
            win.exec_()
        except:
            try:
                if(showmessagebox(9) == ok):
                    pass
                        
            except:
                pass
            
    def search_mail(self):
        query = self.users_number.text()
        df = pd.read_excel("message.xlsx","Sheet1")
        df = pretty_format(df)
        df = df[df['From_Name'].str.lower().str.contains(query)]
        df = df.loc[:,['MID','Subject','Date','Time','From','From_Name','Label1','Attachment']]
        df.sort_index(by='Date',ascending=False,inplace=True)
        df.reset_index(inplace=True)
        del df['index']
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.clicked.connect(self.get_cell_Value)
      
        
        
    def get_cell_Value(self,index):
        self.message_id =  index.data()
        print(self.message_id)

    def view_folder(self,text):
        df = pd.read_excel("message.xlsx","Sheet1")
        df = pretty_format(df)
        df = df.loc[:,['MID','Subject','Date','Time','From','From_Name','Label1','Attachment']]
        try:
            df = df.loc[df['Label1']==text]
            df = df.reset_index()
            del df['index']
            model = PandasModel(df)
            self.tableView.setModel(model)
        except:
            try:
                if(showmessagebox(10) == ok):
                    pass          
            except:
                pass
  
class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()
        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


if __name__ == '__main__':
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    window= Loginwindow()
    window.show()
    import os.path
    if(os.path.isfile('Mailing.db')):
        print('DB exists')

    else:
        create_db.create_DB()
    sys.exit(app.exec_())

			
