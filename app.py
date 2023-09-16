from tkinter import * 
from chat import get_res, bot_name 
import tkinter as tk
# from PIL import Image
# filen = r'logo.png'
# img = Image.open(filen)
# img.save('icon.ico',format = 'ICO', sizes=[(32,32)])

BG_GRAY = "#ABB2B9" 
BG_COLOR = "#17202A" 
TEXT_COLOR = "#EAECEE" 
FONT = "Helvetica 14" 
FONT_BOLD = "Helvetica 13 bold" 
class ChatApplication: 
    def __init__(self): 
        self.window = Tk() 
        self._setup_main_window() 

    def run(self): 
        self.window.mainloop() 
    def _setup_main_window(self): 
        
        
        self.window.title("FixAPI chatBot") 
        self.window.resizable(width=True, height=True) 
        self.window.configure(width=470, height=550, bg=BG_COLOR) 
        head= Label(self.window,bg=BG_COLOR,fg=TEXT_COLOR,
                        text="Welcome",font=FONT_BOLD,pady=10)
        head.place(relwidth=1)
        line=Label(self.window,width=450,bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07,relheight=0.012)
        self.text_widget=Text(self.window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,font=FONT,padx=5,pady=5)
        self.text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)
          
        bottom_label=Label(self.window,bg=BG_GRAY,height=80)
        bottom_label.place(relwidth=1,rely=0.825)
        self.message_entry=Entry(bottom_label,bg="#2C3E50",fg=TEXT_COLOR,font=FONT)
        self.message_entry.place(relwidth=0.74,relheight=0.06,relx=0.011,rely=0.008)
        self.message_entry.focus()
        self.message_entry.bind("<Return>",self._on_enter_pressed)
        sendB=Button(bottom_label,text="Send",font=FONT_BOLD,width=20,bg=BG_GRAY,command=lambda:self._on_enter_pressed(None))
        sendB.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)

    def _on_enter_pressed(self,event):
        msg=self.message_entry.get()
        self._insert_msg(msg,"You")
    def _insert_msg(self,msg,sender):
        if not msg:
            return
        self.message_entry.delete(0,END)
        msg1=f"{sender}:{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

        self.message_entry.delete(0,END)
        msg2=f"{bot_name}:{get_res(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)
if __name__=="__main__":

    app = ChatApplication() 
    app. run() 
