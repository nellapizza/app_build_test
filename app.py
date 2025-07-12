import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

repo_dir = os.path.dirname(__file__)
images_dir = os.path.join(repo_dir, "resources", "images")
app_icon_path = os.path.join(images_dir, "icon.png")
app =QApplication(sys.argv)
app_icon = QIcon(app_icon_path)
widget = QWidget()
widget.setWindowIcon(app_icon)
widget.setWindowTitle('App')
widget.show()
app.exec()
