# -*- coding: utf-8 -*-
'''
*config.py: Configuration options*
----------------------------------
This file created in SelectConfigSetting on 13 03 2023 16:14
'''

import os.path
import GSASIIpath

debug = True
'''Set to True to turn on debugging mode. This enables use of IPython on
exceptions and on calls to :func:`GSASIIpath.IPyBreak` or breakpoint(). 
Calls to :func:`GSASIIpath.pdbBreak` will invoke pdb at that location.
%%
If debug is False, calls to :func:`GSASIIpath.IPyBreak`, breakpoint() and
:func:`GSASIIpath.pdbBreak` are ignored.
%%
From inside Spyder, calls to breakpoint() invoke the Spyder debugger, 
independent of the setting of debug. 
%%
Restart GSAS-II for the setting of debug to take effect.
'''

Main_Pos = (209, 205)
'''Main window location - will be updated & saved when user moves
it. If position is outside screen then it will be repositioned to default
'''

Main_Size = (1029, 606)
'''Main window size (width, height) - initially uses wx.DefaultSize but will updated
 and saved as the user changes the window
'''

pdffit2_exec = "/private/tmp/mf/envs/pdffit2/bin/python"
'''Defines the full path to a Python executable that has been configured 
with the PDFfit2 (diffpy) package. If None (the default), GSAS-II will see 
if PDFfit2 can be imported into the current Python.
'''

Plot_Pos = (26, 53)
'''Plot window location - will be updated & saved when user moves it
these widows. If position is outside screen then it will be repositioned to default
'''

Plot_Size = (1026, 877)
'''Plot window size (width, height) - initially uses wx.DefaultSize but will updated
 and saved as the user changes the window
'''

previous_GPX_files = [
	  "/Users/toby/Scratch/Seq2021Sept/repeatSeq5.gpx",
	  "/Users/toby/Projects/Ukagha/NoCopper.gpx",
	  "/private/tmp/Al20Ti2Nd.gpx",
	  "/private/tmp/Al20Ti2Nd_Powder_2023.gpx",
	  "/Users/toby/Projects/Ukagha/one with low copper.gpx",
   ]
'''A list of previously used .gpx files
'''

SeparateHistPhaseTreeItem = True
'''When this is set to True, the parameters for each histogram in each phase
are placed in a separate 1st-level tree item rather than in the Data tab 
for each phase. Requires GSAS-II be restarted to take effect. Default is False.

This option is under development and is not fully tested.
'''

