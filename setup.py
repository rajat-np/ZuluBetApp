import cx_Freeze
import sys
import os


base = None
executables = [cx_Freeze.Executable("gui.py",base = base ,icon = "1496065573_letter_Z_blue.ico")]
os.environ['TCL_LIBRARY'] = 'C:\\Python35\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python35\\tcl\\tk8.6'
os.environ['TIX_LIBRARY'] = 'C:\\Python35\\tcl\\tix8.4.3'

cx_Freeze.setup(
	name = "ZuluBet", 
	options = {"build_exe":{"packages":["tkinter","tkinter.tix","requests","bs4","lxml"], "include_files":["1496065573_letter_Z_blue.ico", "back.py","C:\\Python35\\DLLs\\tk86t.dll","C:\\Python35\\DLLs\\tcl86t.dll","C:\\Python35\\tcl\\tix8.4.3\\tix84.dll"]}}, 
	version = "1.0", 
	description = "Betting App for the Client",
	executables = executables
	)
