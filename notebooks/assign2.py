import pandas as pd
from datetime import date
from datetime import datetime
import statistics


data = pd.read_csv("notebooks/files/healthcare-dataset-stroke-data.csv", sep=',')


def percentage(part, whole):
  return 100 * float(part)/float(whole)


## Q1: In the given dataset, what is the percentage (of all the persons in the dataset) of 70 years old or older who suffered a stroke?

q1 = data.query('age > 70 and stroke == 1')
q1 = percentage(len(q1), len(data))
q1 = round(q1, 2)

print(f'Q1: The percentage of persons who are over 70 years old and suffered a stroke is {q1}%.')

## Q2: In the given dataset, what is the percentage (of all the persons in the dataset) of 70 years old or older who suffered a stroke and are smokers / former smokers?

q2 = data.query('age >= 70 and stroke == 1 and (smoking_status == "formerly smoked" or smoking_status == "smokes")')
q2 = percentage(len(q2), len(data))
q2 = round(q2, 2)

print(f'Q2: The percentage of persons who are over 70 years old and suffered a stroke and formerly smoked or still smoke is {q2}%.')

## Q3: What percentage of those who suffered a stroke have “avg_glucose_level” at least 20% above the mean value of the entire dataset?

avg_glucose_level__mean = data['avg_glucose_level'].mean()
twenty_percent_above_mean = avg_glucose_level__mean * 1.2

stroke_data = data[data['stroke'] == 1]

q3 = stroke_data[stroke_data['avg_glucose_level'] >= twenty_percent_above_mean]
q3 = percentage(len(q3), len(stroke_data))
q3 = round(q3, 2)

print(f'Q3: The percentage of persons who suffered a stroke and have "avg_glucose_level" at least 20% above the mean is {q3}%.')

## Q4: Are all age groups equally represented in this dataset?



age__mean = data['age'].mean()
age__std = data['age'].std()

print()
print(age__mean)
print(age__std)
print()

data.hist(column='age')
data.plot(kind='hist')
data.plot.hist()


print(f'Q4: [Yes|No] all age groups [are|are not] equally represented in this datasent, because [explanation].')
