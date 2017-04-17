import pandas as pd
import csv

#print ("Archivo 1")
#file = r'Python_scopus_dic_2017.csv'
#file = r'Python_Union.csv'
#df = pd.read_csv(file,names)


headers = ["Author","Title","C1","Abstract","C2","Cant02","Keywords","Cant03","Publication Title","Year"]
names = headers

df = pd.read_csv("XYZ.csv", header=0, names = headers)


# Resumen por archivo
x=0
for i in df['Abstract']:
    x+=1
    print (df.iloc[(x-1)]['Abstract'])


'''
#LISTA DE TITULOS
for i in df['Title']:
    print (i,'.')
'''

'''JUSMEIDY - Listado de los 42 artículos
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
