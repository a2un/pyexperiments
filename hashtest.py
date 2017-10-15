from hashlib import sha256

x = 5
y = 0

while sha256(str(x*y).encode()).hexdigest()[-1]!="0":
    print('{x*y}'.encode());
    print("dint work for y",y);
    y+= 1

print('The solution is y ='+ str(y));