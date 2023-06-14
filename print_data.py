# name = "Aysel"
# age = 20
# print("telebenin adi", name, "ve yasi", age, "-dir")
# telebenin adi Aysel ve yasi 20-dir.
name1 = input("ad daxil edin: ")
age1 = int(input("yas daxil edin: "))
# print("telebenin adi", name1, "ve yasi", age1, "-dir")
# print("telebenin adi "+ name1+ " ve yasi "+ str(age1)+ "-dir")
print("Telebenin adi {} ve yasi {}-dir".format(name1, age1))
print("Telebenin adi {1} ve yasi {0}-dir".format(age1,name1))

a=int(input("1-ci ededi daxil edin: "))
b=int(input("2-ci ededi daxil edin: "))
print("1-ci eded {} , 2-ci eded {}, cemi {}-dir".format(a,b,a+b))
