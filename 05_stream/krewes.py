"""
Amanda Tan
Elmo's Cheez-it
SoftDev
05_bitsream
2024-09-17
time spent: 0.5
"""

import random

f = open("krewes.txt", "r")
people = f.read().replace("\n", "").split('@@@')
for count, person in enumerate(people):
    people[count] = person.split('$$$')
    people[count] = {"period":people[count][0],
                     "devo":people[count][1],
                     "ducky":people[count][2]}

randoDevo = random.randint(0, len(people)-1)

print("Name: " + people[randoDevo].get("devo") + " | Period: " + people[randoDevo].get("period") + " | Ducky: " + people[randoDevo].get("ducky"))
