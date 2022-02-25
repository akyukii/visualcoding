# visualcoding
A visual encoding/decoding platform made with numpy.

Hi, this is a short project made with Python and numpy (library). In this project, there are two parts:

1. Encoder: images are pre-selected (although it is very simple to change in the code [just one line]) and a message (user inputs) can be encoded in the image through the use of binary and ASCII conversion. The message is stored in the pixels of RGB color in the image.
2. Decoder: two images are uploaded (new_pic, which is the file containing the message) and the original image (the same image without any prior modifications). The code uses an array to figure out the binary encodings, then uses it to convert into ASCII characters to achieve the decoding process.
