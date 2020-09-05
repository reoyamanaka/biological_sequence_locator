#nucleotide sequences in gene file
#peptide sequences in the protein file

import wx, os, sys, wx.lib.scrolledpanel

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt = True)
        frame = MyFrame()
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title = "Genetic Sequence Locator", size = (700, 650))
        self.OnInit()

    def OnInit(self):
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)

        labelFont = wx.Font(14, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        titleLabel = wx.StaticText(self, label = "Genetic Sequence Locator", pos = (30, 30))
        titleLabel.SetFont(labelFont)

        inputLabel = wx.StaticText(self, label = "Select the .txt file containing the COMPLETE sequence of interest.", pos = (30, 75))
        txtFileInput = wx.FilePickerCtrl(self, pos = (440, 70))
            
        sequenceLabel = wx.StaticText(self, label = "Insert the shorter sequence of interest.", pos = (30, 125))
        sequenceInput = wx.TextCtrl(self, pos = (280, 123), size = (200, 24))

        def locate(self):
            fileLocation = sequenceInput.GetValue()
            appendInput = ""
            with open(fileLocation, 'r') as rf:
                for line in rf:
                    appendInput += line
            print(appendInput)

        sequenceButton = wx.Button(self, label = "Search sequence of interest.", pos = (490, 125))
        sequenceButton.Bind(wx.EVT_BUTTON, locate)

        resultsLabel = wx.StaticText(self, label = "Results:", pos = (30, 175))
        resultsLabel.SetFont(labelFont)
        
        occurrenceLabel = wx.StaticText(self, label = "Occurrence frequency of the shorter sequence in the input .txt:", pos = (30, 215))
        occurrence = wx.StaticText(self, label = "", pos = (380, 215))

        locationLabel = wx.StaticText(self, label = "Location(s):", pos = (30, 255))
        locationOutput = wx.StaticText(self, label = "", pos = (30, 290))

        panelScroll = wx.lib.scrolledpanel.ScrolledPanel(self, size = (650, 250), pos = (30, 290), style = wx.SIMPLE_BORDER)
        boxSizer = wx.BoxSizer(wx.VERTICAL)

        def quitProgram(self):
            sys.exit()
        
        quitButton = wx.Button(self, label = "Quit", pos = (30, 560))
        quitButton.Bind(wx.EVT_BUTTON, quitProgram)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
        
