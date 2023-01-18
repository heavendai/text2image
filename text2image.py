#-*- coding:utf-8 -*-
"""
####################################
# author: mingyang.heaven@gmail.com
# date: 2022-11-05 23:47
# last modified: 2022-11-05 23:47
# filename: text2image.py
# description: 
####################################
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys, getopt
from generate_background import *

fontsFolder = './fonts'
def get_text_content(text_file):
    fo = open(text_file, "r")
    lines = fo.readlines()
    con = ''
    for line in lines:
        tab_to_space_line = line.replace('\t', '    ')
        #Replace tab with spaces otherwise it will render without indentions
        con += tab_to_space_line
    fo.close()
    print(con)
    return con

def main(text_file, dst_file, font_name='SimHei', font_size=22):
    text = get_text_content(text_file)
    #im = MakeGradationImg(600, 600, RGB(10,10,10), RGB(50, 12, 38), (False, False, False)) # for Thorough answer
    #im = MakeGradationImg(600, 600, RGB(230,230,230), RGB(0, 230, 0), (False, False, False)) # for That's true
    im = MakeGradationImg(600, 600, RGB(240,240,240), RGB(0, 0, 250), (False, False, False)) # 
    draw = ImageDraw.Draw(im) #Draw the image
    try:
        monoFont = ImageFont.truetype(os.path.join(fontsFolder, '%s.ttf' % font_name), font_size)
        draw.text((20, 20), text, fill='black', font=monoFont) #Draw the text on image with true fonts
    except Exception as ex:
        draw.text((20, 20), text, fill='black') #Draw the text on image with default system fonts
    im.save(dst_file) #Save the image
    return im

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: %s [text_path][dst_path][font_name][font_size]" % (sys.argv[0]))
        sys.exit(0)
    text_file = sys.argv[1]
    dst_file = sys.argv[2]
    font_name = sys.argv[3]
    font_size = int(sys.argv[4])
    main(text_file, dst_file, font_name, font_size)

