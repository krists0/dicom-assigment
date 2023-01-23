import pydicom
import csv
import numpy as np
from PIL import Image


# Read dcm file
dicom_file = pydicom.dcmread("HomeEx.dcm")


print(dicom_file)

# Save the information to a CSV file
with open("dicom.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)  
    writer.writerow(dicom_file)
 
#show the image
image = dicom_file.pixel_array
image = image.reshape(image.shape[0] * image.shape[1], image.shape[2])
image = Image.fromarray(image)
image.show()

#resize the image
image = np.array(image)
image = Image.fromarray(image)
image = image.resize((image.size[0]//2, image.size[1]//2))
image = np.array(image)

#change the color



# Rotate the image
image = np.array(image)
image = np.rot90(image)
image = Image.fromarray(image)
image.show()





"""
image = dicom_file.pixel_array
plt.imshow(image, cmap='gray')
plt.show()"""
