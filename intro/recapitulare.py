from selenium import webdriver
from selenium.webdriver.common.by import By

a = 5
b = int(5)

PI = 3.14
print(int(PI))

string = str(5)
print(type(string))

print(float(a))

print(bool(1))
print(bool(3))
print(bool(4))
print(bool(0))

text_1 = "Cerul este senin"

"""
cuvant: C E R U L _ E S T E _  S  E  N  I  N
 index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""

print(text_1[::-1])

print("asdfsadfd")
print('asdfsadfd')
print("asdfs'a'dfd")

a = 10
assert a == 10

# Colectii in python

# Liste
lista_1 = [1, "sd", True, 3.14, True, 3.14]
print(lista_1)

# Tuplu
tuplu_1 = (1, 2, 3, 4, 5, 6, 6, 6, 6)
print(tuplu_1)


# Dictionare
dict_1 = {
    "Prenume": "Ion",
    "Nume": "Pop",
    "Varsta": 14,
    "Varsta": 24
}

print(dict_1)

# Set
set_1 = {1, 2 , 3, 4, 4, 4, 4, 4}
print(set_1)

a = 10
b = 5
c = 8

if a < b:
    print("Suntem pe if")
elif b < a:
    print("Suntem pe elif1")
elif c > b:
    print("Suntem pe elif2")
else:
    print("Suntem pe else")


numarator = 1

while numarator <= 10:
    print(numarator)
    numarator += 1  # numarator = numarator + 1
    if numarator == 9:
        break

print("--------------")

for i in range(10, 0, -2):
    print(i)


for x in lista_1:
    print(x)

class Masina:
    roti = 4
    usi = 5

class Vehicul:
    electric = True

class BMWX5(Vehicul, Masina):

    def __init__(self, cp):
        self.cp = cp


bmw = BMWX5(123)

driver = webdriver.Chrome()
driver.get("google.com")

x = driver.find_element(By.ID, "input")
x.send_keys("search text")



