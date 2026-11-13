from barcode import EAN13 
from barcode.writer import ImageWriter 
# number = "0000000000111"
number = '5901234123457'
number = ''
# my_code = EAN13(number, writer=ImageWriter()) 
my_code = EAN13(number, writer=ImageWriter()) 
my_code.save("result/03")

# res = ""
# counter = 1
# while counter < 7:
#     if counter < 10:
#         res = "000000000000" + str(counter) # 12 
#     elif counter < 100:
#         res = "00000000000" + str(counter) # 11
#     elif counter < 1000:
#         res = '0000000000' + str(counter) # 10
#     elif counter < 10000:
#         res = '000000000'+ str(counter) # 9
#     elif counter < 100000:
#         res = '00000000' + str(counter) # 8
#     elif counter < 1000000:
#         res = '0000000' + str(counter) # 7
#     elif counter < 10000000:
#         res = '000000' + str(counter) # 6
#     elif counter < 100000000:
#         res = '00000' + str(counter) # 5
#     elif counter < 1000000000:
#         res = '0000' + str(counter) # 4
#     elif counter < 10000000000:
#         res = '000' + str(counter) # 3
#     elif counter < 100000000000:
#         res = '00' + str(counter) # 2
#     else:# counter < 1000000000000:
#         res = '0' + str(counter) # 1
# ****************************************************
    # print(res)
    # my_code = EAN13(res, writer=ImageWriter())
    # full_path = "result/" + res
    # my_code.save(full_path)
    # # my_code.clear()

    # counter = counter + 1
    # print(res)
# ****************************************************
