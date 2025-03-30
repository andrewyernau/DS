import pandas as pd

edades = pd.Series(
    [28, 21, 22],
    index= ['Pedro','Marcos','María'],
    name='edad'
)

print(edades)
esperanza_adicional = pd.Series(
    [53.4,65.6,64.5],
    index=['Pedro','Marcos','María'],
    name='edad'
) 

print(edades+esperanza_adicional)

s1 = pd.Series(
    [3,2.5,-1,10],
    index=['a','b','c','b']
)

s2 = pd.Series(
    [1,0.5,2],
    index=['b','c','b']
)

print(s1+s2)

##DataFrame

personas = pd.DataFrame(
    [[28,53.4],[21,65.6],[22,64.5],[22]],
    index=['Pedro','Maria','Marta','Mateo'],
    columns=['edad','esperanza_adicional']
)

#Con diccionario
personas2 = pd.DataFrame(
    {
        'edad':[28,21,22],
        'esperanza_adicional':[53.4,65.6,64.5]
    },
    index=['Pedro','Maria','Marta']
)

personas3 = pd.DataFrame(
    {
        'edad':edades.values,
        'esperanza_adicional':esperanza_adicional.values
    },
    index=['Pedro','Maria','Marta']
)

print(personas.info()) #.describe(), .head(N), .tail(N),.shape(),.columns,.index,.row,.values,.dtypes
print("Personas 2:")
print(personas2)
print("Personas 3:")
print(personas3)


print(personas.dropna(axis=1,how='all'))