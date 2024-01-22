from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

def ChessBoard(m, n):
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("*", end="  ")
            else:
                print("#", end="  ")
        print()

n = int(input("Enter first number(n): "))
m = int(input("Enter first number(m): "))
ChessBoard(m, n)