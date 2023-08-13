import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class STUDENT:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        #variables
        self.var_dep=StringVar()
        self.var_batch=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_r1=StringVar()

        #first image
        img=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\4.png")
        img=img.resize((550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        l1=Label(self.root,image=self.photoimg)
        l1.place(x=0,y=0,width=550,height=130)

        #second image
        img1=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\5.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photoimg1)
        l1.place(x=550,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\6.png")
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

        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_label.place(x=0,y=0,width=1530,height=45)

        f=Frame(bg_img,bd=2,bg="green")
        f.place(x=10,y=50,width=1500,height=600)

        #left label frame
        lf=LabelFrame(f,bd=5,bg="light green",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        lf.place(x=10,y=10,width=727,height=580)

        img_left=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\7.png")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        l1=Label(lf,image=self.photoimg_left)
        l1.place(x=0,y=0,width=720,height=130)

        #current course
        ccf=LabelFrame(lf,bd=5,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        ccf.place(x=0,y=135,width=720,height=120)

        #department
        dep=Label(ccf,text="DEPARTMENT",font=("calibri",12,"bold"),bg="white")
        dep.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(ccf,textvariable=self.var_dep,font=("times new roman",11,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","SOFTWARE","COMPUTER INFORMATION SYSTEM","CYBER SECURITY","ARTIFICIAL INTELLIGENCE","ELECTRICAL","MECHANICAL","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #batch
        batch=Label(ccf,text="BATCH",font=("calibri",12,"bold"),bg="white")
        batch.grid(row=0,column=2,padx=10)

        batch_combo=ttk.Combobox(ccf,textvariable=self.var_batch,font=("times new roman",11,"bold"),width=20,state="readonly")
        batch_combo["values"]=("Select Batch","FE","SE","TE","BE")
        batch_combo.current(0)
        batch_combo.grid(row=0,column=3,padx=2,pady=10)

        #year
        year=Label(ccf,text="YEAR",font=("calibri",12,"bold"),bg="white")
        year.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(ccf,textvariable=self.var_year,font=("times new roman",11,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2022-23","2021-22","2020-21","2019-20")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        #semester
        semester=Label(ccf,text="SEMESTER",font=("calibri",12,"bold"),bg="white")
        semester.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(ccf,textvariable=self.var_semester,font=("times new roman",11,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","First Semester","Second Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10)

        #class student
        csf=LabelFrame(lf,bd=5,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        csf.place(x=0,y=255,width=720,height=297)

        #student id
        s_id=Label(csf,text="STUDENT ID:",font=("calibri",12,"bold"),bg="white")
        s_id.grid(row=0,column=0,padx=10,pady=5)

        s_id_entry=ttk.Entry(csf,textvariable=self.var_id,width=20,font=("times new roman",11,"bold"))
        s_id_entry.grid(row=0,column=1,padx=10,pady=5)

        #student name
        s_name=Label(csf,text="STUDENT NAME:",font=("calibri",12,"bold"),bg="white")
        s_name.grid(row=0,column=2,padx=10,pady=5)

        s_name_entry=ttk.Entry(csf,textvariable=self.var_name,width=20,font=("times new roman",11,"bold"))
        s_name_entry.grid(row=0,column=3,padx=10,pady=5)

        #roll no
        roll_no=Label(csf,text="ROLL NO:",font=("calibri",12,"bold"),bg="white")
        roll_no.grid(row=1,column=0,padx=10,pady=5)

        roll_no_entry=ttk.Entry(csf,textvariable=self.var_roll_no,width=20,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=2,pady=10)

        #gender
        gender=Label(csf,text="GENDER:",font=("calibri",12,"bold"),bg="white")
        gender.grid(row=1,column=2,padx=10,pady=5)

        gender_combo=ttk.Combobox(csf,textvariable=self.var_gender,font=("times new roman",11,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=5)

        #date of birth
        dob=Label(csf,text="DATE OF BIRTH:",font=("calibri",12,"bold"),bg="white")
        dob.grid(row=2,column=0,padx=10,pady=5)

        dob_entry=ttk.Entry(csf,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5)

        #email
        email=Label(csf,text="EMAIL:",font=("calibri",12,"bold"),bg="white")
        email.grid(row=2,column=2,padx=10,pady=5)

        email_entry=ttk.Entry(csf,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5)

        #phone no
        phone_no=Label(csf,text="PHONE NUMBER:",font=("calibri",12,"bold"),bg="white")
        phone_no.grid(row=3,column=0,padx=10,pady=5)

        phone_no_entry=ttk.Entry(csf,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold"))
        phone_no_entry.grid(row=3,column=1,padx=10,pady=5)

        #address
        address=Label(csf,text="ADDRESS:",font=("calibri",12,"bold"),bg="white")
        address.grid(row=3,column=2,padx=10,pady=5)

        address_entry=ttk.Entry(csf,textvariable=self.var_address,width=20,font=("times new roman",11,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=5)

        #radio buttons
        self.var_r1=StringVar()
        r1=ttk.Radiobutton(csf,variable=self.var_r1,text="Take Photo Smaple",value="Yes")
        r1.grid(row=4,column=0)
        r2=ttk.Radiobutton(csf,variable=self.var_r1,text="No Photo Smaple",value="No")
        r2.grid(row=4,column=1)

        #button frame
        bf=Frame(csf,bd=2,bg="white",relief=RIDGE)
        bf.place(x=0,y=170,width=710,height=35)

        save=Button(bf,command=self.add_data,text="SAVE",font=("times new roman",12,"bold"),bg="green",fg="white",width=19)
        save.grid(row=0,column=0)

        update=Button(bf,command=self.update_data,text="UPDATE",font=("times new roman",12,"bold"),bg="green",fg="white",width=19)
        update.grid(row=0,column=1)

        delete=Button(bf,command=self.delete_data,text="DELETE",font=("times new roman",12,"bold"),bg="green",fg="white",width=19)
        delete.grid(row=0,column=2)

        reset=Button(bf,command=self.reset_data,text="RESET",font=("times new roman",12,"bold"),bg="green",fg="white",width=19)
        reset.grid(row=0,column=3)

        #photo frame
        pf=Frame(csf,bd=2,bg="white",relief=RIDGE)
        pf.place(x=0,y=220,width=710,height=35)

        take_photo=Button(pf,command=self.generate_dataset,text="TAKE PHOTO SAMPLE",font=("times new roman",12,"bold"),bg="green",fg="white",width=80)
        take_photo.grid(row=0,column=0)

        #right label frame
        rf=LabelFrame(f,bd=5,bg="light green",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        rf.place(x=757,y=10,width=727,height=580)

        img_right=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\8.png")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        l1=Label(rf,image=self.photoimg_right)
        l1.place(x=0,y=0,width=720,height=130)

        #search system
        search_frame=LabelFrame(rf,bd=5,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=135,width=720,height=70)

        search_label=Label(search_frame,text="SEARCH BY:",font=("calibri",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5)

        self.var_combo_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo_search,font=("times new roman",11,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select Option","ROLL NO","PHONE NUMBER","STUDENT ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=17,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5)

        search=Button(search_frame,command=self.search_data,text="SEARCH",font=("times new roman",12,"bold"),bg="green",fg="white",width=10)
        search.grid(row=0,column=3,padx=10)

        show_all=Button(search_frame,command=self.fetch_data,text="SHOW ALL",font=("times new roman",12,"bold"),bg="green",fg="white",width=10)
        show_all.grid(row=0,column=4,padx=10)

        #table frame
        table_frame=Frame(rf,bd=5,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=210,width=720,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","batch","year","sem","id","name","roll no","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("batch",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=130)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#try handles the errors
    #function decleration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_batch.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_roll_no.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_r1.get()
                                                                                                    )) 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success","Student Details Have Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)                                                                                          

    #function to fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_batch.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll_no.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_r1.set(data[12])


    #update function
    def update_data(self):   
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Batch=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,Date_Of_Birth=%s,Email=%s,Phone_Number=%s,Address=%s,Photo_Sample_Status=%s where Student_ID=%s",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_batch.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_roll_no.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_r1.get(),
                                                                                            self.var_id.get()
                                                                                              ))
                else: 
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)  
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                   conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
                   my_cursor=conn.cursor()
                   sql="delete from student where Student_ID=%s"
                   val=(self.var_id.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 


    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_batch.set("Select Batch") 
        self.var_year.set("Select Year") 
        self.var_semester.set("Select Semester") 
        self.var_id.set("") 
        self.var_name.set("") 
        self.var_roll_no.set("") 
        self.var_gender.set("Male") 
        self.var_dob.set("") 
        self.var_email.set("") 
        self.var_address.set("") 
        self.var_phone.set("")
        self.var_r1.set("")  

    #  generate data set  or take a photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Batch=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,Date_Of_Birth=%s,Email=%s,Phone_Number=%s,Address=%s,Photo_Sample_Status=%s where Student_ID=%s",(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_batch.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_roll_no.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_r1.get(),
                                                                                                                                                                                                                                self.var_id.get()==id+1
                                                                                                                                                                                                                               
                                                                                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #load predefined data on face frontal from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3(by default)
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped


                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 

    #search_data
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="301510mel",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select Department,Batch,Year,Roll_No,Semester,Student_ID,Name,Date_Of_Birth,Gender,Email,Phone_Number,Address,Photo_Sample_Status from student where Roll_No="+str(self.var_search.get())) 
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)           

                
if __name__ == "__main__":
    root=Tk()
    obj=STUDENT(root)
    root.mainloop()      
