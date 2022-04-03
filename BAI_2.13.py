print("NHAP A")
a = int(input())
print("NHAP B")
b = int(input())
print("NHAP C")
c = int(input())
if a == 0:
    if b == 0:
        print("PHUONG TRINH VO NGHIEM")
    else:
        x = -c / b
        print("x=" + str(x))
else:
    dELTA = b ** 2 - 4 * a * c
    print("DELTA=" + str(dELTA))
    if dELTA < 0:
        print("PHUONG TRINH VO NGHIEM")
    else:
        if dELTA >= 0:
            x1 = (-b + sqrt(dELTA)) / (2 * a)
            print("x1=" + str(x1))
            x2 = (-b - sqrt(dELTA)) / (2 * a)
            print("x2=" + str(x2))
        else:
            print("PHUONG TRINH VO NGHIEM")
