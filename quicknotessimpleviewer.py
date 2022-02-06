#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Sun Feb  6 05:31:00 2022 from "/home/stephane/Dev/PYTHON/PROJETS/QuickNotesSimplerViewer/tmp/qnsv_layout.wxg"
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class QuickNotesSimpleViewer(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: QuickNotesSimpleViewer.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("QuickNotesSImpleViewer")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("/home/stephane/Dev/PYTHON/PROJETS/QuickNotesSimplerViewer/qnsv-64x64.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = ["main_frame_statusbar"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)

        self.main_panel = wx.Panel(self, wx.ID_ANY)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.file_explorer = wx.TextCtrl(self.main_panel, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.file_explorer.SetMinSize((250, -1))
        main_sizer.Add(self.file_explorer, 0, wx.ALL | wx.EXPAND, 5)

        self.file_viewer = wx.TextCtrl(self.main_panel, wx.ID_ANY, "", style=wx.TE_AUTO_URL | wx.TE_BESTWRAP | wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB | wx.TE_RICH2 | wx.TE_WORDWRAP)
        self.file_viewer.SetMinSize((500, 480))
        self.file_viewer.SetBackgroundColour(wx.Colour(252, 252, 252))
        self.file_viewer.SetForegroundColour(wx.Colour(19, 19, 19))
        self.file_viewer.SetFont(wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Source Code Pro"))
        main_sizer.Add(self.file_viewer, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        self.main_panel.SetSizer(main_sizer)

        main_sizer.Fit(self)
        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_NAVIGATION_KEY, self.event_navkey)
        self.Bind(wx.EVT_TEXT, self.event_text, self.file_viewer)
        self.Bind(wx.EVT_TEXT_ENTER, self.event_text_enter, self.file_viewer)
        # end wxGlade

    def event_navkey(self, event):  # wxGlade: QuickNotesSimpleViewer.<event_handler>
        print("Event handler 'event_navkey' not implemented!")
        event.Skip()

    def event_text(self, event):  # wxGlade: QuickNotesSimpleViewer.<event_handler>
        print("Event handler 'event_text' not implemented!")
        event.Skip()

    def event_text_enter(self, event):  # wxGlade: QuickNotesSimpleViewer.<event_handler>
        print("Event handler 'event_text_enter' not implemented!")
        event.Skip()

# end of class QuickNotesSimpleViewer

class MyApp(wx.App):
    def OnInit(self):
        self.main_frame = QuickNotesSimpleViewer(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
