from pikepdf import Pdf, Name, PdfImage
import cv2
import os
import glob
import numpy as np
pdf_path = "C:/LegalBrain/ViewJournal2105.pdf"
output_dir = "C:/LegalBrain/Trade/"
final_dir = "C:/LegalBrain/TradeImages/"
pdf = Pdf.open(pdf_path)
page = pdf.pages
files = os.listdir(output_dir)
os.environ['OPENCV_IO_ENABLE_JASPER'] = 'true'
# for pg in range(11, 12):
#     keys = list(page[pg].images.keys())
#     print(keys)
#     raw_img = page[pg].images[keys[0]]
#     pdf_img = PdfImage(raw_img)
#     pdf_img.extract_to(fileprefix=output_dir + "Image" + str(0))
i = 0
for pg in range(11, len(page)):
    keys = list(page[pg].images.keys())
    print(keys)
    k = 0
    #['/X13', '/X14']
    if len(keys) >= 2:
        k = 0
        for p in keys:
            raw_img = page[pg].images[p]
            pdf_img = PdfImage(raw_img)
            pdf_img.extract_to(fileprefix=output_dir + "Image" + str(k))
            k += 1
        files = os.listdir(output_dir)
        haha = 0
        assemble = []
        for f in files:
            (n , e) = os.path.splitext(f)
            if e == ".jp2":
                image = cv2.imread(output_dir + 'Image' + str(haha) + '.jp2')
                cv2.imwrite(output_dir + 'Image' + str(haha) + '.png', image)
                whatdidusay = cv2.imread(output_dir + "Image" + str(haha) + ".png")
                assemble.append(whatdidusay)
                haha += 1
        if len(assemble) == 0:
            huhu = 0
            for f in files:
                whatdidusay = cv2.imread(output_dir + "Image" + str(huhu) + ".png")
                assemble.append(whatdidusay)
                huhu += 1
        new_img = cv2.vconcat(assemble)
        cv2.imwrite(final_dir + "Image" + str(pg) + ".png", new_img)
        i += 1
        # what = cv2.imread(final_dir + "NewImage.png")
        #Delete all files
        # files = os.listdir(output_dir)
        for f in files:
            os.remove(output_dir + f)
    elif len(keys) == 1:
        raw_img = page[pg].images[keys[0]]
        pdf_img = PdfImage(raw_img)
        pdf_img.extract_to(fileprefix=output_dir + "Image" + str(k))
        files = os.listdir(output_dir)
        for f in files:
            (name, extension) = os.path.splitext(f)
            myimg = cv2.imread(output_dir + name + extension)
            cv2.imwrite(final_dir + "Image" + str(pg) + ".png", myimg)
            i += 1
        for f in files:
            os.remove(output_dir + f)

