import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf = wi(filename = "AvradeepGupta.pdf", resolution = 300)   # To read the pdf file and create a pdf object
pdfImage = pdf.convert('jpeg')                               # To convert the pdf to a pdf of images of jpeg format

imageBlobs = []                                              # Empty List to store each page

for img in pdfImage.sequence:
    imgPage = wi(image= img)                                 # To retrieve the actual image and not the object definition
    imageBlobs.append(imgPage.make_blob('jpeg'))             # Append to the ImageBlobs and to make the binary string of the image

recognized_text = []                                         # List of recognized text for each page

for imgBlob in imageBlobs:                                   # Iterate for all the Images
    im = Image.open(io.BytesIO(imgBlob))                     # Using PIL library and using io to open the image
    text = pytesseract.image_to_string(im, lang='eng')       # Convert the image to string
    recognized_text.append(text)                             # Appending the text content for each image

print(recognized_text)                                       # Printing the entire list

#Image_To_Text
#im = Image.open("acknowledgement.png")
#text = pytesseract.image_to_string(im, lang='eng')

#print(text)