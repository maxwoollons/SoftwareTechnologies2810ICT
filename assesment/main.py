import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import numpy as np

# Data years we have available
options = [
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019"  
]

# Keywords for the third option
keywords = [
    "Struck Pedestrian",
    "Collision with a fixed object",
    "Collision with vehicle",
    "No collision and no object struck",
]

# Day-Month
vicholidays = ['1-1','2-1','26-1','13-3','7-4','8-4','9-4','10-4','25-4','12-6','29-9','7-11','25-12','26-12']


root = tk.Tk()
root.title("Data Visualization Project - Victoria Crash Data")
root.geometry("800x500")
root.iconbitmap("favicon.ico")

label = tk.Label(root, text="Data Visualization", font=("Arial", 20))
label.pack()

# First Option

graph1 = tk.Label(root, text="Graph 1: Infomation on Crash over a period of time", font=("Arial", 15))
graph1.pack()
framebtn1 = tk.Frame(root)
framebtn1.columnconfigure(0, weight=1)
framebtn1.columnconfigure(1, weight=1)
framebtn1.columnconfigure(2, weight=1)
framebtn1.pack()

button1 = tk.Button(framebtn1, text="Show Graph", command=lambda: show_graph1())
button1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry1 = tk.StringVar()
entry1.set("Start Year")
drop = tk.OptionMenu(framebtn1, entry1, *options)
drop.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry2 = tk.StringVar()
entry2.set("End Year")
drop2 = tk.OptionMenu(framebtn1, entry2, *options)
drop2.grid(row=0, column=2, sticky="ew", padx=5, pady=5)





# Second Option


graph2 = tk.Label(root, text="Graph 2: Number of accidents in each hour of the day", font=("Arial", 15))
graph2.pack()

framebtn2 = tk.Frame(root)
framebtn2.columnconfigure(0, weight=1)
framebtn2.columnconfigure(1, weight=1)
framebtn2.columnconfigure(2, weight=1)
framebtn2.pack()

button2 = tk.Button(framebtn2, text="Show Graph", command=lambda: show_graph2())
button2.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry3 = tk.StringVar()
entry3.set("Start Year")
drop1 = tk.OptionMenu(framebtn2, entry3, *options)
drop1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry4 = tk.StringVar()
entry4.set("End Year")
drop5 = tk.OptionMenu(framebtn2, entry4, *options)
drop5.grid(row=0, column=2, sticky="ew", padx=5, pady=5)


# Third Option
# (Drop down box)

graph3 = tk.Label(root, text="Graph 3: All accidents caused by an accident type that contains a keyword", font=("Arial", 15))
graph3.pack()
framebtn3 = tk.Frame(root)
framebtn3.columnconfigure(0, weight=1)
framebtn3.columnconfigure(1, weight=1)
framebtn3.columnconfigure(2, weight=1)
framebtn3.columnconfigure(3, weight=1)
framebtn3.pack()
button3 = tk.Button(framebtn3, text="Show Graph", command=lambda: show_graph3())
button3.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry5 = tk.StringVar()
entry5.set("Keyword")
drop6 = tk.OptionMenu(framebtn3, entry5, *keywords)
drop6.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry6 = tk.StringVar()
entry6.set("Start Year")
drop7 = tk.OptionMenu(framebtn3, entry6, *options)
drop7.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
entry7 = tk.StringVar()
entry7.set("End Year")
drop7 = tk.OptionMenu(framebtn3, entry7, *options)
drop7.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

# Fourth Option
graph4 = tk.Label(root, text="Graph 4: Alcohol Impact in accidents", font=("Arial", 15))
graph4.pack()
framebtn4 = tk.Frame(root)
framebtn4.columnconfigure(0, weight=1)
framebtn4.columnconfigure(1, weight=1)
framebtn4.columnconfigure(2, weight=1)
framebtn4.pack()
button4 = tk.Button(framebtn4, text="Graph 1", command=lambda: show_graph41())
button4.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button5 = tk.Button(framebtn4, text="Graph 2", command=lambda: show_graph42())
button5.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
button6 = tk.Button(framebtn4, text="Graph 3", command=lambda: show_graph43())
button6.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
graph5 = tk.Label(root, text="Graph 5: Information of all accidents that occurred on a Victorian public holiday", font=("Arial", 15))
graph5.pack()

# Fifth Option
framebtn5 = tk.Frame(root)
framebtn5.columnconfigure(0, weight=1)
framebtn5.pack()

button7 = tk.Button(framebtn5, text="Types of Accidents", command=lambda: show_graph5())
button7.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button8 = tk.Button(framebtn5, text="Alcohol Hourly Distrubution", command=lambda: show_graph52())
button8.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

def show_graph1():
    # For a user-selected period, display the information of all accidents that happened in the period.
    date1 = entry1.get()
    date2 = entry2.get()
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year

    if date1 > date2:
        print("Error")
        messagebox.showinfo("Error", "Start date cannot be greater than end date")
    elif date1 == date2:
        crash_data = crash_data[crash_data['YEAR'] == int(date1)]
        plt.figure(figsize=(10,5))
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        plt.title('Types of Accidents between ' + date1 + ' and ' + date2)
        plt.ylabel('')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['ACCIDENT_TYPE'].unique())
        plt.tight_layout()
        plt.show()
    else:

        crash_data = crash_data[(crash_data['YEAR'] >= int(date1)) & (crash_data['YEAR'] <= int(date2))]    
        plt.figure(figsize=(10,5))
        
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        plt.title('Types of Accidents between ' + date1 + ' and ' + date2)
        plt.ylabel('')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['ACCIDENT_TYPE'].unique())
        plt.tight_layout()
        plt.show()      

def show_graph2():
    date1 = entry3.get()
    date2 = entry4.get()
    # For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    if date1 > date2:
        print("Error")
        messagebox.showinfo("Error", "Start date cannot be greater than end date")
    elif date1 == date2:
        crash_data = crash_data[crash_data['YEAR'] == int(date1)]
        crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
        crash_data["HOUR"] = crash_data["HOUR"].astype('int32')
        plt.figure(figsize=(10,5))
        plt.bar(crash_data['HOUR'].value_counts().index, crash_data['HOUR'].value_counts().values)
        plt.title('Number of Accidents in each hour of the day between ' + date1 + ' and ' + date2)
        plt.ylabel('Number of Accidents')
        plt.xlabel('Hour of the day')
        plt.xticks(rotation=0, ticks=crash_data['HOUR'].value_counts().index)
        plt.tight_layout()
        plt.show()
        
    else:
        crash_data = crash_data[(crash_data['YEAR'] >= int(date1)) & (crash_data['YEAR'] <= int(date2))]   
        crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
        crash_data["HOUR"] = crash_data["HOUR"].astype('int32')
        plt.figure(figsize=(10,5))
        plt.bar(crash_data['HOUR'].value_counts().index, crash_data['HOUR'].value_counts().values)
        plt.title('Number of Accidents in each hour of the day between ' + date1 + ' and ' + date2)
        plt.ylabel('Number of Accidents')
        plt.xlabel('Hour of the day')
        plt.xticks(rotation=0, ticks=crash_data['HOUR'].value_counts().index)
        plt.tight_layout()
        plt.show()

def show_graph3():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    date1 = entry6.get()
    date2 = entry7.get()
    keyword = entry5.get()
    if date1 > date2:
        print("Error")
        messagebox.showinfo("Error", "Start date cannot be greater than end date")
    elif date1 == date2:
        crash_data = crash_data[crash_data['YEAR'] == int(date1)]
        crash_data = crash_data[crash_data['ACCIDENT_TYPE'].str.contains(keyword)]
        plt.figure(figsize=(10,5))
        crash_data['FATALITY'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        plt.title('Fatalities between ' + date1 + ' and ' + date2 + ' that contains the keyword ' + keyword)
        plt.ylabel('Number of Fatalities')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['FATALITY'].unique())
        plt.tight_layout()
        plt.show()   
    else:
        crash_data = crash_data[(crash_data['YEAR'] >= int(date1)) & (crash_data['YEAR'] <= int(date2))]   
        crash_data = crash_data[crash_data['ACCIDENT_TYPE'].str.contains(keyword)]
        plt.figure(figsize=(10,5))
        crash_data['FATALITY'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        plt.title('Fatalities between ' + date1 + ' and ' + date2 + ' that contains the keyword ' + keyword)
        plt.ylabel('Number of Fatalities')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['FATALITY'].unique())
        plt.tight_layout()
        plt.show()


# 4.1
def show_graph41():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['YEAR'] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    grouped_data = crash_data.groupby(['YEAR', 'ALCOHOL_RELATED'])['FATALITY'].mean().unstack(fill_value=0)
    plt.figure(figsize=(10, 5))
    num_years = len(grouped_data)
    bar_width = 0.35
    indices = np.arange(num_years)
    plt.bar(
        indices - bar_width/2,
        grouped_data['yes'],
        label='Alcohol Related',
        width=bar_width,
        alpha=0.7
    )
    plt.bar(
        indices + bar_width/2,
        grouped_data['no'],
        label='Non-Alcohol Related',
        width=bar_width,
        alpha=0.7
    )
    plt.xticks(indices, grouped_data.index)
    plt.title('Average Fatalities in Alcohol vs. Non-Alcohol Related Accidents between 2013 and 2019')
    plt.ylabel('Average Fatalities')
    plt.xlabel('Year')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 4.2
def show_graph42():
    crash_data = pd.read_csv('data.csv')    
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()    
    alcohol_related = crash_data[crash_data['ALCOHOL_RELATED'] == 'yes']
    non_alcohol_related = crash_data[crash_data['ALCOHOL_RELATED'] == 'no']
    sorted_alcohol_related = alcohol_related['HOUR'].value_counts().sort_index()
    sorted_non_alcohol_related = non_alcohol_related['HOUR'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(sorted_alcohol_related.index, sorted_alcohol_related.values)
    plt.title('Number of Alcohol-Related Accidents 2013-2019')
    plt.ylabel('Number of Accidents')
    plt.xlabel('Hour of the day')
    plt.xticks(rotation=0)
    plt.subplot(1, 2, 2)
    plt.bar(sorted_non_alcohol_related.index, sorted_non_alcohol_related.values)
    plt.title('Number of Non-Alcohol-Related Accidents 2013-2019')
    plt.ylabel('Number of Accidents')
    plt.xlabel('Hour of the day')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# 4.3
def show_graph43():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    crash_data['DAY_OF_WEEK'] = crash_data['ACCIDENT_DATE'].dt.dayofweek
    crash_data['DAY_OF_WEEK'] = crash_data['DAY_OF_WEEK'].replace([0, 1, 2, 3, 4, 5, 6],['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    alcohol_related = crash_data[crash_data['ALCOHOL_RELATED'] == 'yes']
    non_alcohol_related = crash_data[crash_data['ALCOHOL_RELATED'] == 'no']
    custom_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sorted_alcohol_related = alcohol_related['DAY_OF_WEEK'].value_counts().reindex(custom_order)
    sorted_non_alcohol_related = non_alcohol_related['DAY_OF_WEEK'].value_counts().reindex(custom_order)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.barplot(x=sorted_alcohol_related.index, y=sorted_alcohol_related.values, order=custom_order)
    plt.title('Number of Alcohol-Related Accidents 2013-2019')
    plt.ylabel('Number of Accidents')
    plt.xlabel('Day of the week')
    plt.xticks(rotation=45)
    plt.subplot(1, 2, 2)
    sns.barplot(x=sorted_non_alcohol_related.index, y=sorted_non_alcohol_related.values, order=custom_order)
    plt.title('Number of Non-Alcohol-Related Accidents 2013-2019')
    plt.ylabel('Number of Accidents')
    plt.xlabel('Day of the week')
    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.show()

def show_graph5():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    crash_data['On_Public_Holiday'] = crash_data['ACCIDENT_DATE'].dt.strftime('%d-%m').isin(vicholidays)
    # holiday_counts = crash_data['On_Public_Holiday'].value_counts()
    # plt.figure(figsize=(8, 6))
    # holiday_counts.plot(kind='bar', rot=0)
    # plt.title('Accidents on Victorian Public Holidays (All Available Data)')
    # plt.xlabel('Public Holiday')
    # plt.ylabel('Number of Accidents')
    # plt.xticks([0, 1], ['Not on Public Holiday', 'On Public Holiday'])
    holiday_accident_counts = crash_data.groupby(['On_Public_Holiday', 'ACCIDENT_TYPE'])['ACCIDENT_TYPE'].count().unstack().fillna(0)
    total_accidents_holiday = holiday_accident_counts.loc[True].sum()
    total_accidents_non_holiday = holiday_accident_counts.loc[False].sum()
    holiday_accident_percentage = (holiday_accident_counts.loc[True] / total_accidents_holiday) * 100
    non_holiday_accident_percentage = (holiday_accident_counts.loc[False] / total_accidents_non_holiday) * 100
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.pie(holiday_accident_percentage, labels=holiday_accident_percentage.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Accident Types on Public Holidays')
    plt.subplot(1, 2, 2)
    plt.pie(non_holiday_accident_percentage, labels=non_holiday_accident_percentage.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Accident Types on Non-Holidays')
    plt.tight_layout()
    plt.show()

def show_graph52():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    crash_data['On_Public_Holiday'] = crash_data['ACCIDENT_DATE'].dt.strftime('%d-%m').isin(vicholidays)
    holiday_alcohol_related = crash_data[(crash_data['On_Public_Holiday'] == True) & (crash_data['ALCOHOL_RELATED'] == 'yes')]
    holiday_alcohol_related['HOUR'] = holiday_alcohol_related['HOUR'].astype('int32')
    holiday_alcohol_related = holiday_alcohol_related['HOUR'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.bar(holiday_alcohol_related.index, holiday_alcohol_related.values)
    plt.title('Number of Alcohol-Related Accidents on Public Holidays 2013-2019')
    plt.ylabel('Number of Accidents')
    plt.xlabel('Hour of the day')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

root.mainloop()




    