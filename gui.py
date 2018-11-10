import wx
from matrix import Matrix

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.x = 1
        self.y = 1
        self._cells = []
        self.current_matrix = None

        self.g_sizer = None

        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        menuItem = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        cells = ['1', '2', '3', '4'] 
        self.sizer2.Add(wx.StaticText(self, label="Number of Equations: "))
        self.y_dim = wx.ComboBox(self,choices=cells, style=wx.CB_READONLY, value='1')
        self.y_dim.Bind(wx.EVT_COMBOBOX, self.OnYDim)
        self.sizer2.Add(self.y_dim, 1, wx.EXPAND)

        self.sizer2.Add(wx.StaticText(self, label="Number of variables: "))
        self.x_dim = wx.ComboBox(self,choices=cells, style=wx.CB_READONLY, value='1')
        self.x_dim.Bind(wx.EVT_COMBOBOX, self.OnXDim)
        self.sizer2.Add(self.x_dim, 1, wx.EXPAND)

        self.submit = wx.Button(self, label="submit")
        self.submit.Bind(wx.EVT_BUTTON, self.OnSubmit)
        self.sizer2.Add(self.submit)

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.DrawCells()
        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()
    
    def OnSubmit(self, event):
        m = []
        for i in range(len(self._cells)):
            m.append([])
            for j in range(len(self._cells[0])):
                m[i].append(int(self._cells[i][j].GetValue()))
        self.current_matrix = Matrix.from_list(m)
        print(self.current_matrix.coefficient_matrix)
    
    def DrawCells(self):
        self._cells = []
        for i in range(len(self.sizer.GetChildren()) - 1):
            self.sizer.Hide(i + 1)
            self.sizer.Remove(i + 1)

        self.g_sizer = wx.GridSizer(self.x, self.y, 5)
        for i in range(self.y):
            self._cells.append([])
            for j in range(self.x):
                self._cells[i].append(wx.TextCtrl(self, size = (20,20), style=wx.TE_CENTRE))
                self.g_sizer.Add(self._cells[i][j])

        self.sizer.Add(self.g_sizer)
        self.Layout()
        self.Fit()
    

    def OnXDim(self, event): 
        self.x = int(self.x_dim.GetValue())
        self.DrawCells()

    def OnYDim(self, event): 
        self.y = int(self.y_dim.GetValue())
        self.DrawCells()




app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()