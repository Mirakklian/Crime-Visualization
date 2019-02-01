# Data analysing and visualizing the crime data of USA using Python
# Objective question : which state in the USA is the safe or has less crime rate
import numpy as np
import pandas as pd
import csv
from numpy.linalg import inv,det
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns
# Reading the Data from a csv file
crime = pd.read_csv('C:\\Users\\Pratik Dutta\\Downloads\\crime.csv')
Data = pd.DataFrame(crime)
print(Data)

# Summary of the crime data
describe = crime.describe()
print(describe)

crm=pd.get_dummies(crime['CRIME HEAD'],drop_first=True)
print(crm.head(5))

##Concatinate the data field into our data set

crime=pd.concat([crime,crm],axis=1)


##now we drop the unnecessary column
crime.drop(['CRIME HEAD'],axis=1,inplace=True)
print(crime)

# correlation between Rape and Assault
fig=plt.figure(figsize=(10,5))
plt.plot(crime['SELLING OF GIRLS FOR PROSTITUTION'],crime['BUYING OF GIRLS FOR PROSTITUTION'],color='M',label='PROSTITUTION', marker ='o')
plt.title("Correlation between selling  and buying")
plt.ylabel("SELLING OF GIRLS FOR PROSTITUTION")
plt.xlabel("BUYING OF GIRLS FOR PROSTITUTION")
plt.xticks(rotation=90)
plt.legend(loc='best')
plt.show()

# Bar plot for 2003
fig=plt.figure(figsize=(10,5))
plt.bar(Data['STATE'],Data['2003'], color='G',label='2003')
plt.title(' Rate of crime in each state')
plt.ylabel('2003')
plt.xlabel('STATE')
plt.xticks(rotation=90)
plt.legend(loc='best')
plt.show()
#
### Line plot for Burglary
fig=plt.figure(figsize=(10,5))
#plt.plot(Data['STATE'],Data['BURGLARY'], label='State')
plt.plot(Data['STATE'],Data['2011'], color='M',label='2011 INDIA', marker ='o')
plt.title(' Rate of crime in each state')
plt.ylabel('2011 crime')
plt.xlabel('STATE')
plt.xticks(rotation=90)
plt.legend(loc='best')
plt.show()
