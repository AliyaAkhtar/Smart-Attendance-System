import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import STUDENT
from train import TRAIN
from face_recognition import Face_Recognition
from attendance import ATTENDANCE
 

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        #first image
        img=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\1.png")
        img=img.resize((550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        l1=Label(self.root,image=self.photoimg)
        l1.place(x=0,y=0,width=550,height=130)

        #second image
        img1=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\2.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photoimg1)
        l1.place(x=550,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\3.png")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        l1=Label(self.root,image=self.photoimg2)
        l1.place(x=1050,y=0,width=550,height=130)

        #background image
        img3=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #timer
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_label,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=100,height=50)
        time()    

        #student button
        img4=Image.open(r"college_images\student.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=250,y=300,width=220,height=40)

        #detect face button
        img5=Image.open(r"college_images\face detector.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=650,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=650,y=300,width=220,height=40)

        #attendance button
        img6=Image.open(r"college_images\attendance.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=1050,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDANCE",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1050,y=300,width=220,height=40)

        #train data button
        img7=Image.open(r"college_images\train data.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=450,y=370,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=450,y=570,width=221,height=40)

        #photos button
        img8=Image.open(r"college_images\photos.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=850,y=370,width=220,height=220)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=850,y=570,width=221,height=40)

    def open_img(self):
        os.startfile("data")


    #function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=STUDENT(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=TRAIN(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ATTENDANCE(self.new_window)        


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()      
