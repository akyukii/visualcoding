from PIL import Image
import numpy as np

info_str = input('Enter your message：')

def str2bin(info_str):
    info_ascii = []
    for i in info_str:
        #creates ASCII code
        info_ascii.append(ord(i))
    info_bin = []
    for j in info_ascii:
        #cuts off the 0b
        temp = list(bin(j)[2:])
        res = []
        for k in temp:
            res.append(int(k))
        info_bin.append(res)
    res_array = np.array(info_bin)
    return res_array

#converts to monotone
pic = Image.open('舞台.png').convert('L')
info_array = str2bin(info_str)
height, width = info_array.shape
piece_pic = pic.crop((0,0,width,height))
piece_array = np.array(piece_pic)
print(piece_array)
new_array = info_array + piece_array
print(new_array)
new_piece = Image.fromarray(new_array)
print(new_piece)

pic.paste(new_piece, (0,0))
pic.save('new_pic.png')
new_pic = Image.open('new_pic.png')
pic = Image.open('舞台.png').convert("L")
new_pic.show()
pic.show()
new_pic_array = np.array(new_pic)
pic_array = np.array(pic)
print(new_pic_array)
print(pic_array)