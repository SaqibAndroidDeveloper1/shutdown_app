from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="Red")
restart_but=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)

restart_but.place(x=160,y=50,height=50,width=200)
restart_r=Button(st,text="Restart time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)

restart_r.place(x=160,y=170,height=50,width=200)
restart_log=Button(st,text="log_out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_out)

restart_log.place(x=160,y=290,height=50,width=200)

restart_shut=Button(st,text="Shutdown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)

restart_shut.place(x=160,y=410,height=50,width=200)

st.mainloop()