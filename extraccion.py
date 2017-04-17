import pandas as pd
import csv

headers = ["Author","Title","C1","Abstract","C2","Cant02","Keywords","Cant03","Publication Title","Year"]
names = headers

df = pd.read_csv("CorpusCompleto_UNdeC.csv", header=0, names = headers)


# Resumen por archivo
x=0
for i in df['Abstract']:
    x+=1
    archivos = "Archivo_"+str(x)
    file = open(archivos,"w") 
    file.write(i)
    file.close() 

'''
# LISTADO DE Keywords
for i in df['Keywords']:
    x+=1
    print (i)
'''

'''
#LISTA DE TITULOS
for i in df['Title']:
    print (i,'.')
'''

''' Listado de los 42 artículos
x = 0
for i in df['Title']:
    x +=1
    print (x)
    print (df.iloc[(x-1)]['Author'])
    print ("- TÍTULO:\n",i)
    print (" Cantidad:", len(i.split(" ")))
    print ("- RESUMEN:\n",df.iloc[(x-1)]['Abstract'])
    print (" Cantidad:", len(str(df.iloc[(x-1)]['Abstract']).split(" ")))
    print ("- PALABRAS CLAVE:\n",df.iloc[(x-1)]['Keywords'])
    print ("- REVISTA:\n",df.iloc[(x-1)]['Publication Title'])                 
    print ("- AÑO:\n",df.iloc[(x-1)]['Year'])
    print ("\n\n\n")

'''
