from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

fn = int(input("Enter first number: "))
sn = int(input("Enter second number: "))
if fn > sn:
    bmm = fn
else:
    bmm = sn
while fn % bmm != 0 or sn % bmm != 0:
    bmm -= 1
print("bmm", fn, "va", sn, "=", bmm)