# Image-Scrambler
Takes images and scrambles the objects inside of them. It takes three command line inputs. The first is the directory of the images that you want to scramble. This must be surrounded by quotation marks. The second is the size of the chunks that the program is scrambling. This must be an int. The final one is the jitter factor. The jitter factor is the number of chunks away from the outline of the image that chunks are alowed to move. The more pixels there are per chunk(second input) the greater the effect of the jitter factor will be. This also must be an int.


1st: Directory (Surrounded by double quotes)

2nd: Pixels Per Chunk (integer)

3rd: Jitter Factor (integer)

Example:
python __main__.py "C:/My/Image/Directory" 50 3
