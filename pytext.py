# Packages for pyText
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5 import uic

# pyText Main Window
class pyGUI(QMainWindow):
    
    # Show Window
    def __init__(self):
        super(pyGUI, self).__init__()
        uic.loadUi('Assets/UI/pytext.ui', self)
        self.show()
        
        # Styling
        self.setWindowTitle("pyText")
        
        # Font Settings
        self.action8px.triggered.connect(lambda: self.change_size(8))
        self.action12px.triggered.connect(lambda: self.change_size(12))
        self.action20px.triggered.connect(lambda: self.change_size(20))
        self.action24px.triggered.connect(lambda: self.change_size(24))
        self.action30px.triggered.connect(lambda: self.change_size(30))
        
        # Opening File
        self.actionOpen.triggered.connect(self.open_file)
        
        # Saving File
        self.actionSave.triggered.connect(self.save_file)
        
        # New File
        self.actionNew.triggered.connect(self.new_file)
        
    # Font Setting Function    
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))
        
    # Open File Function
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All (*)", options=options )
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
    
    # Save Function            
    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text File (*.txt);; All (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())
    
    # New File Function            
    def new_file(self):
        options = QFileDialog.Options()
        self.plainTextEdit.setPlainText("")
        
        
        
def main():
    app = QApplication([])
    window = pyGUI()
    app.exec_()

if __name__ == '__main__':
    main()