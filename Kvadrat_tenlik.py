# Verilir kvadrat tənlik. ax2+bx+c=0 şəklində. a,b,c əmsalları aşağıdakı kimidir.
text0 = "Verilir kvadrat tənlik. ax2+bx+c=0 şəklində."
text1 = "a=1, b=-5, c=6 olsun."
print(text0)
print(text1)
a1, b1, c1 = 1, 5, 6
D1 = b1**2 - 4 * a1 * c1
print(D1)
text2 = "D=1>0 olduğu üçün tənliyin iki kökü var."
print(text2)
# D=1>0 olduğundan tənliyin iki kökü var.
# Tənliyin kökləri x1 və x2 olsun.
x1 = (-b1 - D1 ** (1 / 2)) / (2 * a1)
x2 = (-b1 + D1 ** (1 / 2)) / (2 * a1)
print(x1, x2)
print("---------------------------")
text3 = "İndi isə a=1, b=-10, c=25 olsun"
print(text3)
a2, b2, c2 = 1, -10, 25
D2 = b2**2 - 4 * a2 * c2
print(D2)
text4 = "D=0 olduğundan tənliyin iki bərabər kökü var."
print(text4)
x = (-b2) / (2 * a2)
print(x)
print("x=5")
print("---------------------------")
text4 = "İndi isə a=1, b=2, c=11 olsun"
print(text4)
a3, b3, c3 = 1, 2, 11
D3 = b3**2 - 4 * a3 * c3
print(D3)
text5 = "D=-40<0 olduğundan tənliyin həlli yoxdur."
print(text5)