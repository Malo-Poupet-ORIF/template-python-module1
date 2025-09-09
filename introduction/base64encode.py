import base64
def encode(a):
    a = a.encode('utf-8')
    a = base64.b64encode(bytes(a))
    return(a)
def decode(a):
    a = a.encode('utf-8')
    a = base64.b64decode(bytes(a))
    return(a)
def main():
    opt = input ("Encode or decode? : ").lower()
    if opt == "encode".lower():
        enc = input("Enter text : ")
        print(encode(enc))
    elif opt == "decode".lower():
        dec = input("Base64 to decode : ")
        print(decode(dec))
    else:
        print("Option please")
        main()
main()