name1 = "Aysel"
print(name1)
print(type(name1))
# text1="My dog name is "Tom"" - yanlis
text1 = 'My dog name is "Tom"'
print(text1)
print(type(text1))
# text2='I'm a student' - yanlis
text2 = "I'm a student"
print(text2)
print(name1[0])
print(name1[3])
print(text1[7])
# indeksleme 0-dan baslayir ve [] isaresi altinda yazilir
print(text1[15])
# len stringin uzunlugunu gosteren funksiyadir. yeni nece simvol oldugunu
print(len(name1))
# uzunluq sonuncu indeksden 1 vahid cox olur
print(len(text1))
print(text1[18])
# sonlugun qeyd olunan simvoldan 1 evvelkini goturur, amma baslangicda ozunu
print(text2[6:12])
print(text2[6:13])
print(text2[6:])
print(text2[6 : len(text2)])
print(len(text2))
print(text1[0:6])
print(text1[:6])
numbers = "0123456789"
print(numbers[:5:2])
print(numbers[:5:3])
print(numbers[2::2])
print(numbers[1::2])
print(name1[::])
print(name1[:])
print(name1[:9])
print(name1[0:9])
print(name1[0:])
# Tersden cap etmek ucun asagidaki kimi etmek lazimdir
print(name1[::-1])
