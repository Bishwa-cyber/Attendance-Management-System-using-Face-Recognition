import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognizer import Face_Recognition
from attendance import Attendance

class Face_Recognition_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        img = Image.open(
            r"images\ap.jpg")
        img = img.resize((500, 130))
        self.photoimage = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=389, height=130)

        img2 = Image.open(
            r"images\facial.jpg")
        img2 = img2.resize((500, 130))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=389, y=0, width=500, height=130)

        img3 = Image.open(
            r"images\system.jpg")
        img3 = img3.resize((500, 130))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimage3)
        f_lbl.place(x=889, y=0, width=385, height=130)

        #background
        img4 = Image.open(
            r"images\back.jpg")
        img4 = img4.resize((1530, 710))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimage4)
        bg_img.place(x=0, y=130, width=1300, height=700)

        title_lbl = Label(bg_img, text="FACE RECOGNITION BASED STANDARD ATTENDANCE SYSTEM SOFTWARE", font=(
            "times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=45)

        #student
        img5 = Image.open(
            r"images\student.jpg")
        img5 = img5.resize((220, 220))
        self.photoimage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimage5,command=self.student_details, cursor="hand2")
        b1.place(x=85, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Student Details', command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=85, y=250, width=220, height=40)

        # Face detector
        img6 = Image.open(
            r"images\access.jpg")
        img6 = img6.resize((220, 220))
        self.photoimage6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimage6, cursor="hand2", command=self.face_data)
        b1.place(x=370, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Face detector', cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=370, y=250, width=220, height=40)

        # Attendance
        img7 = Image.open(
            r"images\night.jpg")
        img7 = img7.resize((220, 220))
        self.photoimage7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimage7, cursor="hand2", command=self.attendance_data)
        b1.place(x=650, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Attendance', cursor="hand2", command=self.attendance_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=250, width=220, height=40)

        #Helpdesk
        img8 = Image.open(
            r"C:\Users\shrij\OneDrive\Desktop\IDP\images\helpdesk.jpg")
        img8 = img8.resize((220, 220))
        self.photoimage8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimage8, cursor="hand2")
        b1.place(x=930, y=70, width=220, height=220)

        b1_1 = Button(bg_img, text='Helpdesk', cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=930, y=250, width=220, height=40)

        #Photos data
        img9 = Image.open(
            r"C:\Users\shrij\OneDrive\Desktop\IDP\images\photos.jpg")
        img9 = img9.resize((220, 220))
        self.photoimage9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimage9, cursor="hand2", command=self.open_img)
        b1.place(x=85, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text='Photos data', cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=85, y=510, width=220, height=40)

        #Train data        
        img10 = Image.open(
            r"C:\Users\shrij\OneDrive\Desktop\IDP\images\training.jpg")
        img10 = img10.resize((220, 220))
        self.photoimage10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimage10, cursor="hand2", command=self.train_data)
        b1.place(x=370, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text='Train data', cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=370, y=510, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    # Function buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendance_System(root)

    root.mainloop()
