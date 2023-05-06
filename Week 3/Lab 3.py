# -*- coding: utf-8 -*-
"""Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pj0PWfq4je5mopHKx-T6KP9sgjtlkN4R
"""

### I. Matplotlib
##1. Importing
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
##2. Basic example
# %matplotlib inline

##2. Basic example
import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2

x

y

##3. Basic Matplotlib Commands
plt.plot(x, y, 'r') 
plt.xlabel('x Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show( )

##4. Creating Multiplots on Same Canvas
plt.subplot(1,2,1)
plt.plot(x, y,'r--')
plt.subplot(1,2,2) 
plt.plot(y, x, 'g*-');

##5. Object Oriented Method
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,'b')

axes.set_xlabel('Set X Label')

axes.set_ylabel('Set y Label')

axes.set_title('Set Title')

fig = plt.figure()
axesl = fig.add_axes([0.1, 0.1,0.8,0.8])
axes2 = fig.add_axes([0.2, 0.5,0.4,0.3])

# Larger Figure Axes 1
axesl.plot(x, y, 'b')

axesl.set_xlabel('X label axes2')
axesl.set_ylabel('Y label axes2')
axesl.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X label axes2')
axes2.set_ylabel('Y label axes2')
axes2.set_title('Axes 2 Title');

##6. Suplot()
fig, axes = plt.subplots()

# Now use the axes object to add stuff to plot
axes.plot(x, y, 'r')

axes.set_xlabel('x')

axes.set_ylabel('y')

axes.set_title('title');

fig, axes = plt.subplots(nrows=1, ncols=2)

axes

for ax in axes:
  ax.plot(x, y, 'b')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title('title')
fig

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
  ax.plot(x, y ,'g')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title(' title')

##7. Figure size, aspect ratio and DPI
flg = plt.figure(figsize=(8,4), dpi=100)

fig, axes = plt.subplots(figsize=(12,3))
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel( 'y')
axes.set_title('title');

##8. Saving figures
fig.savefig("IMG_0019.JPG")

fig.savefig("IMG_0019.JPG", dpi=200)

##9. Figure titles
ax.set_title("title");

##10. Axis labels
ax.set_xlabel("x")

ax.set_ylabel("y");

##11. Legends
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x**2, label="x**2")

ax.plot(x, x**3, label="x**3")
ax.legend()

##12. Plot range
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])

axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");

###II. Seaborn

# Commented out IPython magic to ensure Python compatibility.
##1. Load testing dataset
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
# %matplotlib inline

sns.get_dataset_names()

tips = sns.load_dataset("tips")
tips.head()

##2. Scatter plot
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)

sns.relplot(x="total_bill", y="tip", data=tips, kind="scatter",
hue="sex", size="size",
)

##3. Categorical functions
sns.catplot(x="sex", y="total_bill", hue="day", data=tips, kind="strip")

sns.catplot(x="sex", y="total_bill", hue="day", data=tips, kind="strip",
jitter=False, dodge=True)

sns.catplot(x="sex", y="total_bill", hue="day", data=tips, kind="box")

###III. Exercises

##Continuing with the job market data, use Matplotlib/Seaborn to visualize:
##✓ Job by location. (Below image is just a sample)

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas DataFrame
df = pd.read_csv('job-market.csv')

jobs_by_location = df.groupby('Classification')['Location'].count().reset_index().sort_values('Location')

# Create a horizontal bar chart with rainbow color
plt.barh(jobs_by_location['Classification'], jobs_by_location['Location'], color=plt.cm.rainbow(jobs_by_location['Location']/max(jobs_by_location['Location'])))
plt.show()

# ✓ Job posts by salary range. (Below image is just a sample)
import seaborn as sns
df['salary_range'] = pd.cut(df['HighestSalary'], bins=[0,30,40,50,60])

df['mean_salary'] = (df['LowestSalary'] + df['HighestSalary']) / 2

counts = df.groupby('salary_range').size().reset_index(name='count')

counts

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.title('Job Posts by Salary Range')
sns.set_palette('pastel')
plt.pie(counts['count'], labels=counts['salary_range'], autopct='%1.1f%%')
plt.show()

##✓ Explore other aspects of the dataset
jobs_by_company = df.groupby('Area')['Title'].count()

sns.set(style="whitegrid")
plt.figure(figsize=(10, 10))
sns.barplot(y=jobs_by_company.values, x=jobs_by_company.index)
plt.title('Job by Company')
plt.xlabel('Number of job')
plt.xticks(rotation=90)
plt.ylabel('Jobs')
plt.show()

##2. Data Correlation (Advanced and Optional)
##❖ Load data from wine.data.csv file. Keep 1st column into a separate variable (label) and remove it from DataFrame.
##❖ Use Scatter plot to learn attributes of data. What is your conclusion?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load data
df2 = pd.read_csv('wine.data.csv')
df2.head(10)

label = df2.iloc[:, 0]
data = df2.iloc[:, 1:]

sns.set(style='ticks')
sns.pairplot(data)
plt.show()

corr_matrix = data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)
plt.title('Correlation Heatmap')
plt.show()

scaler = StandardScaler()
wine_scaled = scaler.fit_transform(df2)

kmeans = KMeans(n_clusters=3, random_state=0)
wine_clusters = kmeans.fit_predict(wine_scaled)

df2['cluster'] = wine_clusters
sns.pairplot(df2, hue='cluster',diag_kind="hist")