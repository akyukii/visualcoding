from PIL import Image
import numpy as np 

pic = Image.open("舞台.png").convert('L')
new_pic = Image.open("new_pic.png").convert("L")
pic_array = np.array(pic)
new_pic_array = np.array(new_pic)
#subtract to get the encoded binary
secret_array = new_pic_array-pic_array

tar_list = []
for i in secret_array:
    #if all values are equivalent, then:
    if (i[0:7] == np.array([0,0,0,0,0,0,0])).all():
        #exits for loop.
        break
    temp = []
    for j in i[0:7]:
        temp.append(str(j))
    #joins all elements in i[0:7] into a string
    bin_res = ''.join(temp)
    #turns binary into ascii
    ascii_res = int(bin_res, 2)
    #turns ascii code into a character
    str_res = chr(ascii_res)
    #appends characters to single tar_list
    tar_list.append(str_res)
#joins all characters in tar_list to decode message
print("".join(tar_list))
