#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Sun Aug  2 14:41:43 2009

import wx
import sys

# begin wxGlade: extracode
# end wxGlade



class EditMaterialPropagation(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: EditMaterialPropagation.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Material")
        self.list_box_1 = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE)
        self.label_2 = wx.StaticText(self, -1, "Name")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_3 = wx.StaticText(self, -1, "n")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_4 = wx.StaticText(self, -1, "GVD")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_8 = wx.StaticText(self, -1, "fs**2/m")
        self.label_5 = wx.StaticText(self, -1, "TOD")
        self.text_ctrl_4 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_9 = wx.StaticText(self, -1, "fs**3/m")
        self.label_6 = wx.StaticText(self, -1, "FOD")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_10 = wx.StaticText(self, -1, "fs**4/m")
        self.label_7 = wx.StaticText(self, -1, "Length")
        self.text_ctrl_6 = wx.TextCtrl(self, -1, "",style=wx.TE_RIGHT)
        self.label_11 = wx.StaticText(self, -1, "m")
        self.button_1 = wx.Button(self, -1, "Refresh")
        self.button_2 = wx.Button(self, -1, "Done")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.listbox_click, self.list_box_1)
        self.Bind(wx.EVT_BUTTON, self.refresh_click, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.done_click, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: EditMaterialPropagation.__set_properties
        self.SetTitle("Edit Material Propagation")
        self.SetMinSize((270,300))
        if(sys.platform=='win32'):
            self.SetBackgroundColour(wx.Colour(212,208,200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: EditMaterialPropagation.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(8, 3, 5, 5)
        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.list_box_1, 0, wx.ALL, 5)
        grid_sizer_1.Add((45, 5), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((30, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((30, 20), 0, wx.ALL, 5)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_3, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.label_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.label_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.text_ctrl_6, 0, wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_11, 0, wx.ALL, 5)
        grid_sizer_1.Add((30, 1), 0, wx.ALL, 1) #hack.
        grid_sizer_1.Add((30, 1), 0, wx.ALL, 1)
        grid_sizer_1.Add((30, 1), 0, wx.ALL, 1)
        sizer_1.Add(grid_sizer_1, 1, wx.ALL|wx.EXPAND, 5)
        
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add((30, 20), 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.button_1, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add((30, 20), 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.button_2, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add((30, 20), 0, wx.ALL|wx.EXPAND, 5)
        sizer_1.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
        
    def set_info(self,element,materials,refresh_function):
        self.element = element
        self.refresh_function = refresh_function
        self.materials = materials
        
        #add material names to list
        for material in materials:
            self.list_box_1.Insert(material[0],self.list_box_1.GetCount())
        self.list_box_1.Insert('User Defined',self.list_box_1.GetCount())
        self.list_box_1.SetSelection(self.list_box_1.GetCount()-1)
        
        #show element properties
        self.text_ctrl_1.SetValue(str(self.element.name))
        self.text_ctrl_2.SetValue(str(self.element.n))
        self.text_ctrl_3.SetValue(str(self.element.material[2]*1e30))
        self.text_ctrl_4.SetValue(str(self.element.material[3]*1e45))
        self.text_ctrl_5.SetValue(str(self.element.material[4]*1e60))
        self.text_ctrl_6.SetValue(str(self.element.length))

    def listbox_click(self, event): # wxGlade: EditMaterialPropagation.<event_handler>
        i = self.list_box_1.GetSelection()
        if(i == self.list_box_1.GetCount()-1):
            return #it is 'user defined', do nothing
        material = self.materials[i]
        self.text_ctrl_1.SetValue(str(material[0]))
        self.text_ctrl_2.SetValue(str(material[1]))
        self.text_ctrl_3.SetValue(str(material[2]*1e30))
        self.text_ctrl_4.SetValue(str(material[3]*1e45))
        self.text_ctrl_5.SetValue(str(material[4]*1e60))
        
        event.Skip()

    def refresh_click(self, event): # wxGlade: EditMaterialPropagation.<event_handler>
        self.element.name        = self.text_ctrl_1.GetValue()
        try:    
            self.element.n           = float(self.text_ctrl_2.GetValue())
        except:
            self.text_ctrl_2.SetValue(str(self.element.n))
            
        try: 
            self.element.length      = float(self.text_ctrl_6.GetValue())
        except:
            self.text_ctrl_6.SetValue(str(self.element.length))
            
        try: 
            self.element.material[2] = float(self.text_ctrl_3.GetValue())*1e-30
        except:
            self.text_ctrl_3.SetValue(str(self.element.material[2]*1e30))
            
        try: 
            self.element.material[3] = float(self.text_ctrl_4.GetValue())*1e-45
        except:
            self.text_ctrl_4.SetValue(str(self.element.material[3]*1e45))
            
        try: 
            self.element.material[4] = float(self.text_ctrl_5.GetValue())*1e-60
        except:
            self.text_ctrl_5.SetValue(str(self.element.material[4]*1e60))
        
        self.refresh_function()
                                
        if(not event is None):
            event.Skip()

    def done_click(self, event): # wxGlade: EditMaterialPropagation.<event_handler>
        self.refresh_click(None)
        self.Close()
        event.Skip()

# end of class EditMaterialPropagation

