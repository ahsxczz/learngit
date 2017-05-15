# -*- coding: utf-8 -*- # 
from tkinter import *
import pythoncom 
import pyHook#需要pyhook和pywin32

keystr=''
		
def onKeyboardEvent(event):
	global keystr
	if str(event.Key)=='F5' or str(event.Key)=='2' or str(event.Key)=='3' or str(event.Key)=='0':#0,2,3,f5可使用某些功能,功能需再设置
		print ("Key:", event.Key) 
		print ("you can use this function")
		print ("---")
		# 同鼠标事件监听函数的返回值   
		return True
	elif str(event.Key)=='P' or (event.Key)=='A' or str(event.Key)=='S' or str(event.Key)=='W' or str(event.Key)=='O' or str(event.Key)=='R' or str(event.Key)=='D':#设定password的按键
		if keystr=='':
			keystr=keystr+str(event.Key)
			print('please input password')
		else:
			keystr=keystr+str(event.Key)
			print(keystr)
			if keystr=='PASSWORD':
				quit()
			if len(keystr)>=8:
				root = Tk(className='password')  
				label = Label(root)  
				label['text'] = 'your password is wrong'  
				label.pack()
				keystr=''
		return True
	elif str(event.Key)=='1':
		openwindow()
		return True
	else:
		return False

def openwindow():
	global keystr
	
	root = Tk(className='password')  
	label = Label(root)  
	label['text'] = 'please input password'  
	label.pack() 
	text = StringVar()  
	text.set('')  
	entry = Entry(root)  
	entry['textvariable'] = text  
	entry.pack()
	root.mainloop() 
		
def main():
	hm = pyHook.HookManager()  
	hm.KeyDown = onKeyboardEvent 
	hm.HookKeyboard()  
	openwindow()
	pythoncom.PumpMessages()
	
if __name__ == "__main__":   
  main()