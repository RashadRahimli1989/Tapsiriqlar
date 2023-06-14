# Verilir kvadrat tənlik. ax2+bx+c=0 şəklində. a,b,c əmsalları aşağıdakı kimidir.
text = "Verilir kvadrat tənlik. ax2+bx+c=0 şəklində."
print(text)
a = int(input("a-ni daxil edin "))
b = int(input("b-ni daxil edin "))
c = int(input("c-ni daxil edin "))
# print("Tenlik {}x2+{}x+{}=0 seklindedir".format(a,b,c))
D = b**2 - 4 * a * c
print("kvadrat tenliyin diskriminanti {}-dir".format(D))
