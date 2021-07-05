import hashlib

text = input("Enter text here : ")
salt = "salt123"
join = text + salt

print("md5 : " + hashlib.md5(join.encode('utf-8')).hexdigest())
print("sha256 : " + hashlib.sha256(join.encode('utf-8')).hexdigest())
print("sha512 : " + hashlib.sha512(join.encode('utf-8')).hexdigest())