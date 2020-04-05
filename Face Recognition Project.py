from tkinter import *
from tkinter import filedialog
import tkinter.font as tkfont
from PIL import Image, ImageTk
import cv2 as cv




btn_color="#941679"
btn_text="#000000"
highlightbackground="#165893"
highlightcolor="798102"




def choose_image():
    choose_window = Tk()
    choose_window.withdraw()   
    choose_window.title("Choose your Own Image")
    file_path = filedialog.askopenfilename()
    print(file_path)


    face_cascade = cv.CascadeClassifier("C:/Users/ganes/Downloads/Programs/Face/haarcascade_frontalface_default.xml")
    img = cv.imread(file_path)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    print(type(faces))
    for x, y, w, h in faces:
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3) 
    resized = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv.imshow("Gray", resized)
    cv.waitKey(0)
    cv.destroyAllWindows()
    choose_window.mainloop()
def open_camera():
    open_camera_window=Tk()
    open_camera_window.title="Live Face Recognition"



    face_cascade = cv.CascadeClassifier("C:/Users/ganes/Downloads/Programs/Face/haarcascade_frontalface_default.xml")
    cap = cv.VideoCapture(0)

    while True:
        _, img = cap.read()

        img = cv.flip(img , 1)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


        cv.imshow('img', img)

        k = cv.waitKey(30)# & 0xff
        if k==27:
            break
        
    cap.release()
    open_camera_window.mainloop()

root = Tk()
root.geometry("1100x700")
title_font = tkfont.Font(size=30)
button_font=tkfont.Font(size=20)
root.title("Face Recognition System")

title_label = Label(root, text="Face Recognition Project", font=title_font, borderwidth=3, relief="groove")
title_label.place(x=300, y=50)
    
demo_image_var="C:/Users/ganes/Downloads/Programs/Face/leonardo.jpg"
demo_image_var1="C:/Users/ganes/Downloads/Programs/Face/leonardo2.jpg"

output_button=Button(root, text="Choose An Image",command=choose_image,font=button_font, bg=btn_color, fg=btn_text, borderwidth=3, relief="solid")
output_button.place(x=300, y=600)


camera_button=Button(root, text="Open Camera",command=open_camera,font=button_font, bg=btn_color, fg=btn_text, borderwidth=3, relief="solid")
camera_button.place(x=620, y=600)



load=Image.open(demo_image_var)
load=load.resize((450,400), Image.ANTIALIAS)
render=ImageTk.PhotoImage(load)

load1=Image.open(demo_image_var1)
load1=load1.resize((450,400), Image.ANTIALIAS)
render1=ImageTk.PhotoImage(load1)

image_lable=Label(root,image=render, height=400, width=450,borderwidt=3, relief="solid")
image_lable.place(x=50, y=150)

image_lable1=Label(root,image=render1, height=400, width=450,borderwidt=3, relief="solid")
image_lable1.place(x=600, y=150)



root.mainloop()