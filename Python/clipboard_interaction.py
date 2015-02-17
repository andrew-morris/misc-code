#!/usr/bin/python
# referencing the following blog post - http://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python/4203897#4203897

from Tkinter import Tk

def SetClipboard(value):
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(value)
  r.destroy()
  
def GetClipboard():
  r = Tk()
  r.withdraw()
  contents = r.selection_get(selection = "CLIPBOARD")
  return contents
