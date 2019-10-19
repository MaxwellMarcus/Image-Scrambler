from tkinter import *
from PIL import Image,ImageTk

root = Tk()

canvas = Canvas(root,width = root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack()

def get_chunks(picture, num_chunks_x,num_chunks_y):
    picture_x = picture.width
    picture_y = picture.height

    chunk_x = int(picture_x/num_chunks_x)
    chunk_y = int(picture_y/num_chunks_y)

    final_picture = []

    for x in range(num_chunks_x):
        row_chunks = []
        for y in range(num_chunks_y):
            x_pos = x*chunk_x
            y_pos = y*chunk_y

            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))

            row_chunks.append(chunk)

        final_picture.append(row_chunks)

    return final_picture



if __name__ == '__main__':
    #getting a picture as an input
    picture = input('Picture: ')
    picture = Image.open(picture)
    chunk_size = input('Chunk Size: ')

    new_picture = get_chunks(picture,20,20)

    x_pos = 0
    y_pos = 0
    imgs = []
    for y in new_picture:
        for x in y:
            img = ImageTk.PhotoImage(x)
            canvas.create_image(y_pos,x_pos,image=img)
            imgs.append(img)
            x_pos += picture.height/19
        x_pos = 0
        y_pos += picture.width/19

    root.mainloop()
