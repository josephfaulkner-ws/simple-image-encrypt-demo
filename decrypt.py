from cryptography.fernet import Fernet

key = "w6mvoM7vhOjIBN1ejHPdMiUTya8RMaAB_ptvAqXMLgg="
f = Fernet(key)

encryptedFile = open('encryptedImageFile.jpg', 'rb')
encryptedFileContents = encryptedFile.read()

unencryptedFileContents =  f.decrypt(encryptedFileContents)

unencryptedFile = open('testImageFileDecrypt.jpg', 'wb')
unencryptedFile.write(unencryptedFileContents)