import PyPDF2
import sys

# with open('./PDF/dummy.pdf', 'rb') as file:
    # 'rb' is read binary, for pdf we append 'b' to 'r'.
    # so it converts the file to binary and PyPDF2 works with binary files.
#     reader = PyPDF2.PdfReader(file)
#     print(file) # <_io.BufferedReader name='./PDF/dummy.pdf'>
#     print(reader) #<PyPDF2._reader.PdfReader object at 0x000002766C5F38D0>
#     print(reader.pages) #<PyPDF2._page._VirtualList object at 0x000002766C6022D0>
#     print(len(reader.pages)) #1
#     print(reader.pages[0]) # acts as deprecated reader.getPage(0)
# {'/Type': '/Page', '/Parent': IndirectObject(4, 0, 2707647576272),
# '/Resources': IndirectObject(11, 0, 2707647576272), '/MediaBox': [0, 0, 595, 842],
# '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': True},
# '/Contents': IndirectObject(2, 0, 2707647576272)}

    # page = reader.pages[0]
    # page.rotate(90)
    # writer_output = PyPDF2.PdfWriter()
    # writer_output.add_page(page)
    #
    # with open('./PDF/tilt.pdf', 'wb') as new_file:
    #     writer_output.write(new_file)

# -------------------
# inputs = sys.argv[1:]
# this will store all the arguments passes except the first one, and store them in a list

# def pdf_merger(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('./PDF/merged2.pdf')
#
# pdf_merger(inputs)

# --------------------------------------------------------
# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# This is the new way to do this:
template = PyPDF2.PdfReader(open('./PDF/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('./PDF/wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

# for i in range(template.getNumPages()):

# New way to do this:
for i in range(len(template.pages)):
	page = template.pages[i]
	page.merge_page(watermark.pages[0])
	output.add_page(page)

with open('./PDF/watermaked_output2.pdf', 'wb') as outputFile:
	output.write(outputFile)