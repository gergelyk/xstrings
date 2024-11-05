# coding: lang-auto

# Encoding `lang-auto` above takes language code from your $LANG env var.
# Try changing it to `lang-none`, `lang-de`, `lang-it`, `lang-jp`...

import wx

app = wx.App()
window = wx.Frame(None, title=t"Simple application", size=(400, 200))
panel = wx.Panel(window)

wx.StaticText(panel, label=t"Hello World!", pos=(100,0))
btn1 = wx.Button(panel, label='&' + t'Move to the Corner', pos=(100, 50))
btn2 = wx.Button(panel, label='&' + t'Close this Window', pos=(100, 100))

btn1.Bind(wx.EVT_BUTTON, lambda ev: window.Move((0, 0)))
btn2.Bind(wx.EVT_BUTTON, lambda ev: window.Close())

window.Show(True)
app.MainLoop()
