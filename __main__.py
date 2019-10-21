from tkinter import *
from PIL import Image,ImageTk
from random import shuffle
import time
import random
import sys
import os

root = Tk()

canvas = Canvas(root,width = root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack()

def get_chunks(picture, num_chunks_x,num_chunks_y,jitter):
    picture_x = picture.width
    picture_y = picture.height

    chunk_x = int(picture_x/num_chunks_x)
    chunk_y = int(picture_y/num_chunks_y)

    final_picture = []
    all_chunks = []
    positions = []
    all_positions = []

    start_useful = False
    for x in range(num_chunks_x):
        first_useful = False
        last_useful = False
        for y in range(num_chunks_y):
            x_pos = x*chunk_x
            y_pos = y*chunk_y

            all_positions.append((x_pos,y_pos))

            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))

            all_chunks.append(chunk)

            data = chunk.load()
            for x1 in range(chunk_x):
                for y1 in range(chunk_y):
                    if not data[x1,y1][:3] == (255,255,255):
                        if not first_useful:
                            first_useful = y_pos
                        last_useful = y_pos

        for y in range(num_chunks_y):
            y_pos = y*chunk_y
            x_pos = x*chunk_x
            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))
            if y_pos >= first_useful-jitter*chunk_y and y_pos <= last_useful+jitter*chunk_y and first_useful:
                final_picture.append(chunk)
                positions.append((x_pos,y_pos))

    shuffle(positions)

    new = Image.new('RGB',(picture_x,picture_y),color = (255,255,255))
    for i in all_positions:
        if i in positions:
            pos = positions.index(i)
            new.paste(final_picture[pos],i)
        else:
            pos = all_positions.index(i)
            new.paste(all_chunks[pos],i)



    return new



if __name__ == '__main__':
    #getting a picture as an input
    pictures = os.listdir(sys.argv[1])
    num_chunks_x = int(sys.argv[2])
    jitter = int(sys.argv[3])

    new_pictures = []
    for i in pictures:
        img = Image.open(sys.argv[1]+'\\'+i)
        new_pictures.append(get_chunks(img,num_chunks_x,num_chunks_x,jitter))

    for i in range(len(pictures)):
        dot = pictures[i].index('.')
        new_filename = pictures[i].strip(pictures[i][dot:])
        new_pictures[i].save(str(sys.argv[1])+'\\'+new_filename+'_scr'+pictures[i][dot:],pictures[i][dot+1:])

    root.mainloop()
