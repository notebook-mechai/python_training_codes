import pyqrcode
from pyqrcode import QRCode

# -*-*-*-*-*-*-*-*-*-*-*-
raw_text_ha = "HA"
i_ha = 1
zero_ha = "0"
while i_ha < 15:
    if i_ha < 10:
        main_text_ha = raw_text_ha + zero_ha + str(i_ha)
    else:
        main_text_ha = raw_text_ha + str(i_ha)
    i_ha = i_ha + 1
    myQR = QRCode(main_text_ha, error='H', version=None, mode=None, encoding='iso-8859-1')
    file_name = main_text_ha + ".png"
    full_path = "photo/HA/" + file_name
    myQR.png(full_path, scale=16)


# -*-*-*-*-*-*-*-*-*-*-*-
raw_text_bt = "BT"
i_bt = 1
zero_bt = "0"
while i_bt < 31:
    if i_bt < 10:
        main_text_bt = raw_text_bt + zero_bt + str(i_bt)
    else:
        main_text_bt = raw_text_bt + str(i_bt)
    i_bt = i_bt + 1
    myQR = QRCode(main_text_bt, error='H', version=None, mode=None, encoding='iso-8859-1')
    file_name = main_text_bt + ".png"
    full_path = "photo/BT/" + file_name
    myQR.png(full_path, scale=16)


# -*-*-*-*-*-*-*-*-*-*-*- 
raw_text_tr = "TR"
i_tr = 1
zero_two_tr = "00"
zero_tr = "0"
while i_tr < 501:
    if i_tr < 10:
        main_text_tr = raw_text_tr + zero_two_tr + str(i_tr)
    elif i_tr > 9 and i_tr < 100:
        main_text_tr = raw_text_tr + zero_tr + str(i_tr)
    else:
        main_text_tr = raw_text_tr + str(i_tr)
    # print(main_text)
    i_tr = i_tr + 1
    myQR = QRCode(main_text_tr, error='H', version=None, mode=None, encoding='iso-8859-1')
    file_name = main_text_tr + ".png"
    full_path = "photo/TR/" + file_name
    myQR.png(full_path, scale=16)

#myQR = QRCode(text, error='H', version=None, mode=None, encoding='iso-8859-1')
#myQR.png('qrcode2.png', scale=10)