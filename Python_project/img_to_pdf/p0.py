# from fpdf import FPDF

# pdf = FPDF()

# imagelist = ["youtube.png","img1.jpg", "img2.jpg", "img3.jpg"]  # 👈 define this

# for image in imagelist:
#     pdf.add_page()
#     pdf.image(image, x=0, y=0, w=210, h=297)

# pdf.output("output.pdf")


import os
from fpdf import FPDF

pdf = FPDF()

folder_path = "images"

imagelist = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))]

for image in imagelist:
    pdf.add_page()
    pdf.image(os.path.join(folder_path, image), x=0, y=0, w=210, h=297)

pdf.output("output.pdf")

print("PDF created successfully!")