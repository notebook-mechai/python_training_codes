import treepoem
#image = treepoem.generate_barcode(barcode_type="code128",data="barcode payload",)
#image.convert("1").save("one.png")
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
res = ""
counter = 6454
# 000 001
while counter <= 999999:
     if counter < 10:
         res = "00000" + str(counter) # 5 
     elif counter < 100:
         res = "0000" + str(counter) # 4
     elif counter < 1000:
         res = '000' + str(counter) # 3
     elif counter < 10000:
         res = '00'+ str(counter) # 2
     elif counter < 100000:
         res = '0' + str(counter) # 1
     else: 
         res = str(counter) # 0
# ****************************************************
     full_path = "pta_photos/" + res + ".png"
     image = treepoem.generate_barcode(barcode_type="code128",data=res,)
     image.convert("1").save(full_path)
     counter = counter + 1

