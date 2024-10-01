import pandas as pd

colors= pd.Series(["red","yellow","pink","orange","black"])

print(colors)

print(colors[0])
 

#dataFrames - it is  a whole table

data ={
     'calories':[420,436,390] ,
     "duration":[40,56,76],
     
       }
myvar= pd.DataFrame(data)
print(myvar)
print(myvar.loc[0])

#loading a file into a dataframe
df = pd.read_csv(r"C:\Users\RISPER\Downloads\data.csv")
print(df)

print(pd.options.display.max_rows) 
