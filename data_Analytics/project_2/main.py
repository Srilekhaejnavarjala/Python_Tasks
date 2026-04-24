'''
=================================================================================================================================
 ---------------------------------------------📊 Project Title: IGN Data Analysis------------------------------------------------
 ----------------------------------Analyze IGN dataset using NumPy, Pandas, Matplotlib-------------------------------------------
=================================================================================================================================
'''
'''
=================================================================================================================================
 📦 1. Import Required Libraries
=================================================================================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation
<Import your libraries>
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
=================================================================================================================================
 🟢 SCENARIO 1: Data Loading & Preprocessing
=================================================================================================================================
�� Tasks:
1. Load the dataset using Pandas.
2. Display:
   ○ First 5 rows (head())
   ○ Last 5 rows (tail())
   ○ Shape of dataset
3. Remove the unnecessary column:
   ○ "Unnamed: 0" (index column)
4. Check for missing values in:
   ○ score, genre, platform
5. Handle missing values:
   ○ Fill numeric column score with mean
   ○ Fill categorical column genre with mode
6. Ensure correct data types:
   ○ score → float
   ○ release_year, release_month, release_day → integer
'''
#Loading dataset using pandas
data = pd.read_csv("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/ign.csv")

#First five rows of the dataset
print("Displaying the first 5 rows of data:")
print(data.head())
print("------------------------------------------------------------------------------")

#Last five rows of the dataset
print("Displaying the last 5 rows of data:")
print(data.tail())
print("------------------------------------------------------------------------------")

#Shape of the dataset
print("The shape of the dataset is : ")
print(data.shape)
print("------------------------------------------------------------------------------")

# removing unnecessary column (avoid error if not present)
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
print("Removed the column Unnamed!!")
print("------------------------------------------------------------------------------")

# checking missing values before handling
missing_values = data[['score_phrase', 'genre', 'platform']].isnull().sum()
print("Total missing values before handling:\n", missing_values)
print("------------------------------------------------------------------------------")

# convert score to numeric (invalid values -> NaN)
data['score_phrase'] = pd.to_numeric(data['score_phrase'], errors='coerce')

# fill numeric column with mean
average_score = data['score_phrase'].mean()
data['score_phrase'] = data['score_phrase'].fillna(average_score)

# fill categorical columns with mode (handle empty mode safely)
if not data['genre'].mode().empty:
    mode_val_genre = data['genre'].mode()[0]
    data['genre'] = data['genre'].fillna(mode_val_genre)

if not data['platform'].mode().empty:
    mode_val_platform = data['platform'].mode()[0]
    data['platform'] = data['platform'].fillna(mode_val_platform)

print("Replaced missing values correctly!!")
print("------------------------------------------------------------------------------")

# checking missing values after handling 
missing_values_after = data[['score_phrase', 'genre', 'platform']].isnull().sum()
print("Total missing values AFTER handling:\n", missing_values_after)
print("------------------------------------------------------------------------------")

#Changing data types

data = data.astype({
    'score_phrase': 'float64',
    'release_year': 'int32',
    'release_month': 'int32',
    'release_day': 'int32'
})

print("Changed the type of columns into its respective types")
print("------------------------------------------------------------------------------")

'''
=================================================================================================================================
 🟢 SCENARIO 2: Line Graph (Score Trend) + Save
=================================================================================================================================
�� Tasks:
1. Group data by release_year.
2. Calculate average score per year using Pandas.
3. Convert results into NumPy arrays.
4. Plot a line graph:
    ○ X-axis → release_year
    ○ Y-axis → average score
5. Add:
    ○ Title: "Average Game Score Over Years"
    ○ Axis labels
6. Save the graph: plt.savefig("avg_score_trend.png")
'''
grouped_year = data.groupby('release_year')['score'].mean()
print("------------------------------------------------------------------------------")
#Calculating average score per year using pandas
print("The average score for respective years is: ")
print(grouped_year)
print("------------------------------------------------------------------------------")

#converting into numpy arrays
years = grouped_year.index.to_numpy()
avg_scores = grouped_year.values
print("------------------------------------------------------------------------------")

#Plotting line graph
plt.figure()
plt.plot(years,avg_scores, marker = 'o')
plt.title("Average Game Score Over Years")
plt.xlabel("release_year")
plt.ylabel("average_score")
plt.tight_layout()
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/avg_score_trend.png")
#plt.show()
print("------------------------------------------------------------------------------")

'''
=================================================================================================================================
 🟡 SCENARIO 3: Filtering + Bar Chart + Save
=================================================================================================================================
 �� Tasks:
1. Filter dataset where:
    ○ score > 7
2. Count number of high-rated games per platform.
3. Select top 10 platforms using Pandas.
4. Convert data into NumPy arrays.
5. Plot a bar chart:
    ○ X-axis → platform
    ○ Y-axis → count of games
6. Rotate x-axis labels for readability.
Save the graph: plt.savefig("top_platforms_bar.png")

'''
# Filtering dataset where score > 7
filtered_data = data[data['score'] > 7]
print("------------------------------------------------------------------------------")

# Count number of high-rated games per platform
top_rated_games = filtered_data.groupby('platform')['title'].count()
print(top_rated_games)
print("------------------------------------------------------------------------------")

# Select top 10 platforms based on count
top_10 = top_rated_games.sort_values(ascending=False).head(10)
print(top_10)
print("------------------------------------------------------------------------------")

# Convert to NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values
print(platforms)
print(counts)

# Plotting bar chart
plt.figure()
plt.bar(platforms, counts)
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()
# Save before show
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/top_platforms_bar.png")
#plt.show()
'''
=================================================================================================================================
 🟡 SCENARIO 4: Aggregation + Pie Chart + Save
=================================================================================================================================
�� Tasks:
1. Count the number of games per genre.
2. Select top 5 genres using Pandas.
3. Prepare labels and values.
4. Plot a pie chart:
○ Labels → genre
○ Values → count
5. Add percentage labels (autopct).
Save the graph: plt.savefig("genre_distribution.png")
'''
# Counting number of games per genre
genre_counts = data['genre'].value_counts()
print("The number of games per genre are:")
print(genre_counts)
print("------------------------------------------------------------------------------")

# Select top 5 genres
top_5 = genre_counts.head(5)
print("Top 5 genres are:")
print(top_5)
print("------------------------------------------------------------------------------")

# Prepare labels and values
genres = top_5.index.to_numpy()
counts = top_5.values

# Plot pie chart
plt.figure()
plt.pie(counts, labels=genres, autopct='%1.1f%%')
plt.title("Genre Distribution")
plt.tight_layout()
# Save before show
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/genre_distribution.png")
#plt.show()
'''
=================================================================================================================================
 🔴 SCENARIO 5: Advanced Analysis + Multiple Graphs
=================================================================================================================================
�� Part 1: Feature Engineering
1. Create a new column:
    ○ score_category:
        ■ score >= 9 → "Excellent"
        ■ 7 <= score < 9 → "Good"
        ■ < 7 → "Average"
2. Convert editors_choice:
    ○ Y → 1, N → 0
�� Part 2: NumPy Analysis
3. Use NumPy to:
    ○ Calculate yearly score growth using np.diff() on average yearly scores
�� Part 3: Visualizations
�� Line Graph
4. Plot trend of:
    ○ Average score per release_year
�� Stacked Bar Chart
5. Show count of:
    ○ score_category per release_year
�� Histogram
6. Plot distribution of:
    ○ score
�� Part 4: Save All Graphs
plt.savefig("score_trend.png")
plt.savefig("score_category_stacked.png")
plt.savefig("score_distribution.png")
�� Part 5: Insights
Identify:
    ● Which years had highest scores
    ● Whether high scores increased over time
    ● If editors_choice correlates with high scores
'''

#Part 1: Feature Engineering

# Create score_category column using conditions
data['score_category'] = np.where(
    data['score'] >= 9, "Excellent",
    np.where(data['score'] >= 7, "Good", "Average")
)

print("Score category column created!")
print("------------------------------------------------------------------------------")

# Convert editors_choice column (Y → 1, N → 0)
data['editors_choice'] = data['editors_choice'].map({'Y': 1, 'N': 0})

print("Converted editors_choice to numeric!")
print("------------------------------------------------------------------------------")


#Part 2: NumPy Analysis

# Average score per year (reuse or recompute safely)
yearly_avg = data.groupby('release_year')['score'].mean()

years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

# Calculate yearly growth using np.diff()
score_growth = np.diff(avg_scores)

print("Yearly score growth:")
print(score_growth)
print("------------------------------------------------------------------------------")


#Part 3: Visualizations

#1. Line Graph (Score Trend)
plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.tight_layout()
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/score_trend.png")
#plt.show()


#2. Stacked Bar Chart (Score Category per Year)

# Create pivot table
category_counts = data.pivot_table(
    index='release_year',
    columns='score_category',
    aggfunc='size',
    fill_value=0
)

category_counts.plot(kind='bar', stacked=True)

plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/score_category_stacked.png")
#plt.show()


#3. Histogram (Score Distribution)
plt.figure()
plt.hist(data['score'], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
#plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_2/pictorial_analysis/score_distribution.png")
#plt.show()


#Part 5: Insights 

# Year with highest average score
max_year = yearly_avg.idxmax()
max_score = yearly_avg.max()

print(f"Year with highest average score: {max_year} ({max_score:.2f})")

# Check trend direction
if score_growth.mean() > 0:
    print("Overall trend: Scores are increasing over time ")
else:
    print("Overall trend: Scores are decreasing or fluctuating ")

# Editors choice vs score
editors_avg = data.groupby('editors_choice')['score'].mean()

print("\nAverage score based on editors_choice:")
print(editors_avg)

if editors_avg[1] > editors_avg[0]:
    print("Editors' Choice games generally have higher scores ")
else:
    print("Editors' Choice does not strongly correlate with higher scores ")

'''
================================================================================================================
-----------------------------------------------------THE END----------------------------------------------------
================================================================================================================
'''

