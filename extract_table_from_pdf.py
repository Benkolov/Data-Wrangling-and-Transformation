import camelot as cl
import pandas as pd

table = cl.read_pdf('raw_data/SUMMER OFFERS 2023_web.pdf', pages='all', flavor='stream')

print(table)

# Ако имате 4 таблиците
table_0 = table[0].df
table_1 = table[1].df
table_2 = table[2].df
table_3 = table[3].df
table_4 = table[4].df
table_5 = table[5].df
table_6 = table[6].df
table_7 = table[7].df
table_8 = table[8].df
table_9 = table[9].df


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
    table_4.to_excel(writer, sheet_name='Table 4', index=False)
    table_5.to_excel(writer, sheet_name='Table 5', index=False)
    table_6.to_excel(writer, sheet_name='Table 6', index=False)
    table_7.to_excel(writer, sheet_name='Table 7', index=False)
    table_8.to_excel(writer, sheet_name='Table 8', index=False)
    table_9.to_excel(writer, sheet_name='Table 9', index=False)
