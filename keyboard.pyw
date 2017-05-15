# -*- coding: utf-8 -*- # 
from tkinter import *
import pythoncom 
import pyHook#需要pyhook和pywin32

def on_click():
	label['text'] = text.get()#需要输入密码并click后退出
	text.set('')
	if label['text'] =='password': 
		quit()

def onKeyboardEvent(event):
	if str(event.Key)=='F5' or str(event.Key)=='2' or str(event.Key)=='3' or str(event.Key)=='0':#0,2,3,f5可使用某些功能,功能需再设置
		print ("Key:", event.Key) 
		print ("you can use this function")
		print ("---")
  # 同鼠标事件监听函数的返回值   
		return True
	elif str(event.Key)=='P' or (event.Key)=='A' or str(event.Key)=='S' or str(event.Key)=='W' or str(event.Key)=='O' or str(event.Key)=='R' or str(event.Key)=='D':
		#设定password的按键
		return True
	else:
		return False

hm = pyHook.HookManager()  
hm.KeyDown = onKeyboardEvent 
hm.HookKeyboard()
  
root = Tk(className='password')
label = Label(root)
label['text'] = 'please input password'
label.pack()
text = StringVar()
text.set('')
entry = Entry(root)
entry['textvariable'] = text
entry.pack()
button = Button(root,text='enter in',command=on_click).pack()
root.mainloop()#创建输入窗口，尚未实现无法关闭/关闭后循环弹出

pythoncom.PumpMessages()