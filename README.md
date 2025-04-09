🌍 Global Landslide Data Analysis using Python
📊 Project Overview
This project focuses on analyzing the Global Landslide Catalog dataset using Python. The goal is to uncover insights about landslide trends, triggers, and impacts across countries and time periods. The project demonstrates skills in data preprocessing, outlier detection, visualization, and insight extraction using tools like Pandas, Seaborn, and Matplotlib.

🔧 Tools & Technologies Used
Python 3.x

Pandas for data manipulation

Matplotlib & Seaborn for data visualization

NumPy for numerical operations

DateTime for time-based analysis

📂 Dataset
Source: Global Landslide Catalog (NASA)

Format: CSV

Attributes: Includes event date, location, trigger type, fatality & injury count, population, etc.

📈 Key Objectives & Visualizations
1. 🗺️ Top 10 Countries by Landslide Frequency
Bar chart showing countries with the highest number of landslide events.

2. 🧍‍♂️ Fatalities vs Injuries (Scatter Plot)
Analyzes the relationship between injuries and fatalities from landslides.

3. 🌧️ Rainfall vs Other Triggers (Pie Chart)
Categorizes events based on their primary trigger (rainfall or other).

4. 📅 Quarterly Landslide Trends (Line Plot)
Time-series visualization of landslide occurrences by quarter.

5. 🔥 Correlation Heatmap
Highlights correlations between population, injuries, fatalities, and distance.

6. 📊 Pair Plot of Numerical Features
Matrix of scatter plots for multivariate analysis of numerical attributes.

🧹 Data Cleaning Highlights
Converted event_date to datetime format and extracted the quarter.

Handled missing values in key columns like fatality_count, injury_count, etc.

Applied IQR method to detect outliers and summarize results.

📌 How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/landslide-data-analysis.git
Install required libraries:

bash
Copy code
pip install pandas matplotlib seaborn
Run the Python file:

bash
Copy code
python landslide_analysis.py
Ensure the CSV file is placed in the correct directory path or update it in the script.

📚 Learnings
Strengthened skills in EDA (Exploratory Data Analysis)

Improved understanding of correlation, trend detection, and outlier handling

Learned how to create meaningful visualizations for decision-making

📬 Connect with Me
Feel free to connect on LinkedIn or reach out for collaboration, suggestions, or feedback!

⭐ Future Improvements
Create interactive dashboards using Plotly or Dash

Integrate geospatial analysis for mapping landslide locations

Predict landslide risk using machine learning

📌 License
This project is for academic and learning purposes. Dataset credit to NASA Global Landslide Catalog.

