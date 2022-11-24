# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

# baca file csv secara streaming
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())

    reader = csv.reader(f, delimiter=',')

    # membaca baris per baris
    # for row in reader:
    #     print(row)

# tentukan lokasi file, nama file, dan inisialisasi csv
# f = open('https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv', 'r')
# reader = csv.reader(f)

# membaca baris per baris
# for row in reader:
#     print(row)

# # menutup file csv
# f.close()

pd.set_option("display.max_columns", 50)

table = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
# print(table)

# %%
table = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

plt.show()

# %%
