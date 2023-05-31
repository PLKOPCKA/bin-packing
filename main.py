from packer import newPacker

import matplotlib.pyplot as plt
from openpyxl import load_workbook
import pandas as pd

df_pal = pd.read_excel(open('C:/Users/PLKOPCKA/PycharmProjects/bin-packing/Input_Data.xlsx', 'rb'), sheet_name='Pallets')
df_truck = pd.read_excel(open('C:/Users/PLKOPCKA/PycharmProjects/bin-packing/Input_Data.xlsx', 'rb'), sheet_name='Trucks')

pallets = []
trucks = []

for index, row in df_pal.iterrows():
    for i in range(1, int(row[4])+1):
        pallets.append((row[1], row[2], row[3], row[0]))

for index, row in df_truck.iterrows():
    trucks.append((row[1], row[2], row[3], row[4], row[0]))

packer = newPacker(rotation=False)

# Add the rectangles to packing queue
for r in pallets:
    packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in trucks:
    packer.add_bin(*b)

# Start packing
packer.pack()

# Full rectangle list with coordinates
all_rects = packer.rect_list()

# Pallets with dimensions
all_pals = [sorted([p[3], p[4]]) for p in all_rects]

def plot_solution(all_rects):
    # Loop all rect
    plt.figure(figsize=(2, 10))
    for rect in all_rects:
        print(rect)
        n, x, y, w, h, rid, weight = rect
        x1, x2, x3, x4, x5 = x, x + w, x + w, x, x
        y1, y2, y3, y4, y5 = y, y, y + h, y + h, y
        color = '--k'
        plt.plot([x1, x2, x3, x4, x5], [y1, y2, y3, y4, y5], color)
    plt.show()

plot_solution(all_rects)




