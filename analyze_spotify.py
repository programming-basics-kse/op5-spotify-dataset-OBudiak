import csv
import ast

rows = []
# with open('top_50_2023.csv', 'r') as file:
#     columns = next(file)
#     for line in file:
#         lines.append(line[:-1].split(','))

with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(file)
    print(header)
    header = header.split(',')
    print(header)
    for row in csv_reader:
        rows.append(row)
'''
is_explicit = float(header.index('is_explicit'))
list_is_explicit = 0

for row in rows:
    print(row)
    print(is_explicit)
    inf = row[is_explicit]
    print(row)
    if inf == 'True':
        list_is_explicit += 1
print(list_is_explicit)

# danceability = header.index('danceability')
# sum_dance = 0
#
# for row in rows:
#     num = float(row[danceability])
#     if num > 0.5:
#         sum_dance += float(row[danceability])'''

# counter = []
# idx = header.index('popularity')

# # Task 2
# for row in rows:
#     if float(row[7]) > 0.5:
#         counter.append(float(row[11]))
# print(sum(counter)/len(counter))

# Task 3
# counter = {}
#
# for row in rows:
#     artist = row[0]
#     if artist in counter:
#         counter[artist] += 1
#     else:
#         counter[artist] = 1
#
# top = sorted(counter.items(), key = lambda x: x[1], reverse = True)
# print(top[0])

# for row in rows:

#     row[4] = ast.literal_eval(row[4])
#     for i in row[4]:
#         if i in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1
#
# top = sorted(counter.items(), key = lambda x: x[1], reverse = True)
# print(top[:3])


# Task 5
# counter = {}
#
# for row in rows:
#     year = row[3][:4]
#     if year in counter:
#         counter[year] += 1
#     else:
#         counter[year] = 1
#
# top = sorted(counter.items(), key = lambda x: x[1], reverse = True)
# print(top[0][0])