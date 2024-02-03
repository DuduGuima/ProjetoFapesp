# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:05:49 2024

@author: Eduardo
"""

import os
import numpy as np
import csv
import pandas as pd

def save_to_csv(file_path, data_list):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Column1', 'Column2', 'Column3'])  # Replace with your column names

        for item in data_list:
            csv_writer.writerow(item)

def read_specific_line_pandas(csv_file, line_number):
    # Read the entire CSV file into a DataFrame
    cols = ['date','years','FOPT', 'FWPT','TCPU']
    df = pd.read_csv(csv_file,skiprows=9,names=cols, sep='\s+')

    # Check if the specified line number is valid
    if 1 <= line_number <= len(df):
        # Extract the specific line using iloc
        specific_line = df.iloc[line_number - 1]
        return specific_line
    else:
        return None

def read_specific_line(csv_file, line_number):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None

def load_from_csv(file_path):
    data_list = []
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header if it exists
        header = next(csv_reader, None)

        for row in csv_reader:
            data_list.append(row)
    
    return data_list

objetivos=[]
raiz_pasta = "output"
arquivo="UNISIM-I-D_OPM-FLOW.RSM"    

for i in range(1,499):
    raiz_final = raiz_pasta + str(i) + "/" + arquivo
    resultado = read_specific_line_pandas(raiz_final, 34)
    objetivos.append([resultado['FOPT'],
                  resultado['FWPT']])
        
    

        
#o indice sempre vai ser 20 pra prod de oleo do campo
#o outro indice, da prod de auga é 34

# resultado = [read_specific_line(arquivo, 88)[0].split(" ")[20],
#              read_specific_line(arquivo, 131)[0].split(" ")[34]]
# print(resultado)

# resultado = read_specific_line_pandas(arquivo, 34)
# cols = ['date','years','FOPT', 'FWPT','TCPU']
# resultado= pd.read_csv(arquivo,skiprows=9, sep= "\s+",names=cols)
objetivos=np.array(objetivos)/1000
print(objetivos)

save_to_csv("targets_finais.csv", objetivos)

# teste=pd.read_csv("targets_finais.csv")

# print(teste)