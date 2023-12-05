
# fungsi untuk merubahnya menjadi angka hexadecimal
def hexa(num, length=2):
    h = hex(num).lstrip("0x").upper()
    h = "0" *(length-len(h)) + h
    return h

# fungsi untuk enkripsi pesan
def encript(plaintext, key):
    cipherHex=""
    keyLength = len(key)
    for i in range(0, len(plaintext)):
        j = i % keyLength
        xor = ord(plaintext[i]) ^ ord(key[j])
        cipherHex = cipherHex + hexa(xor) + " "
    return cipherHex

# fungsi untuk dekripsi pesan
def decrypt(cipherHex, key):
    decryptedAscii = ""
    cipherHexList = cipherHex.split()

    keyLength = len(key)

    for i in range(len(cipherHexList)):
        j = i % keyLength
        xor = int(cipherHexList[i], 16) ^ ord(key[j])
        decryptedAscii += chr(xor)

    return decryptedAscii


# fungsi untuk menu utama
def main():
   start = 1
   while start == 1:
        print("1. enkripsi \n2. dekripsi \n0. exit")
        menu = input("masukan perintah (pakai nomer)")
        if menu == "1":
            plaintext = input("masukan pesan yang akan dienkripsi:\n")
            key= input("masukan input kuncinya:\n") 
            print(encript(plaintext, key))
        elif menu == "2":
            plaintext = input("masukan pesan yang akan didekripsi:\n")
            key= input("masukan input kuncinya:\n")
            print(decrypt(plaintext, key))
        elif menu == "0":
            start=0

        else:
            print("masukan nomer yang benar")

if __name__ == '__main__':
    main()

