from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

s1 = int(input("Enter the size of the fist side: "))
s2 = int(input("Enter the size of the second side: "))
s3 = int(input("Enter the size of the third side: "))

sumS = s1 + s2
sumS2 = s2 + s3
sumS3 = s1 + s3
if sumS > s3:
    print("Possible to draw.")
elif sumS2 > s1:
    print("Possible to draw.")
elif sumS3 > s2:
    print("Possible to draw.")
else:
    print("Impossible to draw!")