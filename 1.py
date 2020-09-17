
import csv
import os
from pathlib import Path

PARENT_DIR = Path(__file__).parent

users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
fields = users[0].keys()

file_path = os.path.join(PARENT_DIR, 'users.csv')
with open(file_path, 'w') as f:
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in users:
        writer.writerow(user)


for file_ in os.listdir(PARENT_DIR):
    os.path.join(PARENT_DIR, file_)
