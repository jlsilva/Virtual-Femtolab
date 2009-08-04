#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Tue Aug  4 20:21:38 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class ProgressFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
       
        self.label_1 = wx.StaticText(self, -1, "Exporting frame  1 of   ")

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ExportFrame.__set_properties
        self.SetTitle("Exporting animation")
               # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ExportFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add(self.label_1, 0, wx.ALL|wx.EXPAND, 5)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
        
    def set_frame(self,n,max):
        self.label_1.SetLabel('Exporting frame %d of %d'%(n,max))
        self.label_1.Refresh()
#        self.label_1.Update()
        wx.Yield()



# end of class 



