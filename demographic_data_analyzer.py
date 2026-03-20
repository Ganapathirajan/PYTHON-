import pandas as pd

data = [
    [39,"State-gov",77516,"Bachelors",13,"Never-married","Adm-clerical","Not-in-family","White","Male",2174,0,40,"United-States","<=50K"],
    [50,"Self-emp-not-inc",83311,"Bachelors",13,"Married-civ-spouse","Exec-managerial","Husband","White","Male",0,0,13,"United-States","<=50K"],
    [38,"Private",215646,"HS-grad",9,"Divorced","Handlers-cleaners","Not-in-family","White","Male",0,0,40,"United-States","<=50K"],
    [53,"Private",234721,"11th",7,"Married-civ-spouse","Handlers-cleaners","Husband","Black","Male",0,0,40,"United-States","<=50K"],
    [28,"Private",338409,"Bachelors",13,"Married-civ-spouse","Prof-specialty","Wife","Black","Female",0,0,40,"Cuba","<=50K"]
]

columns = [
    "age","workclass","fnlwgt","education","education-num",
    "marital-status","occupation","relationship","race","sex",
    "capital-gain","capital-loss","hours-per-week",
    "native-country","salary"
]

df = pd.DataFrame(data, columns=columns)

race_count = df["race"].value_counts()
print(race_count)

average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
print(f"Average age of men: {average_age_men}")

num_bachelors = df[df['education'] == 'Bachelors'].shape[0]
total_individuals = df.shape[0]
percentage_bachelors = (num_bachelors / total_individuals) * 100
print(f"Percentage of individuals with a Bachelor's degree: {percentage_bachelors:.2f}%")

higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
num_higher_education = higher_education.shape[0]
higher_education_rich = higher_education[higher_education['salary'] == '>50K'].shape[0]
percentage_higher_education_rich = (higher_education_rich / num_higher_education) * 100
print(f"Percentage of people with advanced education who earn >50K: {percentage_higher_education_rich:.2f}%")

lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
num_lower_education = lower_education.shape[0]
lower_education_rich = lower_education[lower_education['salary'] == '>50K'].shape[0]
percentage_lower_education_rich = (lower_education_rich / num_lower_education) * 100
print(f"Percentage of people without advanced education who earn >50K: {percentage_lower_education_rich:.2f}%")

min_work_hours = df['hours-per-week'].min()
num_min_workers = df[df['hours-per-week'] == min_work_hours]
total_min_workers = num_min_workers.shape[0]
rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]

if total_min_workers > 0:
    percentage_rich_min_workers = (rich_min_workers / total_min_workers) * 100
else:
    percentage_rich_min_workers = 0.0

print(f"Minimum number of hours worked per week: {min_work_hours}")
print(f"Percentage of those individuals earning >50K: {percentage_rich_min_workers:.2f}%")

india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

if not india_high_earners.empty:
    most_popular_occupation_india = india_high_earners['occupation'].mode()[0]
    print(f"Most popular occupation among high earners in India: {most_popular_occupation_india}")
else:
    print("No high earners from India found in the dataset.")

print(f"Average age of men: {average_age_men:.2f}")
print(f"Percentage of individuals with a Bachelor's degree: {percentage_bachelors:.2f}%")
print(f"Percentage of people with advanced education who earn >50K: {percentage_higher_education_rich:.2f}%")
print(f"Percentage of people without advanced education who earn >50K: {percentage_lower_education_rich:.2f}%")
print(f"Minimum number of hours worked per week: {min_work_hours}")
print(f"Percentage of those individuals earning >50K: {percentage_rich_min_workers:.2f}%")
print(f"Highest earning country: {highest_earning_country}")
print(f"Percentage of rich in {highest_earning_country}: {highest_earning_country_percentage:.2f}%")

if 'most_popular_occupation_india' in locals():
    print(f"Most popular occupation among high earners in India: {most_popular_occupation_india}")
else:
    print("No high earners from India found in the dataset for occupation analysis.")
