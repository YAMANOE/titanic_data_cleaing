import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\users\user\Downloads\archive (29)\Titanic-Dataset.csv")

print(data.info())

print("*"*15)

print(data.head())
print(data.describe())
print(data['Cabin'].value_counts())
print(data.isnull().sum())
data['Age'].fillna(data['Age'].mean(),inplace=True)
print(data.isnull().sum())
data.dropna(subset=['Cabin','Name','PassengerId'],inplace=True)
print(data.isnull().sum())
print(data['Embarked'].value_counts())
data['Embarked'].fillna('S',inplace=True)
print(data.isnull().sum())
data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)
print(data['Embarked'].value_counts())
data['Sex'].fillna('male',inplace=True)
print(data.isnull().sum())
data['Sex'].replace(['male','female'],[0,1],inplace=True)
print(data.isnull().sum())