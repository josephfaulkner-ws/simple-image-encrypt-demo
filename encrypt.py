from cryptography.fernet import Fernet

key = "w6mvoM7vhOjIBN1ejHPdMiUTya8RMaAB_ptvAqXMLgg="
f = Fernet(key)

unencryptedFile = open('testImageFile.jpg', 'rb')
unencryptedFileContents = unencryptedFile.read()

encryptedFileContents =  f.encrypt(unencryptedFileContents)

encryptedFile = open('encryptedImageFile.jpg', 'wb')
encryptedFile.write(encryptedFileContents)