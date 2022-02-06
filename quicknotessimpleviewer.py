#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
QuickNotesSimpleViewer

A light, fast and simple app to view memo notes.
"""

import sys
import os
import errno

from typing import Optional, Any
import argparse

import wx

from qnsvlib import qnsvgui

__author__  = "idealtitude"
__version__ = "0.1.0"
__license__ = "MT108"

# Constants
EXIT_SUCCESS: int = 0
EXIT_FAILURE: int = 1
DIR_SEP: str = os.sep

APP_PATHES = {
    "root": os.path.dirname(os.path.realpath(__file__)),
    "cwd": os.getcwd(),
    "home": os.path.expanduser('~'),
    "input": "nil"
}


class MyApp(wx.App):
    def OnInit(self):
        self.main_frame = qnsvgui.QuickNotesSimpleViewer(APP_PATHES, None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True


# Command line arguments
def get_args() -> argparse.Namespace:
    """Basic arguments parsing."""
    parser = argparse.ArgumentParser(
        prog="qnsv",
        description="QuickNotesSImpleViewer",
        epilog="Help and documentation at https://github.com/idealtitude/quicknotessimpleviewer",
    )

    parser.add_argument("file", nargs='?', help="Specifies a file to open")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser.parse_args()

def set_pathes_end() -> None:
    for key, value in APP_PATHES.items():
        if value != "nil" and not value.endswith(DIR_SEP):
            APP_PATHES[key] = f"{value}{DIR_SEP}"

def main() -> int:
    """Entry point"""
    args: argparse.Namespace = get_args()

    set_pathes_end()

    if args.file:
        file_in: str = args.file

        try:
            if os.path.isfile(file_in) and os.access(file_in, os.R_OK):
                if not os.path.isabs(file_in):
                    file_in = os.path.realpath(file_in)
        except FileNotFoundError:
            errmsg = f"Error {errno.ENOENT}: {os.strerror(errno.ENOENT)} {file_in}"
            raise FileNotFoundError(errmsg)
        except PermissionError:
            errmsg = f"Error {errno.EACCES}: {os.strerror(errno.EACCES)} {file_in}"
            raise PermissionError(errmsg)

        APP_PATHES["input"] = file_in

    app = MyApp(0)
    app.MainLoop()

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
