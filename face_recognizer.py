import os
import cv2
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # left image
        img_top = Image.open(r"images\faceRecognize.png")
        img_top = img_top.resize((650,650))
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage_top)
        f_lbl.place(x=0, y=45, width=650, height=650)

        # right image
        img_bottom = Image.open(r"images\facial_recognition.jpg")
        img_bottom = img_bottom.resize((650,650))
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage_bottom)
        f_lbl.place(x=650, y=45, width=650, height=650)

        b1_1 = Button(self.root, text='Face Recognition', cursor="hand2", command=self.face_recognize, font=(
            "times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=230, y=570, width=180, height=40)

    # attendance
    def mark_attendance(self, i, r, n, d):
        with open('attendance.csv', "r+", newline="\n") as f:
            myData = f.readlines()
            name_List = []
            dateList = []
            for line in myData:
                entry = line.split(",")
                name_List.append(entry[0])
                dateList.append(entry[-2])
            
            now = datetime.now()
            dt = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            if (i not in name_List):
                f.writelines(f"{i},{r},{n},{d},{dtString},{dt}, Present\n")
            elif dt not in dateList:
                f.writelines(f"{i},{r},{n},{d},{dtString},{dt}, Present\n")


    # face recognition
    def face_recognize(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                con = mysql.connector.connect(host="localhost", username="root", password="Shrijal@123", database="shrijaldb")
                my_cursor = con.cursor()

                my_cursor.execute("select Student_ID from students where Student_ID="+str(id))
                i = my_cursor.fetchone()
                i = i[0]

                my_cursor.execute("select `RollNo.` from students where Student_ID="+str(id))
                r = my_cursor.fetchone()
                r = r[0]

                my_cursor.execute("select Name from students where Student_ID="+str(id))
                n = my_cursor.fetchone()
                n = n[0]

                my_cursor.execute("select Department from students where Student_ID="+str(id))
                d = my_cursor.fetchone()
                d = d[0]


                if confidence > 77:
                    cv2.putText(img, f"Student Id:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Roll no:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Name:{n}", (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    self.mark_attendance(i,r,n,d)
                
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
                    cv2.putText(img, "Unknown face", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)

                coord = [x,y,w,h]
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classfier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__": 
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()