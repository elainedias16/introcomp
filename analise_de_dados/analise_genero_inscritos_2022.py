import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
import codecs

male = 0
female = 0
other = 0

with codecs.open("inscricoes_2022-06-27T20_46_37.csv",  encoding = 'cp850') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') 
    for line in reader:
        if "female" in line:
            female = female + 1
        elif "male" in line:
            male = male + 1
        elif "female" not in line and "male" not in line:
            other = other + 1


other = other - 1 #to decrease title' line

print('Quantity of female is ', female)
print("\n")
print('Quantity of male is ' , male)
print("\n")
print('Quantity of others is ', other)

gender = ['Male', 'Female', 'Other']
qtd = [male, female, other]

plt.bar(gender, qtd)
plt.show()



