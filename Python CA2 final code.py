import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python ca 2\\Global_Landslide_Catalog_Export.csv")
print(df.shape)
print(df.head())
print(df.columns)
print("Null:- ", df.isnull().sum())

# Select numeric columns to analyze
numeric_cols = ['fatality_count', 'injury_count', 'admin_division_population', 'gazeteer_distance']

# Fill missing values
df[numeric_cols] = df[numeric_cols].fillna(0)

# Handle dates
df['event_date'] = pd.to_datetime(df['event_date'], errors='coerce')
df['quarter'] = df['event_date'].dt.to_period('Q')  # ✅ This fixes the 'quarter' column issue

# Detect outliers using IQR
outlier_info = {}
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_info[col] = {
        'num_outliers': len(outliers),
        'lower_bound': lower_bound,
        'upper_bound': upper_bound
    }

# Print outlier info
for col, stats in outlier_info.items():
    print(f"{col}:\n  Outliers: {stats['num_outliers']}\n  Lower Bound: {stats['lower_bound']:.2f}\n  Upper Bound: {stats['upper_bound']:.2f}\n")

# 1. Top 10 Countries
plt.figure(figsize=(10, 6))
top_countries = df['country_name'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Blues_r')
plt.title("Top 10 Countries by Landslide Frequency")
plt.xlabel("Number of Landslides")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# 2. Scatter Plot: Fatalities vs Injuries
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='injury_count', y='fatality_count', alpha=0.6)
plt.title("Fatalities vs Injuries")
plt.xlabel("Injuries")
plt.ylabel("Fatalities")
plt.tight_layout()
plt.show()

# 3. Rain-triggered vs Other Triggers Pie Chart
plt.figure(figsize=(8, 8))
rain_pie = df['landslide_trigger'].apply(lambda x: 'Rainfall' if 'rain' in str(x).lower() else 'Other')
rain_counts = rain_pie.value_counts()
plt.pie(rain_counts, labels=rain_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightgray'])
plt.title("Rainfall vs Other Triggers")
plt.tight_layout()
plt.show()

# 4. Quarterly Landslide Trends
plt.figure(figsize=(12, 6))
quarterly_counts = df['quarter'].value_counts().sort_index()
quarterly_counts.plot(kind='line', marker='o', color='green')
plt.title("Quarterly Landslide Trends")
plt.xlabel("Quarter")
plt.ylabel("Number of Landslides")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.show()

# 6. Pair Plot (Opens separately)
sns.pairplot(df[numeric_cols])
plt.suptitle("Pairplot of Numerical Columns", y=1.02)
plt.show()
