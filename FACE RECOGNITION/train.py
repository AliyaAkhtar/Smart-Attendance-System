import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class TRAIN:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        title_label=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="orange")
        title_label.place(x=0,y=0,width=1530,height=45)   

        img_top=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\9.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        l1=Label(self.root,image=self.photoimg_top)
        l1.place(x=0,y=45,width=1530,height=325)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",27,"bold"),bg="orange",fg="white")
        b1_1.place(x=0,y=370,width=1530,height=50)

        img3=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=420,width=1530,height=710)

        img_bottom=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\10.png")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        l1=Label(bg_img,image=self.photoimg_bottom)
        l1.place(x=20,y=30,width=1480,height=300)


        #lbph=local binary pattern histogram
#it is the easiest algorithms for face recognition . can represent local pics.it is posiible to get grid results.strong for grayscale.
#numpy increases the performances of changing into array
#uint8=datatype


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")

if __name__ == "__main__":
    root=Tk()
    obj=TRAIN(root)
    root.mainloop()            