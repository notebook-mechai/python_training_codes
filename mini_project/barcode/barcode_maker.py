import treepoem
res = ""
counter = 1000000
while counter <= 1002209:
     full_path = "amin_photos/" + str(counter) + ".png"
     image = treepoem.generate_barcode(barcode_type="code128",data=str(counter),)
     image.convert("1").save(full_path)
     counter = counter + 1