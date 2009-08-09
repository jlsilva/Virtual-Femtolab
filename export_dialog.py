#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Tue Aug  4 20:21:38 2009

import wx
import sys

# begin wxGlade: extracode
# end wxGlade



class ExportFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ExportFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.type_box = wx.RadioBox(self, -1, "Type", choices=["Single Frame", "Animation"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.label_1 = wx.StaticText(self, -1, "Num. Frames")
        self.num_frames_ctrl = wx.SpinCtrl(self, -1, "64", min=0, max=100000)
        self.element_box = wx.RadioBox(self, -1, "Elements", choices=["Only Electric Field and Spectrum", "All"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.okbutton = wx.Button(self, -1, "Ok")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.type_click, self.type_box)
        self.Bind(wx.EVT_BUTTON, self.ok_click, self.okbutton)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ExportFrame.__set_properties
        self.SetTitle("Export")
        self.type_box.SetSelection(0)
        self.num_frames_ctrl.Enable(False)
        self.element_box.SetSelection(1)
        self.num_frames_ctrl.SetMinSize((80, 30))
        if(sys.platform=='win32'):
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ExportFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.type_box, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.label_1, 0, wx.ALL, 5)
        sizer_3.Add(self.num_frames_ctrl, 0, wx.ALL, 5)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(self.element_box, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add((20, 20), 1, 0, 0)
        sizer_2.Add(self.okbutton, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def type_click(self, event): # wxGlade: ExportFrame.<event_handler>
        if(self.type_box.GetSelection()==0):
            self.num_frames_ctrl.Enable(False)
        else:
            self.num_frames_ctrl.Enable(True)
        event.Skip()
        
    def set_info(self,export_callback):
        self.export_callback = export_callback

    def ok_click(self, event): # wxGlade: ExportFrame.<event_handler>
        num_frames = self.num_frames_ctrl.GetValue()
        export_type = self.type_box.GetSelection()
        export_elements = self.element_box.GetSelection()
        self.Destroy()
        self.export_callback(export_type, export_elements, num_frames)
        event.Skip()

# end of class ExportFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = ExportFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
