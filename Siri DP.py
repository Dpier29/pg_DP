Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:\Users\csci\Desktop\Davis Piper\Talking Thing.py ========
Traceback (most recent call last):
  File "C:\Program Files\Python36\lib\site-packages\win32com\client\dynamic.py", line 89, in _GetGoodDispatch
    IDispatch = pythoncom.connect(IDispatch)
pywintypes.com_error: (-2147221005, 'Invalid class string', None, None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\csci\Desktop\Davis Piper\Talking Thing.py", line 5, in <module>
    speak = wincl.Dispatch("SAPI.SpVioce")
  File "C:\Program Files\Python36\lib\site-packages\win32com\client\__init__.py", line 95, in Dispatch
    dispatch, userName = dynamic._GetGoodDispatchAndUserName(dispatch,userName,clsctx)
  File "C:\Program Files\Python36\lib\site-packages\win32com\client\dynamic.py", line 114, in _GetGoodDispatchAndUserName
    return (_GetGoodDispatch(IDispatch, clsctx), userName)
  File "C:\Program Files\Python36\lib\site-packages\win32com\client\dynamic.py", line 91, in _GetGoodDispatch
    IDispatch = pythoncom.CoCreateInstance(IDispatch, None, clsctx, pythoncom.IID_IDispatch)
pywintypes.com_error: (-2147221005, 'Invalid class string', None, None)
>>> 
======== RESTART: C:\Users\csci\Desktop\Davis Piper\Talking Thing.py ========
Listening...
Thinking...
Google Speech Recongnition could not understand audio
>>> 
