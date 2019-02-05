import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode("csdn.jpeg")
print(barcode.parsed)
