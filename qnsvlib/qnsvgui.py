#-*- coding: utf-8 -*-

import os
import errno

import subprocess
import re

import wx
import wx.richtext


class QuickNotesSimpleViewer(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        self.app_pathes = args[0]
        reargs = list(args)
        reargs.pop(0)
        reargs = tuple(reargs)

        wx.Frame.__init__(self, *reargs, **kwds)
        self.SetTitle("QuickNotesSImpleViewer")

        favicon = f"{self.app_pathes['root']}qnsv-64x64.png"
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(favicon, wx.BITMAP_TYPE_ANY))
        #_icon.CopyFromBitmap(wx.Bitmap("./qnsv-64x64.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = ["QuickNotesSimpleViwer - No file selected"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)

        #self.main_panel = wx.Panel(self, wx.ID_ANY)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #self.file_explorer = wx.TextCtrl(self.main_panel, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.file_explorer = wx.GenericDirCtrl(self, -1, dir=f"self.app_pathes['home']", style=wx.DIRCTRL_SHOW_FILTERS |
wx.DIRCTRL_3D_INTERNAL | wx.DIRCTRL_MULTIPLE | wx.DIRCTRL_SELECT_FIRST, filter="MD files (*.md)|*.md|All files (*.*)|*.*")

        self.file_explorer.SetMinSize((250, 480))
        main_sizer.Add(self.file_explorer, 0, wx.ALL | wx.EXPAND, 5)

        #self.file_viewer = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_AUTO_URL | wx.TE_BESTWRAP | wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB | wx.TE_RICH2 | wx.TE_WORDWRAP)
        # RichTextCtrl(parent, id=-1, value="", pos=DefaultPosition,
        #      size=DefaultSize, style=RE_MULTILINE, validator=DefaultValidator,
        #      name=TextCtrlNameStr)
        initial_content = ""
        fp = self.app_pathes["input"]
        if fp != "nil" and self.check_fmime(fp):
            with open(fp, 'r') as ic:
                initial_content = ic.read()
                self.statusbar.SetStatusText(f"Current file: {fp}")

        self.file_viewer = wx.richtext.RichTextCtrl(self, value=initial_content, size=wx.Size(500, 480))
        #self.file_viewer.SetMinSize((500, 480))
        # self.file_viewer.SetBackgroundColour(wx.Colour(252, 252, 252))
        # self.file_viewer.SetForegroundColour(wx.Colour(19, 19, 19))
        # self.file_viewer.SetFont(wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Source Code Pro"))
        main_sizer.Add(self.file_viewer, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        self.SetSizer(main_sizer)

        main_sizer.Fit(self)
        self.Layout()
        self.Centre()

        # EVENTS
        # Window
        self.Bind(wx.EVT_NAVIGATION_KEY, self.event_navkey)

        # GenericDirCtrl
        self.Bind(wx.EVT_DIRCTRL_FILEACTIVATED, self.event_file_selected, self.file_explorer)

        # RichTextCtrl
        self.Bind(wx.EVT_TEXT, self.event_text, self.file_viewer)
        self.Bind(wx.EVT_TEXT_ENTER, self.event_text_enter, self.file_viewer)

    def check_fmime(self, file_path):
        result = subprocess.check_output(["file", "--mime-type", file_path])
        mime_type = result.split()[-1]
        if _m := re.match(r"^text\/.+$", mime_type.decode('utf-8')):
            return True
        return False

    def event_file_selected(self, event):
        fp = self.file_explorer.GetPath()
        content = ""
        errmsg = ""
        checks = False

        try:
            if os.path.isfile(fp) and os.access(fp, os.R_OK) and self.check_fmime(fp):
                checks = True
        except FileNotFoundError:
                errmsg = f"Error {errno.ENOENT}: {os.strerror(errno.ENOENT)} {fp}"
                # raise FileNotFoundError(errmsg)
        except PermissionError:
                errmsg = f"Error {errno.EACCES}: {os.strerror(errno.EACCES)} {fp}"
                # raise PermissionError(errmsg)
        except IsADirectoryError:
                errmsg = f"Error {errno.EISDIR}: {os.strerror(errno.EISDIR)} {fp}"
                # raise PermissionError(errmsg)

        if checks:
            with open(fp, 'r') as ic:
                content = ic.read()

            self.file_viewer.SetValue(content)
            self.statusbar.SetStatusText(f"Current file: {fp}")
        else:
            if len(errmsg) > 0:
                self.statusbar.SetStatusText(errmsg)
            else:
                self.statusbar.SetStatusText(f"Can not open file {fp}")

    def event_navkey(self, event):
        print("Event handler 'event_navkey' not implemented!")
        event.Skip()

    def event_text(self, event):
        print("Event handler 'event_text' not implemented!")
        event.Skip()

    def event_text_enter(self, event):
        print("Event handler 'event_text_enter' not implemented!")
        event.Skip()
