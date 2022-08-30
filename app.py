# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:13:36 2022

@author: prashant sehrawat
"""

from tkinter import *
from chat import get_resp, bot_name, choice


BG_GRAY = "#ABB2B9"
BG_COLOR = "#90ee90"
TEXT_COLOR = "#000000"

FONT = "Times", "14", "bold italic"
FONT_BOLD = "Helvetica 13 bold"

class ChatApp:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
     
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width = True, height = True)
        self.window.configure(width = 900, height = 600, bg = BG_COLOR)
        
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR,text = "welcome to Delicious Burgers", font = FONT_BOLD,pady = 10)
        head_label.place(relwidth = 1)
        
        line = Label(self.window, width = 400 , bg = BG_GRAY)
        line.place(relwidth=1,rely = 0.07, relheight=0.012)
        
        self.text_widget = Text(self.window,width = 20,height = 2 , bg = BG_COLOR,fg = TEXT_COLOR,font = FONT,padx = 5,pady = 5)
        
        self.text_widget.place(relheight = 0.745,relwidth = 1,rely = 0.08)
        self.text_widget.configure(cursor = "arrow",state = DISABLED)
        
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx = 0.974)
        scrollbar.configure(command = self.text_widget.yview)
        
        
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1,rely = 0.825)
        
        
        self.msg_entry = Entry(bottom_label, bg = "#2c3E50", fg ="#FFFFFF", font = FONT)
        self.msg_entry.place(relwidth=0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_clicked)
        
        
        send_button = Button(bottom_label,text = "Enter" , font = FONT_BOLD, width = 5, bg = BG_GRAY, command = lambda: self._on_enter_clicked(None))
        send_button.place(relx = 0.75,rely = 0.008, relheight = 0.04, relwidth = 0.12)
        

        speak_button = Button(bottom_label,text = "speak" , font = FONT_BOLD, width = 5, bg = BG_GRAY, command = lambda: self._on_speak_clicked(None))
        speak_button.place(relx = 0.88,rely = 0.008, relheight = 0.04, relwidth = 0.12)         
        
    def _on_enter_clicked(self,event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "YOU")
        
    
    def _on_speak_clicked(self,event):
        
        msg = choice()
        self._insert_message(msg, "YOU")
        
        
    def _insert_message(self,msg,sender):
        if not msg:
            return
        
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state = DISABLED)
        
        msg2 = f"{bot_name}: {get_resp(msg)}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state = DISABLED)
        
        self.text_widget.see(END)
        
if __name__ == "__main__":
    app = ChatApp()
    app.run()