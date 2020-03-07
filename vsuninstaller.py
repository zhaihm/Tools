# Uninstaller of Microsoft Visual Studio
import sys, getopt
import os
import subprocess
import codecs

def usage():
    print('%s usage:' % sys.argv[0])
    print('-l list all product')

def getProducts():
    #resultLines = subprocess.call(['wmic', 'product', 'list']).split('\n')
    file = codecs.open('1.txt', 'r', 'utf-8')
    resultLines = file.readlines()
    file.close()
    print(resultLines)
    if len(resultLines) == 0:
        return

    headerLine = resultLines[0]
    headers = ('Description','IdentifyingNumber','InstallDate','InstallLocation','InstallState','Name','PackageCache','SKUNumber','Vendor','Version')
    indexes = []
    for i in range(len(headers)):
        indexes.append(headerLine.find(headers[i]))

    print(resultLines)

    products = []
    for i in range(1, len(resultLines)):
        product = []
        for j in range(len(headers)):
            endIndex = indexes[j + 1]
            if j + 1 == len(headers):
                endIndex = None
            curstr = resultLines[i][indexes[j] : endIndex]
            print(curstr)
            product.append(curstr)
        products.append(product)
    print(products)

opts, args = getopt.getopt(sys.argv[1:], "l")

for op, value in opts:
    if op == "-l":
        getProducts()
    else:
        usage()
        sys.exit()