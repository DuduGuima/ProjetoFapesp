# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:33:22 2024

@author: Eduardo
"""
import os
import numpy as np
import csv
import pandas as pd


def load_from_csv(file_path):
    data_list = []
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header if it exists
        header = next(csv_reader, None)

        for row in csv_reader:
            data_list.append(row)
    
    return data_list

def read_specific_line_pandas(csv_file, line_number):
    # Read the entire CSV file into a DataFrame
    cols = ['date','years','FOPT', 'FWPT','TCPU']
    df = pd.read_csv(csv_file,skiprows=1, sep='\s+')

    # Check if the specified line number is valid
    if 1 <= line_number <= len(df):
        # Extract the specific line using iloc
        specific_line = df.iloc[line_number - 1]
        return specific_line
    else:
        return None
    
def save_to_csv(file_path, data_list):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Column1', 'Column2', 'Column3'])  # Replace with your column names

        for item in data_list:
            csv_writer.writerow(item)
    
inputs_krw=np.zeros((5,15))

    
arquivo_krw = "KRW0.INC"
resultado = pd.read_csv(arquivo_krw,skiprows=1, header=None,sep='\s+')[1][:15].to_numpy()

inputs_krw[0]= np.array( [i for i in resultado] )



for i in range(1,5):    
    for j in range(15):
        arquivo_krw=arquivo_krw.replace(str(i-1),str(i))
        resultado = pd.read_csv(arquivo_krw,skiprows=1, header=None,sep='\s+')[1][:15].to_numpy()
        inputs_krw[i]= np.array( [i for i in resultado] )

print(inputs_krw)

inputs_pvt=np.zeros((3,19*7 ))

arquivo_pvt= "pvt_0.INC"
resultado=pd.read_csv(arquivo_pvt,nrows=19,skiprows=3,header=None,sep='\s+')

resultado = resultado.values.reshape(1,-1)

inputs_pvt[0] = np.array([np.float64(i) for i in resultado])

for i in range(1,3):
    arquivo_pvt=arquivo_pvt.replace(str(i-1),str(i))
    if (i==1):
        resultado=pd.read_csv(arquivo_pvt,nrows=19,skiprows=3,header=None,sep='\s+')
    else:
        resultado=pd.read_csv(arquivo_pvt,nrows=19,skiprows=3,header=None,sep='\s+')
    resultado = resultado.values.reshape(1,-1)
    inputs_pvt[i] = np.array([np.float64(i) for i in resultado])
    
#as combinacoes estao salvas em inputs_krw e inputs_pvt
#agora e so colocar tudo num novo arquivo csv de input, q vou usar pra treinar tudo

combinacoes = load_from_csv("incertezas.csv")
combinacoes = np.int32(combinacoes)
#inputs_finais=np.zeros((len(combinacoes)))
inputs_finais=np.empty((0, 1 + 19*7 +np.shape(inputs_krw)[1] ))

for i in range(len(combinacoes)):
    inputs_finais=np.append(inputs_finais,
                            [np.append(combinacoes[i][0],
                                      np.append(inputs_pvt[combinacoes[i][1]],inputs_krw[combinacoes[i][2]]) )],axis=0)



#save_to_csv("inputs_finais.csv", inputs_finais)

teste=load_from_csv("inputs_finais.csv")

