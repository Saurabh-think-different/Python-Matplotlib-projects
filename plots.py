import matplotlib.pyplot as plt 

#open file name
f = open("file_name.txt", "r")

#initialize array elements to 0
array = []
for i in range(0,26):
    array.append(0)


#main starts
for elem in f.read():
    c = ord(elem.upper())
    if(c >= 65 and c <= 97):
        temp = c
        temp -= 65
        array[temp] += 1


#alphas array to initialize all elements to upper-case alphabet letters
alphas = []

for i in range(0,26):
    c = chr(i+65)
    alphas.append(c)


#plotting and showing the array
plt.bar(alphas , array)
plt.show()
