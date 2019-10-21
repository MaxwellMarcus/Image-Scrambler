#import libraries
from PIL import Image
from random import shuffle
import time
import random
import sys
import os

#Create custon exception
class InputError(Exception):
    pass



def scramble(picture:Image, chunk_x:int,chunk_y:int,jitter:int) -> 'Scrambled Image':
    '''
    picture: source image
    chunk_x: width of chunks
    chunk_y: height of chunks
    jitter: number of chunks from the outline chunks can go to
    '''

    #Getting information about image and chunks
    picture_x = picture.width
    picture_y = picture.height

    num_chunks_x = int(picture_x/chunk_x)
    num_chunks_y = int(picture_y/chunk_y)

    final_picture = []
    all_chunks = []
    positions = []
    all_positions = []


    start_useful = False
    for x in range(num_chunks_x):
        first_useful = False
        last_useful = False
        #finding the parts of each row need to be scrambled
        for y in range(num_chunks_y):
            x_pos = x*chunk_x
            y_pos = y*chunk_y

            all_positions.append((x_pos,y_pos))

            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))

            all_chunks.append(chunk)

            data = chunk.load()
            for x1 in range(chunk_x):
                for y1 in range(chunk_y):
                    if not data[x1,y1][:3] == (225,225,225):
                        if not first_useful:
                            first_useful = y_pos
                        last_useful = y_pos
        #Getting the data for each chunk that needs to be scrambled
        for y in range(num_chunks_y):
            y_pos = y*chunk_y
            x_pos = x*chunk_x
            chunk = picture.crop((x_pos,y_pos,x_pos+chunk_x,y_pos+chunk_y))
            if y_pos >= first_useful-jitter*chunk_y and y_pos <= last_useful+jitter*chunk_y and first_useful:
                final_picture.append(chunk)
                positions.append((x_pos,y_pos))
    #Moving the chunks to new positions
    shuffle(positions)

    #Putting the all in one image
    new = Image.new('RGB',(picture_x,picture_y),color = (225,225,225))
    for i in all_positions:
        if i in positions:
            pos = positions.index(i)
            new.paste(final_picture[pos],i)
        else:
            pos = all_positions.index(i)
            new.paste(all_chunks[pos],i)

    return new



if __name__ == '__main__':
    print(scramble.__annotations__)
    #getting inputs
    if len(sys.argv) == 4:
        pass
    else:
        raise RequiresThreeInputs
    pictures = os.listdir(sys.argv[1])
    try:
        chunk_size = int(sys.argv[2])
    except ValueError:
        raise InputError('Chunk Size must be int')
    try:
        jitter = int(sys.argv[3])
    except ValueError:
        raise MustInputInts

    #Scrambling all images
    new_pictures = []
    for i in pictures:
        try:
            img = Image.open(sys.argv[1]+'\\'+i)
        except FileNotFoundError:
            raise MustInputImages

        new_pictures.append(scramble(img,int(img.width/chunk_size),int(img.height/chunk_size),jitter))

    #Putting new images into folder
    for i in range(len(pictures)):
        dot = pictures[i].index('.')
        new_filename = pictures[i].strip(pictures[i][dot:])
        new_pictures[i].save(str(sys.argv[1])+'\\'+new_filename+'_scr'+pictures[i][dot:],pictures[i][dot+1:])
