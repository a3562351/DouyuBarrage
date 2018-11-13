#coding=utf-8

from room import ChatRoom
import ctypes
import thread
import Tkinter

whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd)
pass

mRoot = Tkinter.Tk()
mRoot.attributes("-alpha", 0.8)
# mRoot.overrideredirect(True)
mRoot.wm_attributes('-topmost',1)

mListBox = Tkinter.Listbox(mRoot, width = 40, height = 15)
mListBox.pack()

def on_chat_message(msg):
    barrage = '[%s]:%s' % (msg.attr('nn'), msg.attr('txt'))
    # print barrage
    mListBox.insert(0, barrage)
pass

def run():
    room = ChatRoom('5143258')
    room.on('chatmsg', on_chat_message)
    room.knock()
pass

thread.start_new_thread(run, ())
mRoot.mainloop()
