import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

#mydata is a global variable
mydata=[]

class ATTENDANCE:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img1=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\13.png")
        img1=img1.resize((770,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photoimg1)
        l1.place(x=0,y=0,width=770,height=200)

        #second image
        img2=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\14.png")
        img2=img2.resize((770,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        l1=Label(self.root,image=self.photoimg2)
        l1.place(x=760,y=0,width=770,height=200)

        #background image
        img3=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_label=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_label.place(x=0,y=0,width=1530,height=45)

        f=Frame(bg_img,bd=2,bg="brown")
        f.place(x=10,y=50,width=1500,height=600)

        #left label frame
        lf=LabelFrame(f,bd=5,bg="pink",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        lf.place(x=10,y=10,width=727,height=580)

        img_left=Image.open(r"C:\Users\shaba\Desktop\FACE RECOGNITION\college_images\15.png")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        l1=Label(lf,image=self.photoimg_left)
        l1.place(x=0,y=0,width=720,height=130)

        left_frame=Frame(lf,bd=2,relief=RIDGE,bg="white")
        left_frame.place(x=0,y=133,width=717,height=340)

        #label and enteries

        #attendance id
        a_id=Label(left_frame,text="ATTENDANCE ID:",font=("calibri",12,"bold"),bg="white")
        a_id.grid(row=0,column=0,padx=10,pady=10)

        a_id_entry=ttk.Entry(left_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",11,"bold"))
        a_id_entry.grid(row=0,column=1,padx=10,pady=10)

        #name
        name=Label(left_frame,text="STUDENT NAME:",font=("calibri",12,"bold"),bg="white")
        name.grid(row=0,column=2,padx=10,pady=10)

        name_entry=ttk.Entry(left_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",11,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=10)

        #roll no
        roll_no=Label(left_frame,text="ROLL NO:",font=("calibri",12,"bold"),bg="white")
        roll_no.grid(row=1,column=0,padx=10,pady=10)

        roll_no_entry=ttk.Entry(left_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=10)

        #department
        department=Label(left_frame,text="DEPARTMENT:",font=("calibri",12,"bold"),bg="white")
        department.grid(row=1,column=2,padx=10,pady=10)

        department_entry=ttk.Entry(left_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",11,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=10)

        #time
        time=Label(left_frame,text="TIME:",font=("calibri",12,"bold"),bg="white")
        time.grid(row=2,column=0,padx=10,pady=10)

        time_entry=ttk.Entry(left_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",11,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10)

        #date
        date=Label(left_frame,text="DATE:",font=("calibri",12,"bold"),bg="white")
        date.grid(row=2,column=2,padx=10,pady=10)

        date_entry=ttk.Entry(left_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",11,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10)

        #attendance 
        attendance=Label(left_frame,text="ATTENDANCE:",font=("calibri",12,"bold"),bg="white")
        attendance.grid(row=3,column=0,padx=10,pady=10)

        attendance_combo=ttk.Combobox(left_frame,textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),width=18,state="readonly")
        attendance_combo["values"]=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=10,pady=10)

        #button frame
        bf=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        bf.place(x=0,y=240,width=710,height=35)

        save=Button(bf,text="IMPORT CSV",command=self.importCsv,font=("times new roman",12,"bold"),bg="brown",fg="white",width=26)
        save.grid(row=0,column=0)

        update=Button(bf,text="EXPORT CSV",command=self.exportCsv,font=("times new roman",12,"bold"),bg="brown",fg="white",width=26)
        update.grid(row=0,column=1)

        reset=Button(bf,text="RESET",command=self.reset_data,font=("times new roman",12,"bold"),bg="brown",fg="white",width=26)
        reset.grid(row=0,column=2)

        #right label frame
        rf=LabelFrame(f,bd=5,bg="pink",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        rf.place(x=757,y=10,width=727,height=580)

        table_frame=Frame(rf,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=0,width=720,height=470)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","roll no","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("roll no",text="Roll No")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll no",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #fetch data 
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #importcsv
    def importCsv(self): 
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #exportcsv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root) 
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row) 
        rows=content['values'] 
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_roll.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=ATTENDANCE(root)
    root.mainloop()         