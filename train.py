from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2
import os

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Standard Attendance System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        img_top = Image.open(r"images\facerecognition.png")
        img_top = img_top.resize((1300,275))
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage_top)
        f_lbl.place(x=0, y=45, width=1300, height=275)

        b1_1 = Button(self.root, text='Train data', command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 25, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=320, width=1300, height=60)

        img_bottom = Image.open(r"images\facial-recognition.jpg")
        img_bottom = img_bottom.resize((1300,300))
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage_bottom)
        f_lbl.place(x=0, y=380, width=1300, height=300)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #L to convert to Grey scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            # C:\Users\shrij\OneDrive\Desktop\IDP\data\user.1.jpg
            # 0                                        1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13 #window closes on pressing enter
        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classfier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")



if __name__ == "__main__": 
    root = Tk()
    obj = Train(root)
    root.mainloop()