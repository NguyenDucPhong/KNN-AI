import PIL
from PIL import ImageTk, Image, ImageDraw
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2

width = 200
height = 200
white = (255,255,255)
black = (0,0,0)

def RUN():
    #Đọc ảnh ảnh train và ảnh nhận dạng
    img = cv2.imread('digits.png', 0)
    imgtest = cv2.imread('image_save.png', 0)

    #Cắt ảnh thành từng ô nhỏ
    cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]

    #chuyển thành ma trận 2 chiều
    x = np.array(cells)
    x2 = np.array(imgtest)

    #Tạo dữ liệu train và dữ liệu test
    train = x[:,:50].reshape (-1, 400).astype(np.float32)
    test = x2.reshape(-1,400).astype(np.float32)

    #gắn nhãn cho dữ liệu
    k = np.arange(10)
    train_labels = np.repeat(k, 250)[:, np.newaxis]
    #Nhận dạng
    knn = cv2.ml.KNearest_create()
    knn.train(train, 0, train_labels)
    kq1, kq2, kq3, kq4 = knn.findNearest(test, 20)
    box.insert(END, "ket qua la: {}".format(int(kq2)))

def clear():
    box.delete(1.0, END)
    global image1, draw;
    cv.delete("all")
    image1 = PIL.Image.new("RBG", (width, height), black)
    draw = ImageDraw.Draw(image1)
    

def save():
    filename = "image.png"
    image1.save(filename)
    image = Image.open('image.png')
    new_image = image.resize((20,20))
    new_image.save("image_save.png")
def paint(event):
    x1, y1 = (event.x -3), (event.y-3)
    x2, y2 = (event.x +3), (event.y+3)
    cv.create_line(x1,y1,x2,y2,fill="White", width=15)
    draw.line([x1,y1,x2,y2], fill="White", width=15)
    
#Của sổ chương trình
root = Tk()
root.geometry("1280x721+90+30")
root.title("Nguyễn Đức Phong - 62TH5")
background=Image.open("background.png")
render = ImageTk.PhotoImage(background)
img3 = Label(root, image=render)
img3.place(x=0,y=0)

#Ô viết số
cv = Canvas(root, width=width, height=height, bg='black')
cv.place(x=185, y=200)
image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)

cv.bind("<B1-Motion>", paint)

#Nút save
button_frame = Frame(root).pack(side=BOTTOM)
save_button = Button(button_frame,text="save",font=(("Times New Romen"),15,'bold'),command=save)
save_button.place(x=250,y=500)

#Box hiện kết quả
box = Text(root, width=25, height=1, font=("Times New Romen", 13))
box.pack(pady=300)

#Nút RUN
button_frame = Frame(root).pack(side=BOTTOM)
run_button=Button(button_frame,text="run", font=(("Times New Romen"),15,'bold'), command=RUN)
run_button.place(x=545, y=325)

#Nút Clear
button_frame = Frame(root).pack(side=BOTTOM)
clear_button = Button(button_frame,text="clear",font=(("Times New Romen"),15,'bold'),command=clear)
clear_button.place(x=650, y=325)
root.mainloop()
