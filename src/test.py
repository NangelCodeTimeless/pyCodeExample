import wx
import wx.adv
import wx.grid as gridlib


class Window(wx.Frame):
    def __init__(self, title, size):
        super().__init__(None, title=title, pos=wx.DefaultPosition, size=size)
        self.createUI()
        self.Center()
        self.Show()

    def createUI(self):
        # wx.Frame.__init__(self, parent=None, title="A Simple Grid")
        panel = wx.Panel(self)

        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)
        myGrid.SetRowLabelSize(0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)



def main():
    application = wx.App()
    Window("test", (300, 400))
    # window.createUI()
    application.MainLoop()


if __name__ == "__main__":
    main()

