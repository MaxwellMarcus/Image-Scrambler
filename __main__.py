from tkinter import *
from PIL import Image,ImageTk
from random import shuffle
import time

root = Tk()

canvas = Canvas(root,width = root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack()

def get_chunks(picture, num_chunks_x,num_chunks_y):
    picture_x = picture.width
    picture_y = picture.height

    chunk_x = int(picture_x/num_chunks_x)
    chunk_y = int(picture_y/num_chunks_y)

    final_picture = []
    positions = []

    for x in range(num_chunks_x):
        for y in range(num_chunks_y):
            x_pos = x*chunk_x
            y_pos = y*chunk_y

            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))
            data = chunk.load()

            useful = False
            for x1 in range(chunk_x):
                for y1 in range(chunk_y):
                    if data[x1,y1][0] == 0 and data[x1,y1][1] == 0 and data[x1,y1][2] == 0:
                        useful = True

            if useful:
                final_picture.append(chunk)
                positions.append((x_pos,y_pos))

    shuffle(positions)
    shuffle(positions)

    return (final_picture,positions)



if __name__ == '__main__':
    #getting a picture as an input
    picture = input('Picture: ')
    picture = Image.open(picture)
    print(picture.size)
    num_chunks_x = int(input('Number Of Chunks Per Row: '))
    num_chunks_y = int(input('Number Of Rows: '))


    new_picture = get_chunks(picture,num_chunks_x,num_chunks_y)
    new_pos = new_picture[1]
    new_picture = new_picture[0]


    pic = ImageTk.PhotoImage(picture)
    canvas.create_image(0,0,image=pic,anchor=NW)

    x_pos = 0
    y_pos = 0
    imgs = []
    for x in range(len(new_picture)):
        img = ImageTk.PhotoImage(new_picture[x])
        pos = new_pos[x]
        canvas.create_image(pos[0],pos[1],image=img,anchor=NW)
        imgs.append(img)
        root.update()
        time.sleep(.01)

    root.mainloop()
