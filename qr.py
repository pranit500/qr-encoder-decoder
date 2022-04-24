import qrcode   
# example data
data = "https://www.edcbitmesra.in/"
# output file name
filename = "qr.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

