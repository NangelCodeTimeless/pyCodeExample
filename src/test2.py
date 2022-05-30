import wx
import wx.xrc
import wx.media
import os

class StaticText(wx.StaticText):
    def SetLabel(self, label):
        if label != self.GetLabel():
            wx.StaticText.SetLabel(self, label)

class Fr_AnaSayfa ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fapigo Biometrik Sistemi", pos = wx.DefaultPosition, size = wx.Size( 1024,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        Bs_AnaSayfa = wx.BoxSizer( wx.VERTICAL )
        self.Pn_Video = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.Pn_Video.SetMinSize( wx.Size( -1,200 ) )
        Vs_Video = wx.BoxSizer( wx.VERTICAL )
        self.Pn_Video.SetSizer( Vs_Video )
        self.Pn_Video.Layout()
        Vs_Video.Fit( self.Pn_Video )
        Bs_AnaSayfa.Add( self.Pn_Video, 1, wx.EXPAND |wx.ALL, 5 )
        try:
            backend = ""
            self.mc = wx.media.MediaCtrl()
            self.mc.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_DEFAULT)
            ok = self.mc.Create(self.Pn_Video, style=wx.SIMPLE_BORDER,szBackend=backend)
            if not ok:
                raise NotImplementedError
        except NotImplementedError:
            self.Destroy()
            raise




        self.Pn_Button = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.TAB_TRAVERSAL )
        self.Pn_Button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

        Bs_Button = wx.BoxSizer( wx.HORIZONTAL )

        Bs_Button.SetMinSize( wx.Size( -1,40 ) )
        self.Bt_Load = wx.Button( self.Pn_Button, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bs_Button.Add( self.Bt_Load, 0, wx.ALL, 5 )

        self.Bt_Play = wx.Button( self.Pn_Button, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bs_Button.Add( self.Bt_Play, 0, wx.ALL, 5 )

        self.Bt_Pause = wx.Button( self.Pn_Button, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bs_Button.Add( self.Bt_Pause, 0, wx.ALL, 5 )

        self.Bt_Stop = wx.Button( self.Pn_Button, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bs_Button.Add( self.Bt_Stop, 0, wx.ALL, 5 )


        self.slider = wx.Slider(self.Pn_Button, -1, 0, 0, 10)
        self.slider.SetMinSize((150, -1))
        self.Bind(wx.EVT_SLIDER, self.OnSeek, self.slider)
        Bs_Button.Add( self.slider, 0, wx.ALL, 5 )


        self.Bind(wx.media.EVT_MEDIA_LOADED, self.OnMediaLoaded)
        self.Bind(wx.EVT_BUTTON, self.OnLoadFile, self.Bt_Load)
        self.Bind(wx.EVT_BUTTON, self.OnPlay, self.Bt_Play)
        self.Bind(wx.EVT_BUTTON, self.OnPause, self.Bt_Pause)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.Bt_Stop)
        self.Bind(wx.EVT_SLIDER, self.OnSeek, self.slider)


        self.st_size = StaticText(self.Pn_Button, -1, size=(100,-1))
        self.st_len  = StaticText(self.Pn_Button, -1, size=(100,-1))
        self.st_pos  = StaticText(self.Pn_Button, -1, size=(100,-1))


        Bs_Button.Add( self.st_size, 0, wx.ALL, 5 )
        Bs_Button.Add( self.st_len, 0, wx.ALL, 5 )
        Bs_Button.Add( self.st_pos, 0, wx.ALL, 5 )

        self.Pn_Button.SetSizer( Bs_Button )
        self.Pn_Button.Layout()
        Bs_AnaSayfa.Add( self.Pn_Button, 0, wx.EXPAND |wx.ALL, 5 )


        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(100)


        self.Bind(wx.EVT_SIZE, self.ReSize)

        self.SetSizer( Bs_AnaSayfa )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    def OnLoadFile(self, evt):
        dlg = wx.FileDialog(self, message="Choose a media file",
                            defaultDir=os.getcwd(), defaultFile="",
                            style=wx.FD_OPEN | wx.FD_CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.DoLoadFile(path)
        dlg.Destroy()

    def ReSize(self, evt):
        self.mc.Pause()
        self.Layout()
        self.mc.SetSize(self.Pn_Video.GetSize())
        self.mc.Play()


    def DoLoadFile(self, path):

        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path,
                          "ERROR",
                          wx.ICON_ERROR | wx.OK)
            self.Bt_Play.Disable()
        else:
            self.mc.SetInitialSize()

            self.slider.SetRange(0, self.mc.Length())
            self.Bt_Play.Enable()
            self.GetSizer().Layout()

    def OnMediaLoaded(self, evt):
        self.Bt_Play.Enable()

    def OnPlay(self, evt):
        if not self.mc.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?",
                          "ERROR",
                          wx.ICON_ERROR | wx.OK)
        else:
            self.mc.SetInitialSize()
            self.GetSizer().Layout()
            self.slider.SetRange(0, self.mc.Length())

            self.mc.SetSize(self.Pn_Video.GetSize())


    def OnPause(self, evt):
        self.mc.Pause()

    def OnStop(self, evt):
        self.mc.Stop()


    def OnSeek(self, evt):
        offset = self.slider.GetValue()
        self.mc.Seek(offset)

    def OnTimer(self, evt):
        offset = self.mc.Tell()
        self.slider.SetValue(offset)
        self.st_size.SetLabel('size: %s' % self.mc.GetBestSize())
        self.st_len.SetLabel('length: %d seconds' % (self.mc.Length()/1000))
        self.st_pos.SetLabel('position: %d' % offset)

    def ShutdownDemo(self):
        self.timer.Stop()
        del self.timer

if __name__ == '__main__':
    Fapigo = wx.App()
    Fr_AnaSayfa = Fr_AnaSayfa(None)
    Fapigo.SetTopWindow(Fr_AnaSayfa)
    Fr_AnaSayfa.Show()
    Fapigo.MainLoop()