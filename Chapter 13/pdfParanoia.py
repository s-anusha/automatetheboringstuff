#! python 3
# pdfParanoia.py
'''
Using the os.walk() function from Chapter 9, write a script that will go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename. Before deleting the original file, have the program attempt to read and decrypt the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password. If the password is incorrect, the program should print a message to the user and continue to the next PDF.
'''
# Usage: python pdfParanoia.py folder_path

import os
import PyPDF2
import sys

if len(sys.argv) < 2:
    print("Usage: python pdfParanoia.py folder_path")
    sys.exit()

folder = sys.argv[1]

print('Part 1: Encryption\n')
for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            print('Enter password for ' + filename + ': ')
            password = input()
            print('Encrypting file...')
            pdfWriter.encrypt(password)
            newFilename = filename[:len(filename) - 4] + '_encrypted.pdf'
            resultPdf = open(newFilename, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfFile.close()
            print('Testing encryption...')
            checkPdfReader = PyPDF2.PdfFileReader(open(newFilename, 'rb'))
            if checkPdfReader.isEncrypted is False:
                print('Encryption of ' + filename + ' failed.')
            else:
                checkPdfReader.decrypt(password)
                try:
                    pageObj = checkPdfReader.getPage(0)
                    print('Encryption success.\nDeleting original file...')
                    os.unlink(os.path.abspath(filename))
                    print('Done.')
                except PyPDF2.utils.PdfReadError:
                    print('Failed to retrieve page object from encrypted ' + filename)
print('Part 1 complete.\n')

print('Part 2: Decryption\n')
for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted is False:
                print('File not encrypted.')
            else:
                print('Enter password for ' + filename + ': ')
                password = input()
                print('Decrypting file...')
                if pdfReader.decrypt(password) is 0:
                    print('Decryption failed.')
                else:
                    print('Decryption success.\nCreating a copy...')
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    newFilename = filename[:len(filename) - 14] + '.pdf'
                    resultPdf = open(newFilename, 'wb')
                    pdfWriter.write(resultPdf)
                    resultPdf.close()
                    print('Done.')
            pdfFile.close()     
print('Part 2 complete.')
