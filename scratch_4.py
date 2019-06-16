import numpy as np
import pandas as p
import matplotlib.mlab as mlab
import matplotlib.pyplot as pyplot
import csv

x="C:\\Users\\PRACHI CHAUDHARY\\Documents\\food_data1.csv"
data=p.read_csv(x,keep_default_na=True,na_values="#N/A",usecols=["FastFoodRestaurant","Type","AteIt","Rating"],true_values=['Yes'],false_values=['No'])
#print(data)
df=p.DataFrame(data)
df.dropna(inplace=True)
rating={"Very Good":5,"Good":4,"OK":3,"Bad":2, "Very Bad":1}
df.Rating=[rating[item] for item in df.Rating]
#print(df)
y=(df.FastFoodRestaurant)
z=(df.Rating)
pyplot.bar(y,z)
pyplot.title("Rating wrt Restaurant")
pyplot.xlabel("Restaurant")
pyplot.ylabel("Rating")
pyplot.show()
#z=(df.Type)
#pyplot.bar(y,z)
#pyplot.show()

#df.drop(df[["Rating"]=='n/a'],inplace=True)

#pro=df[df['Rating']=="n/a"]
#go=p.DataFrame(pro)
#print(go)



