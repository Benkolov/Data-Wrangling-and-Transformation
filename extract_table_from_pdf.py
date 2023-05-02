import camelot as cl
import pandas as pd

table = cl.read_pdf('raw_data/proforma Garnish 01.05 updated.pdf', pages='all', flavor='stream')

print(table)

# Ако имате 4 таблиците
table_0 = table[0].df
table_1 = table[1].df
table_2 = table[2].df
table_3 = table[3].df


# Принтирайте данните от всяка таблица
# print("Table 0:")
# print(table_0)
# print("\nTable 1:")
# print(table_1)
# print("\nTable 2:")
# print(table_2)
# print("\nTable 3:")
# print(table_3)

with pd.ExcelWriter('output_tables.xlsx', engine='openpyxl') as writer:
    table_0.to_excel(writer, sheet_name='Table 0', index=False)
    table_1.to_excel(writer, sheet_name='Table 1', index=False)
    table_2.to_excel(writer, sheet_name='Table 2', index=False)
    table_3.to_excel(writer, sheet_name='Table 3', index=False)
