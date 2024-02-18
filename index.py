from customtkinter import *
from PIL import Image,ImageTk
from Unlock import face
from Listen_Speak import *
logo_img=CTkImage(dark_image=Image.open("logo.png"),size=(100,100))
def Admin_callback(): 
    import customtkinter as ctk 
    import tkinter.messagebox as tkmb 
    admin_img=CTkImage(dark_image=Image.open("adminlogin.png"),size=(50,50))
    lab=CTkLabel(app,image=admin_img,text='ADMIN Login',compound="top")
    lab.grid(row=0,column=0)
    lab.place(anchor='center', relx=0.5, rely=0.1)
    # Selecting GUI theme - dark, light , system (for system default) 
    ctk.set_appearance_mode("dark") 

    # Selecting color theme - blue, green, dark-blue 
    ctk.set_appearance_mode("dark") 

    def face_unlock():
        result=face()
        if result :
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            return 1
        else:
            return 0

    def login(): 
        username = "iam@rishikant"
        password = "vyom123"
        if user_entry.get() == username and user_pass.get() == password: 
            Speak_en("Welcome rishi sir ")
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            return 1 
            #ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
        elif user_entry.get() == username and user_pass.get() != password: 
            Speak_en("Wrong password")
            tkmb.showwarning(title='Wrong password',message='Please check your password') 
            return 0
        elif user_entry.get() != username and user_pass.get() == password: 
            Speak_en("unknown username")
            tkmb.showwarning(title='Wrong username',message='Please check your username') 
            return 0
        else: 
            Speak_en("login failed")
            tkmb.showerror(title="Login Failed",message="Invalid Username and password") 
            return 0



    label = ctk.CTkLabel(app,text="") 

    label.pack(pady=20) 


    frame = ctk.CTkFrame(master=app) 
    frame.pack(pady=20,padx=20,fill='both',expand=True) 

    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 

    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10) 


    button = ctk.CTkButton(master=frame,text='Login',command=login) 
    button.pack(pady=12,padx=10) 
    button = ctk.CTkButton(master=frame,text='Face Unlock',command=face_unlock) 
    button.pack(pady=12,padx=10)
    
     
app = CTk()
app.title("V.Y.O.M.")
app.geometry("800x450")
app.resizable(False, False)

lab=CTkLabel(app,image=logo_img,text='V.Y.O.M.',compound="top")
lab.grid(row=0,column=0)
lab.place(anchor='center', relx=0.5, rely=0.3)

button = CTkButton(app, text="ADMIN", command=Admin_callback)
button.grid(row=0, column=0, padx=20, pady=20)
button.place(anchor='center', relx=0.5, rely=0.6)


app.mainloop()