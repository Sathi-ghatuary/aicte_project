import cv2
import os


img_path = r"C:\Users\Pratik Erande\Downloads\Stenography-main\Stenography-main\mypic.jpeg"
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found. Check the file path!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}


height, width, channels = img.shape


if len(msg) > height * width:
    print("Error: Message too long to fit in the image!")
    exit()


index = 0
for i in range(len(msg)):
    x = index % width  # Column
    y = index // width  # Row

    img[y, x, 0] = d[msg[i]]  # Modify only the Blue channel
    index += 1

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open image (Windows only)

# Decryption process
message = ""
index = 0
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        x = index % width
        y = index // width

        message += c[img[y, x, 0]]  # Read from Blue channel only
        index += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
