import wx, os, sys, wx.lib.scrolledpanel, re

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt = True)
        frame = MyFrame()
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title = "Genetic Sequence Locator", size = (708, 630))
        self.OnInit()

    def OnInit(self):
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)

        labelFont = wx.Font(14, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        titleLabel = wx.StaticText(self, label = "Biological Sequence Locator", pos = (30, 30))
        titleLabel.SetFont(labelFont)

        inputLabel = wx.StaticText(self, label = "Select the .txt file containing the COMPLETE sequence.", pos = (30, 75))
        txtFileInput = wx.FilePickerCtrl(self, pos = (370, 70))

        panelScroll = wx.lib.scrolledpanel.ScrolledPanel(self, size = (650, 250), pos = (30, 290), style = wx.SIMPLE_BORDER)
        locationsPrimer = wx.StaticText(panelScroll, label = "The shorter sequence of interest was found on:", pos = (20, 9))
        locationsPrimer.Hide()
        locations = wx.StaticText(panelScroll, label = "", pos = (250, 65))
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        boxSizer.Add(locations)
            
        sequenceLabel = wx.StaticText(self, label = "Insert the shorter sequence of interest.", pos = (30, 125))
        sequenceInput = wx.TextCtrl(self, pos = (280, 123), size = (200, 24))

        def locate(self):
            fileLocation = txtFileInput.GetPath()
            soi = sequenceInput.GetValue()
            appendInput = ""
            with open(fileLocation, 'r') as rf:
                for line in rf:
                    appendInput += line
            appendInput = appendInput.replace(" ", "")
            print(appendInput)
            if appendInput.find(soi) == -1:
                locationsPrimer.Show()
                locationsPrimer.SetLabel("Smaller sequence not found.")
                locations.Hide()
                matches = re.finditer(soi, appendInput)
                raw_matches_positions = [match.start() for match in matches]
                matches_positions = []
                for i in raw_matches_positions:
                    matches_positions.append(i + 1)
                occurrence.SetLabel(str(len(matches_positions)))
                
                
            else:
                locationsPrimer.Show()
                locations.Show()
                locationsPrimer.SetLabel("The shorter sequence of interest was found on:")
                panelScroll.SetSizer(boxSizer)
                panelScroll.SetupScrolling(scroll_x = True, scroll_y = True)
                matches = re.finditer(soi, appendInput)
                raw_matches_positions = [match.start() for match in matches]
                matches_positions = []
                for i in raw_matches_positions:
                    matches_positions.append(i + 1)
                occurrence.SetLabel(str(len(matches_positions)))
                print(matches_positions)
                tempLocations = 2*"\n"
                for i in matches_positions:
                    tempLocations += "\t" + "Nucleotide/amino acid index: " + str(i) + "\n"
                locations.SetLabel(tempLocations)
                
        sequenceButton = wx.Button(self, label = "Search Sequence of Interest", pos = (490, 125))
        sequenceButton.Bind(wx.EVT_BUTTON, locate)

        resultsLabel = wx.StaticText(self, label = "Results:", pos = (30, 175))
        resultsLabel.SetFont(labelFont)
        
        occurrenceLabel = wx.StaticText(self, label = "Occurrence frequency of the shorter sequence in the input text file:", pos = (30, 215))
        occurrence = wx.StaticText(self, label = "", pos = (460, 215))

        locationLabel = wx.StaticText(self, label = "Location(s):", pos = (30, 255))
        locationOutput = wx.StaticText(self, label = "", pos = (30, 290))


        def quitProgram(self):
            sys.exit()
        
        quitButton = wx.Button(self, label = "Quit", pos = (30, 560))
        quitButton.Bind(wx.EVT_BUTTON, quitProgram)

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
