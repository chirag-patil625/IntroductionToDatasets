import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/BHAGWAN PATIL/Desktop/Ai-Ds/Datasets/Iris.csv") #path of the data set. I will provide the dataset
print(df) #to Print dataset
print(df.shape) #Rows * Column
print(df.loc[df["Species"]=="Iris-setosa"]) #Print specific values
print(df["Species"].value_counts()) #Count of specific values
sum_data =df["SepalLengthCm"].sum() #to get sum of----
print("sum =",sum_data)
mean_data=df["SepalLengthCm"].mean() #to get mean of----
print("mean =",mean_data)
median_data=df["SepalLengthCm"].median() #to get median of----
print("median =",median_data)