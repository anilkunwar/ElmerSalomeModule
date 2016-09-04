# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:35:56 2016

@author: Rainer Jacob

Salome Plugin-manager file for declaration of Elmer functionality to Salome
"""

from PyQt4 import QtGui

import salome_pluginsmanager
import sys
import os

#add SALOME_PLUGIN_PATH to Python environment for easier module import
plugin_path = os.environ.get("SALOME_PLUGINS_PATH")  + "\\ElmerSalome"
sys.path.append(plugin_path)

#import window handler
import elmer_window_handler as ewh

#required to keep reference to all created widgets, will be overwritten everytime
qwidget = QtGui.QWidget()

#define about Function
def about(context):
    global ewh
    #get active module and check if SMESH
    active_module = context.sg.getActiveComponent()
    if active_module != "SMESH":
        QtGui.QMessageBox.about(None, str(active_module),
                                    "Functionality is only provided in mesh module.")
        return
    qwidget = ewh.about()

#define generalSetup function
def generalSetup(context):
    global ewh, qwidget
    #get active module and check if SMESH
    active_module = context.sg.getActiveComponent()
    if active_module != "SMESH":
        QtGui.QMessageBox.about(None, str(active_module),
                                    "Functionality is only provided in mesh module.")
        return
    qwidget = ewh.showGeneralSetup()
    qwidget.show()
    
#declare ShowWindow-Function to plugin manager
salome_pluginsmanager.AddFunction('ELMER/About', 'About ELMER plugin', about)
salome_pluginsmanager.AddFunction('ELMER/General Setup', 'General setup of Elmer', generalSetup)