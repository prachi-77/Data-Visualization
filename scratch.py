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
bp=df[df["Rating"]==5]
print(bp)
best_rest=bp.FastFoodRestaurant
best_item=bp.Type
#print(best_item)
pyplot.scatter(best_rest,best_item)
pyplot.title("Best Restaurant and its best item on the basis of Rating")
pyplot.xlabel("Restaurant")
pyplot.ylabel("Item")


pyplot.show()
