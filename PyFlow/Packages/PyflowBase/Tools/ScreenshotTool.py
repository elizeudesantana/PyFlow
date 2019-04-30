from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.PyflowBase.Tools import RESOURCES_DIR
from PyFlow.UI.ContextMenuDataBuilder import ContextMenuDataBuilder

from Qt import QtGui
from Qt.QtWidgets import QFileDialog


class ScreenshotTool(ShelfTool):
    """docstring for ScreenshotTool."""
    def __init__(self):
        super(ScreenshotTool, self).__init__()

    def onAction1(self, arg):
        print(self.name(), "pressed", arg)

    def contextMenuBuilder(self):
        menuBuilder = ContextMenuDataBuilder()
        menuBuilder.addEntry("Action1", "Foo", lambda: self.onAction1("foo"), ScreenshotTool.getIcon())
        menuBuilder.addEntry("Action2", "Bar category", icon=ScreenshotTool.getIcon())
        menuBuilder.addEntry("Action3", "Bar", lambda: self.onAction1("bar"), ScreenshotTool.getIcon(), "Action2")
        return menuBuilder

    @staticmethod
    def toolTip():
        return "Takes screenshot of visible area of canvas and\nsaves image to file"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(RESOURCES_DIR + "screenshot_icon.png")

    @staticmethod
    def name():
        return str("ScreenshotTool")

    def do(self):
        name_filter = "Image (*.png)"
        fName = QFileDialog.getSaveFileName(filter=name_filter)
        if not fName[0] == '':
            print("save screen to {0}".format(fName[0]))
            img = self.canvas.grab()
            img.save(fName[0], quality=100)
