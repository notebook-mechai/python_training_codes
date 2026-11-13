from asposebarcode import Generation, Assist
# Setting License
licenseBarCode = Assist.License()
licenseBarCode.setLicense("Aspose.Total.lic")

# Instantiate BarCodeGenerator class object with Barcode Encode Type CODABAR
encode_type = Generation.EncodeTypes.CODABAR
GenerateBarCode = Generation.BarcodeGenerator(encode_type, None)

# Set BarCode text to be encoded
GenerateBarCode.setCodeText("Python Test Barcode")

# Set resolution
GenerateBarCode.getParameters().setResolution(300)

#BarCodeImageFormat.PNG.value
file_path = "OutputBarCode.png"
imageFormat= Generation.BarCodeImageFormat(3)

# Saving the BarCode in PNG image format
# Aspose.Barcode for Python via Java API supports multiple image formats for saving the output BarCode
GenerateBarCode.save(file_path, imageFormat)




