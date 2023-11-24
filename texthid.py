import cv2
import os
import string

img = cv2.imread("indian.jpg")

msg = input("Enter secreat message : ")

password = input("Enter password : ")
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}


m, n, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n, m, z = n + 1, m + 1, (z + 1) % 3

cv2.imwrite("Encryptedmsg.jpg", img)
os.system("start Encryptedmsg.jpg")
print("the image is encrypted sucessfully")


message = ""
m, n, z = 0, 0, 0

pas = input("Enter passcode for Decryption : ")

if password == pas:
    for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n, m, z = n + 1, m + 1, (z + 1) % 3
    print("decryption messeage is :", message)
else:
    print("it is invalid password")
