import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'R:\Prodigy infotech intern project\Task-I\melb_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# To get categorical data
s = (df.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)

# Create a bar chart for the 'Method' variable
method_counts = df['Method'].value_counts()
method_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Method')
plt.ylabel('Count')
plt.title('Distribution of Methods in Melbourne Housing Data')
plt.show()


# create histogrma for the 'Method' variables
plt.hist(df['Method'], color='skyblue')
plt.xlabel('Method')
plt.ylabel('Count')
plt.title('Distribution of Methods in Melbourne Housing Data')
plt.show()

