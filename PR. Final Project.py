# =========================
# IMPORT LIBRARIES
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Packages import Matplotlib_2 as md

while True:
    print("\n================ FINAL PROJECT MAIN MENU ================")
    print("==========================")
    print("1. Load and Preprocess Data")
    print("2. NumPy Operations")
    print("3. Pandas Operations")
    print("4. Data Visualization Tool")
    print("5. Save Visualizations")
    print("6. Exit")
    print("==========================")

    ch = input("Enter Your Choice (1-6) :- ")

    if ch == "1":   

        path = input("Enter CSV file path: ")
        df = pd.read_csv(path)

        df.columns = df.columns.str.strip()
        print("\nDATASET INFO")
        print(df.info())
        print("\nDATASET DESCRIPTION")
        print(df.describe())


        numeric_df = df.select_dtypes(include=np.number)    

        if numeric_df.empty:
            print("No numeric columns found. Exiting program.")
            exit()

        col = numeric_df.columns[0]
        df.rename(columns={col: 'Value'}, inplace=True)

        values = df['Value'].to_numpy() 

        if df['Value'].isnull().sum() > 0:
            print("\nMissing values detected")
            choice = input("1. Drop  2. Fill : ")

            if choice == '1':
                df.dropna(inplace=True)
            else:
                df['Value'].fillna(df['Value'].mean(), inplace=True)
    print("\nDATA PREPROCESSING COMPLETED SUCCESSFULLY  ")

    if ch == "2":
        print("\n=========================")
        print("\nNUMPY OPERATIONS")
        print("=========================")

        print("=========================")
        print("Sum:", np.sum(values))
        print("Mean:", np.mean(values))
        print("Median:", np.median(values))
        print("Std Deviation:", np.std(values))
        print("Variance:", np.var(values))
        print("Min:", np.min(values))
        print("Max:", np.max(values))
        print("25th Percentile:", np.percentile(values, 25))
        print("75th Percentile:", np.percentile(values, 75))
        print("=========================")


    if ch == "3":
        print("\n=========================")
        print("PANDAS OPERATIONS")
        print("=========================")

        print("\nTop 5 Values")
        print(df.sort_values(by='Value', ascending=False).head())
        above_avg = df[df['Value'] > df['Value'].mean()]
        print("\nValues Above Average")
        print(above_avg.head())
        print("\n=========================")

    if ch == "4":
        print("\n=========================")
        print("\nDATA VISUALIZATION TOOL")
        print("=========================")

        print("1. Bar plot")
        print("2. Line plot")
        print("3. Scatter plot")
        print("4. Histogram")
        print("5. Pie chart")
        print("6. Box plot")
        
        choice = input("Choose a visualization type (1-6): ")
        data = df.sample(min(len(df), 3000))
        if choice == '1':
            column = input("Enter the column name for Bar Plot: ")
            data[column].value_counts().plot(kind='bar')
            plt.title(f"Bar Plot of {column}")
            plt.xlabel(column)
            plt.ylabel("Count")
            md.fast_show()
        elif choice == '2':
            column = input("Enter the column name for Line Plot: ")
            plt.plot(data[column], marker='o')
            plt.title(f"Line Plot of {column}")
            plt.xlabel("Index")
            plt.ylabel(column)
            md.fast_show()
        elif choice == '3':
            x_col = input("Enter the X-axis column name for Scatter Plot: ")
            y_col = input("Enter the Y-axis column name for Scatter Plot: ")
            plt.scatter(data[x_col], data[y_col], alpha=0.7)
            plt.title(f"Scatter Plot of {y_col} vs {x_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            md.fast_show()
        elif choice == '4':
            column = input("Enter the column name for Histogram: ")
            plt.hist(data[column], bins=10, alpha=0.7, color='blue')
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            md.fast_show()
        elif choice == '5':
            column = input("Enter the column name for Pie Chart: ")
            data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title(f"Pie Chart of {column}")
            md.fast_show()
        elif choice == '6':
            column = input("Enter the column name for Box Plot: ")
            plt.boxplot(data[column].dropna())
            plt.title(f"Box Plot of {column}")
            plt.ylabel(column)
            md.fast_show()
            print("Exiting the program. Goodbye!")
        
    elif ch == "5":
        output_dir = input("Enter the output directory for saving visualizations (default 'visualizations'): ") or 'visualizations'
        md.save_visualizations((df,), output_dir=output_dir)
        print(f"Visualizations saved in directory: {output_dir}")
        
    elif ch == "6":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
        