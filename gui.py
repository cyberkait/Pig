import wx
import media as m

# creating the window


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Pig")
        panel = wx.Panel(self)
        panel.SetBackgroundColour('black')
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.rollBtn = wx.Button(panel, label="roll")
        self.rollBtn.SetBackgroundColour((0, 71, 171))
        self.rollBtn.SetForegroundColour("white")
        self.rollBtn.Bind(wx.EVT_BUTTON, self.on_roll)
        my_sizer.Add(self.rollBtn, 0, wx.ALL | wx.CENTER, 5)
        self.bankBtn = wx.Button(panel, label="bank")
        self.bankBtn.SetBackgroundColour((0,  100, 0))
        self.bankBtn.SetForegroundColour("white")
        self.bankBtn.Bind(wx.EVT_BUTTON, self.on_bank)
        my_sizer.Add(self.bankBtn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_roll(self, event):
        m.p_roll()

    def on_bank(self, event):
        m.p_bank()


app = wx.App()
frame = MyFrame()
app.MainLoop()
