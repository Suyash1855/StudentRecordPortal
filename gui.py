from customtkinter import *
from helper import * 


mode= "dark"
set_appearance_mode(mode)
set_default_color_theme("dark-blue")


def ldMode():
    set_appearance_mode("light")
def dMode():
    set_appearance_mode("dark")

def get():
    ent= txt.get()
    # name=txt3.get()
    # bir=txt2.get()
    entry.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    newWindow= CTkToplevel(root)
    newWindow.title("Student Record")
    newWindow.geometry("500x600")
    frame= CTkFrame(master=newWindow)
    frame.pack(pady=20, padx= 60 , fill='both', expand= True)
    l1= CTkLabel(frame, text="Student Information", font= ("san sarif", 20, "bold"))
    l1.pack(pady=10,padx=10)
    S1.fetch_all(ent)
    if len(ent)== 0:
        le2= CTkLabel(frame, text="All field are required", font= ("san sarif", 20, "bold"))
        le2.pack(pady=10,padx=10)
    if len(ent) >10:
         le1= CTkLabel(frame, text="No Student Found", font= ("san sarif", 20, "bold"))
         le1.pack(pady=10,padx=10)
    else:
        lA=CTkLabel(frame, text="Name:" ,font= ("san sarif", 15 ,"bold"))
        lA.pack(padx=100)
        lA1= CTkLabel(frame, text=rec[1])
        lA1.pack(padx=10)

        lB=CTkLabel(frame, text="Enrollment No:" ,font= ("san sarif", 15 ,"bold"))
        lB.pack(padx=100)
        lB2= CTkLabel(frame, text=rec[2])
        lB2.pack(padx=10)

        lC=CTkLabel(frame, text="Date of Birth:" ,font= ("san sarif", 15 ,"bold"))
        lC.pack(padx=100)
        lC2= CTkLabel(frame, text=rec[3])
        lC2.pack(padx=10)

        lD=CTkLabel(frame, text="Father's Name:" ,font= ("san sarif", 15 ,"bold"))
        lD.pack(padx=100)
        lD2= CTkLabel(frame, text=rec[4])
        lD2.pack(padx=10)

        lE=CTkLabel(frame, text="Course:" ,font= ("san sarif", 15 ,"bold"))
        lE.pack(padx=100)
        lE2= CTkLabel(frame, text=rec[5])
        lE2.pack(padx=10)

        lF=CTkLabel(frame, text="Fee Status:" ,font= ("san sarif", 15 ,"bold"))
        lF.pack(padx=100)
        lF2= CTkLabel(frame, text=rec[6])
        lF2.pack(padx=10)

        lG=CTkLabel(frame, text="Gender:" ,font= ("san sarif", 15 ,"bold"))
        lG.pack(padx=100)
        lG2= CTkLabel(frame, text=rec[7])
        lG2.pack(padx=10)

        lH=CTkLabel(frame, text="Semester:" ,font= ("san sarif", 15 ,"bold"))
        lH.pack(padx=100)
        lH2= CTkLabel(frame, text=rec[8])
        lH2.pack(padx=10)

        lI=CTkLabel(frame, text="G-mail:" ,font= ("san sarif", 15 ,"bold"))
        lI.pack(padx=100)
        lI2= CTkLabel(frame, text=rec[9])
        lI2.pack(padx=10)



    


root = CTk()
root.title("Student Record Portal")
root.geometry("500x500")
frame= CTkFrame(master=root )
frame.pack(pady=20, padx= 60 , fill='both', expand= True)
label1= CTkLabel(master=frame, text="School of Electronic , Davv" , font= ("san sarif", 20, "bold") )
label1.pack( pady=12, padx=10)



    
label= CTkLabel(master=frame, text="Enter student details", )
label.pack(pady=12, padx=10)

txt3=StringVar()
label2= CTkLabel(master=frame, text="Name", )
label2.pack( padx=10)
entry= CTkEntry(master=frame ,width= 200,textvariable=txt3)
entry.pack( padx=10)
name=entry.get()


txt= StringVar()
label4= CTkLabel(master=frame, text="Enrollment No.", )
label4.pack( padx=10)
entry1= CTkEntry(master=frame,  width= 200, textvariable=txt)
entry1.pack( padx=10, )
ent=entry1.get()

txt2=StringVar()
label3= CTkLabel(master=frame, text="Birth Date", )
label3.pack( padx=10)
entry2= CTkEntry(master=frame,  width= 200,textvariable=txt2)
entry2.pack( padx=10)
bir=entry2.get()

b1= CTkButton(master=frame, text= "search", command=get  )
b1.pack(pady=30, padx=10)
btn= CTkRadioButton(master=frame, text="light mode", command=ldMode )
btn.pack(pady=8)
btn1= CTkRadioButton(master=frame, text="dark mode", command=dMode)
btn1.pack(pady=8)
root.mainloop()



