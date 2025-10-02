import pandas as pd
import matplotlib.pyplot as mp
program=pd.read_csv("gender_submission.csv")
print(program)
program.rename(columns={"PassengerId":"Id","Survived":"Status for clarity"},inplace=True),
print("Renamed column name:",program)
print("The Titanic data from the Top:",program.head())
print("The Titanic data from the Bottom:",program.tail())
print("Titanic dataset information:",program.info())
print("Count:",program.shape)
Non_survived=program[program["Status for clarity"]==0].head(10)
print("Top 10 Non-Survived:",Non_survived)
survived=program[program["Status for clarity"]==1].head(10)
print("Top 10 Survived:",survived)
Total_count=program["Status for clarity"].value_counts()
survived_count=Total_count[1]
Nonsurvived_count=Total_count[0]
print("Total Survived:",survived_count)
print("Total Not Survived:",Nonsurvived_count)
Total_passengers=len(program)
percentage_of_survived_passengers=(survived_count/Total_passengers)*100
percentage_of_Nonsurvived_passengers=(Nonsurvived_count/Total_passengers)*100
print("Percentage Survived:",percentage_of_survived_passengers)
print("Percentage Not Survived:",percentage_of_Nonsurvived_passengers)
Total_count.plot(kind='bar',color=["purple","skyblue"])
mp.xlabel("Status 0=Not survived,1=survived")
mp.ylabel("No of persons")
mp.title("Survived vs Not Survived")
mp.xticks(rotation=0)
mp.show()