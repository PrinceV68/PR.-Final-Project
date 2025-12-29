import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from faker import Faker
import random


data_2 = None
def load_data(file_path):
    try:
        match file_path:
            case path if path.endswith(".csv"):
                data_2 = pd.read_csv(path)
                print("CSV file loaded successfully.")
                return data_2, "csv"

            case path if path.endswith(".xlsx") or path.endswith(".xls"):
                data_2 = pd.read_excel(path)
                print("Excel file loaded successfully.")
                return data_2, "xlsx"

            case _:
                print("Unsupported file format.")
                return None, None

    except Exception as e:
        print("Error loading file:", e)
        return None, None

def display_statistics(data):
    data = data[0]
    print("\nDataset Statistics:")
    
    print("1. Display first 5 rows :- ")
    print("2. Display last 5 rows :- ")
    print("3. Display Column Names :- ")
    print("4. Display Data Types :- ")
    print("5. Display Basic info :- ")
    
    ch = input("Enter your choice (1-5): ")
    
    match ch:
        case '1':
            print(data.head())
        case '2':
            print(data.tail())
        case '3':
            print(data.columns)
        case '4':
            print(data.dtypes)
        case '5':
            print(data.info())
        case _:
            print("Invalid choice.")
        
def visualize_data(data):   
    data = data[0]
    
    print("\nGenerating visualizations...")
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) >= 2:
        sns.pairplot(data[numeric_cols])
        plt.suptitle("Pairplot of Numeric Features", y=1.02)
        plt.show(block=False)
        plt.pause(2)
        plt.close()
    
    else:
        print("Not enough numeric columns for pairplot.")
    
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(data[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show(block=False)
        plt.pause(2)
        plt.close()
    
    
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=data[col], order=data[col].value_counts().index)
        plt.title(f"Count Plot of {col}")
        plt.show(block=False)
        plt.pause(2)
        plt.close()
           
    print(dir(data))

def Random_dataset():
    fake = Faker()
    N = 50000

    data = {
        "Employee_ID": [],
        "Name": [],
        "Gender": [],
        "Age": [],
        "Department": [],
        "Job_Title": [],
        "Experience_Years": [],
        "Salary": [],
        "Email": [],
        "City": [],
        "Joining_Date": [],
        "Performance_Rating": []
    }

    departments = {
        "IT": ["Software Engineer", "Data Analyst", "System Admin"],
        "HR": ["HR Executive", "HR Manager"],
        "Finance": ["Accountant", "Financial Analyst"],
        "Sales": ["Sales Executive", "Sales Manager"],
        "Marketing": ["Marketing Executive", "SEO Analyst"]
    }

    for i in range(1, N + 1):
        dept = random.choice(list(departments.keys()))
        job = random.choice(departments[dept])

        data["Employee_ID"].append(i)
        data["Name"].append(fake.name())
        data["Gender"].append(random.choice(["Male", "Female"]))
        data["Age"].append(random.randint(21, 60))
        data["Department"].append(dept)
        data["Job_Title"].append(job)
        data["Experience_Years"].append(random.randint(0, 35))
        data["Salary"].append(random.randrange(20000, 150001, 5000))
        data["Email"].append(fake.company_email())
        data["City"].append(fake.city())
        data["Joining_Date"].append(fake.date_between(start_date="-10y", end_date="today"))
        data["Performance_Rating"].append(round(random.uniform(1, 5), 1))

    df = pd.DataFrame(data)

    df.to_csv("mydata.csv", index=False)

    print(" Employee HR dataset generated (50,000 rows)")
    return df

def Dataframe(data):

    data = data[0]
    print("\nDataFrame Operations:")
    print("1. Filter Rows")
    print("2. Sort Data")
    print("3. Group By")
    choice = input("Choose an operation (1-3): ")
    
    
    if choice == '1':
        column = input("Enter the column name to filter by: ")
        value = input("Enter the value to filter for: ")

        filtered_data = data[data[column].astype(str) == value]
        print(filtered_data)

        print(filtered_data)

    elif choice == '2':
        column = input("Enter the column name to sort by: ")
        sorted_data = data.sort_values(by=column)
        print(sorted_data)

    elif choice == '3':
        column = input("Enter the column name to group by: ")
        grouped_data = data.groupby(column).size()
        print(grouped_data)
    else:
        print("Invalid choice.")
        
def handle_missing_values(data):
    data = data[0]
    # data.isnull().sum()
    
    print(data.isnull().sum())

    print("\nHandling Missing Values:")
    print("1. Drop Missing Values")
    print("2. Fill Missing Values")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        data = data.dropna()
        print("Missing values dropped.")
        
    elif choice == '2':
        data.fillna(data.mean(numeric_only=True), inplace=True)
        for col in data.select_dtypes(include='object'):
            data[col].fillna(data[col].mode()[0], inplace=True)
        print("Missing values filled.")
    else:
        print("Invalid choice.")
        return data



def descriptive_statistics(data):    
    data = data[0]
    print("\nDescriptive Statistics:")
    print(data.describe(include='all'))
    
    print("\nCorrelation Matrix:")
    print(data.corr(numeric_only=True))  
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Heatmap")
    fast_show()
    
def fast_show():
    i = input("Press Enter to display the plot :- ")
    plt.show(block=False)
    plt.pause(int(i))
    plt.close()
    
def Data_visualization(data):
    data = data[0]
    print("\nData Visualization:")
    print("1. Bar Plot")
    print("2. line Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Histogram")
    print("6. Stack Plot")    

    choice = input("Choose a visualization type (1-6): ")

    data = data.sample(min(len(data), 3000))
    match choice:
        case '1':
            column = input("Enter the column name for Bar Plot: ")
            data[column].value_counts().plot(kind='bar')
            plt.title(f"Bar Plot of {column}")
            fast_show()

        case '2':
            column = input("Enter the column name for Line Plot: ")
            data[column].plot(kind='line')
            plt.title(f"Line Plot of {column}")
            fast_show()

        case '3':
            x_col = input("Enter the X-axis column name for Scatter Plot: ")
            y_col = input("Enter the Y-axis column name for Scatter Plot: ")
            data.plot(kind='scatter', x=x_col, y=y_col)
            plt.title(f"Scatter Plot of {y_col} vs {x_col}")
            fast_show()

        case '4':
            column = input("Enter the column name for Pie Chart: ")
            data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title(f"Pie Chart of {column}")
            fast_show()
        case '5':
            column = input("Enter the column name for Histogram: ")
            data[column].plot(kind='hist', bins=10)
            plt.title(f"Histogram of {column}")
            fast_show()
        case '6':
            columns = input("Enter the column names for Stack Plot: ").split(',')
            data[columns].plot(kind='area', stacked=True)
            plt.title(f"Stack Plot of {', '.join(columns)}")
            fast_show()
    
def save_visualizations(data, output_dir='visualizations'):
    data = data[0]
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(data[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(os.path.join(output_dir, f"{col}_distribution.png"))
        plt.close()

    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=data[col], order=data[col].value_counts().index)
        plt.title(f"Count Plot of {col}")
        plt.savefig(os.path.join(output_dir, f"{col}_countplot.png"))
        plt.close()

    print(f"Visualizations saved in directory: {output_dir}")   
    
