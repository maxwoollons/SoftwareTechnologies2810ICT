import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import numpy as np
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

# Day-Month
vicholidays = ['1-1','2-1','26-1','13-3','7-4','8-4','9-4','10-4','25-4','12-6','29-9','7-11','25-12','26-12']



root = tk.Tk()
root.title("Data Visualization Project - Victoria Crash Data")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.iconbitmap("logo.ico")

style = ttk.Style()
style.theme_use('clam')

label = tk.Label(root,font=("Helvetica", 20), text="Data Visualization")
# image = tk.PhotoImage(file="logo.png")
label.pack()
# label.config(image=image,compound='right')


# First Option

graph1 = tk.Label(root, text="Graph 1: Infomation on Crash over a period of time", font=("Helvetica", 15))
graph1.pack()
framebtn1 = tk.Frame(root)
framebtn1.columnconfigure(0, weight=1)
framebtn1.columnconfigure(1, weight=1)
framebtn1.columnconfigure(2, weight=1)
framebtn1.pack()

button1 = ttk.Button(framebtn1, text="Show Graph", command=lambda: show_graph1())
button1.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
entry1 = tk.StringVar()
drop = ttk.OptionMenu(framebtn1, entry1,"Start Year", *options)
drop.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry2 = tk.StringVar()
entry2.set("End Year")
drop2 = ttk.OptionMenu(framebtn1, entry2,"End Year", *options)
drop2.grid(row=0, column=1, sticky="ew", padx=5, pady=5)






# Second Option


graph2 = tk.Label(root, text="Graph 2: Number of accidents in each hour of the day", font=("Helvetica", 15))
graph2.pack()

framebtn2 = tk.Frame(root)
framebtn2.columnconfigure(0, weight=1)
framebtn2.columnconfigure(1, weight=1)
framebtn2.columnconfigure(2, weight=1)
framebtn2.pack()
button2 = ttk.Button(framebtn2, text="Show Graph", command=lambda: show_graph2())
button2.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
entry3 = tk.StringVar()
drop1 = ttk.OptionMenu(framebtn2, entry3,"Start Year", *options)
drop1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry4 = tk.StringVar()
drop5 = ttk.OptionMenu(framebtn2, entry4,"End Year", *options)
drop5.grid(row=0, column=1, sticky="ew", padx=5, pady=5)


# Third Option
# (Drop down box)

graph3 = tk.Label(root, text="Graph 3: All accidents caused by an accident type that contains a keyword", font=("Helvetica", 15))
graph3.pack()
framebtn3 = tk.Frame(root)
framebtn3.columnconfigure(0, weight=1)
framebtn3.columnconfigure(1, weight=1)
framebtn3.columnconfigure(2, weight=1)
framebtn3.columnconfigure(3, weight=1)
framebtn3.pack()
button3 = ttk.Button(framebtn3, text="Show Graph", command=lambda: show_graph3())
button3.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
entry5 = tk.StringVar()

# This needs to be an entry box
drop6 = ttk.Entry(framebtn3, textvariable=entry5, width=30)
drop6.insert(0, "")
drop6.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry6 = tk.StringVar()

drop7 = ttk.OptionMenu(framebtn3, entry6,"Select Year", *options)
drop7.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Fourth Option
graph4 = tk.Label(root, text="Graph 4: Alcohol Impact in accidents", font=("Helvetica", 15))
graph4.pack()
framebtn4 = tk.Frame(root)
framebtn4.columnconfigure(0, weight=1)
framebtn4.columnconfigure(1, weight=1)
framebtn4.columnconfigure(2, weight=1)
framebtn4.pack()
button4 = ttk.Button(framebtn4, text="Graph 1", command=lambda: show_graph41())
button4.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button5 = ttk.Button(framebtn4, text="Graph 2", command=lambda: show_graph42())
button5.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
button6 = ttk.Button(framebtn4, text="Graph 3", command=lambda: show_graph43())
button6.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
graph5 = tk.Label(root, text="Graph 5: Information of all accidents that occurred on a Victorian public holiday", font=("Helvetica", 15))
graph5.pack()

# Fifth Option
framebtn5 = tk.Frame(root)
framebtn5.columnconfigure(0, weight=1)
framebtn5.pack()
button7 = ttk.Button(framebtn5, text="Types of Accidents", command=lambda: show_graph5())
button7.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button8 = ttk.Button(framebtn5, text="Alcohol Hourly Distrubution", command=lambda: show_graph52())
button8.grid(row=0, column=1, sticky="ew", padx=5, pady=5)



# Bottom of the page for graphs
bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
bottomframe.grid_rowconfigure(0, weight=1)
bottomframe.grid_columnconfigure(0, weight=1)


def show_graph1():
    # For a user-selected period, display the information of all accidents that happened in the period.
    # GUI Intergration complete
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
        fig, ax = plt.subplots(figsize=(10, 5))
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        ax.set_title('Types of Accidents between ' + date1 + ' and ' + date2)
        ax.set_ylabel('')
        ax.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['ACCIDENT_TYPE'].unique())
        if hasattr(bottomframe, 'chart_type'):
            bottomframe.chart_type.get_tk_widget().destroy()
        chart_type = FigureCanvasTkAgg(fig, bottomframe)
        chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        bottomframe.chart_type = chart_type


    else:
        crash_data = crash_data[(crash_data['YEAR'] >= int(date1)) & (crash_data['YEAR'] <= int(date2))]    
        fig, ax = plt.subplots(figsize=(10, 5))
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%', labels=None)
        ax.set_title('Types of Accidents between ' + date1 + ' and ' + date2)
        ax.set_ylabel('')
        ax.legend(loc='upper left', bbox_to_anchor=(-0.6, 0.6), labels=crash_data['ACCIDENT_TYPE'].unique())
        if hasattr(bottomframe, 'chart_type'):
            bottomframe.chart_type.get_tk_widget().destroy()
        chart_type = FigureCanvasTkAgg(fig, bottomframe)
        chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        bottomframe.chart_type = chart_type

def show_graph2():
    # GUI Intergration complete
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
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.bar(crash_data['HOUR'].value_counts().index, crash_data['HOUR'].value_counts().values)
        ax.set_title('Number of Accidents in each hour of the day between ' + date1 + ' and ' + date2)
        ax.set_ylabel('Number of Accidents')
        ax.set_xlabel('Hour of the day')
        ax.set_xticks(crash_data['HOUR'].value_counts().sort_index().index)
        ax.set_xticklabels(crash_data['HOUR'].value_counts().sort_index().index, rotation=45)
        if hasattr(bottomframe, 'chart_type'):
            bottomframe.chart_type.get_tk_widget().destroy()
        chart_type = FigureCanvasTkAgg(fig, bottomframe)
        chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        bottomframe.chart_type = chart_type
        
    else:
        crash_data = crash_data[(crash_data['YEAR'] >= int(date1)) & (crash_data['YEAR'] <= int(date2))]   
        crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
        crash_data["HOUR"] = crash_data["HOUR"].astype('int32')
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.bar(crash_data['HOUR'].value_counts().index, crash_data['HOUR'].value_counts().values)
        ax.set_title('Number of Accidents in each hour of the day between ' + date1 + ' and ' + date2)
        ax.set_ylabel('Number of Accidents')
        ax.set_xlabel('Hour of the day')
        ax.set_xticks(crash_data['HOUR'].value_counts().sort_index().index)
        ax.set_xticklabels(crash_data['HOUR'].value_counts().sort_index().index, rotation=45)
        if hasattr(bottomframe, 'chart_type'):
            bottomframe.chart_type.get_tk_widget().destroy()
        chart_type = FigureCanvasTkAgg(fig, bottomframe)
        chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        bottomframe.chart_type = chart_type

def show_graph3():
    # GUI Intergration complete
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ACCIDENT_TYPE'] = crash_data['ACCIDENT_TYPE'].str.lower()
    date1 = entry6.get()
    # date2 = entry7.get()
    keyword = entry5.get()
    keyword = keyword.lower()
    if date1 == "Select Year":
        print("Error")
        messagebox.showinfo("Error", "Please Select a year")
    else:
        crash_data = crash_data[crash_data['YEAR'] == int(date1)]
        crash_data = crash_data[crash_data['ACCIDENT_TYPE'].str.contains(keyword)]
        if crash_data.empty:
            messagebox.showinfo("Error", "No results, please try again")
        else:
            fig, ax = plt.subplots(figsize=(10, 5))
            crash_data['MONTH'].value_counts().sort_index().plot(kind='bar')
            ax.set_title('Number of Accidents containing the word \"' + keyword + '\" in ' + date1)
            ax.set_ylabel('Number of Accidents')
            ax.set_xlabel('Month')
            ax.set_xticks(ticks=crash_data['MONTH'].value_counts().sort_index().index)
            if hasattr(bottomframe, 'chart_type'):
                bottomframe.chart_type.get_tk_widget().destroy()
            chart_type = FigureCanvasTkAgg(fig, bottomframe)
            chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
            bottomframe.chart_type = chart_type


# 4.1
def show_graph41():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['YEAR'] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    grouped_data = crash_data.groupby(['YEAR', 'ALCOHOL_RELATED'])['FATALITY'].mean().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 5))
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
    ax.set_xticks(indices, grouped_data.index)
    ax.set_title('Average Fatalities in Alcohol vs. Non-Alcohol Related Accidents between 2013 and 2019')
    ax.set_ylabel('Average Fatalities')
    ax.set_xlabel('Year')
    ax.legend()
    if hasattr(bottomframe, 'chart_type'):
        bottomframe.chart_type.get_tk_widget().destroy()
    chart_type = FigureCanvasTkAgg(fig, bottomframe)
    chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bottomframe.chart_type = chart_type

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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.bar(sorted_alcohol_related.index, sorted_alcohol_related.values)
    ax1.set_title('Number of Alcohol-Related Accidents 2013-2019')
    ax1.set_ylabel('Number of Accidents')
    ax1.set_xlabel('Hour of the day')
    ax2.bar(sorted_non_alcohol_related.index, sorted_non_alcohol_related.values)
    ax2.set_title('Number of Non-Alcohol-Related Accidents 2013-2019')
    ax2.set_ylabel('Number of Accidents')
    ax2.set_xlabel('Hour of the day')
    if hasattr(bottomframe, 'chart_type'):
        bottomframe.chart_type.get_tk_widget().destroy()
    chart_type = FigureCanvasTkAgg(fig, bottomframe)
    chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bottomframe.chart_type = chart_type

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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(x=sorted_alcohol_related.index, y=sorted_alcohol_related.values, order=custom_order, ax=ax1)
    ax1.set_title('Number of Alcohol-Related Accidents (All Data)')
    ax1.set_ylabel('Number of Accidents')
    ax1.set_xlabel('Day of the week')
    ax1.set_xticklabels(ax1.get_xticklabels())
    sns.barplot(x=sorted_non_alcohol_related.index, y=sorted_non_alcohol_related.values, order=custom_order, ax=ax2)
    ax2.set_title('Number of Non-Alcohol-Related Accidents (All Data)')
    ax2.set_ylabel('Number of Accidents')
    ax2.set_xlabel('Day of the week')
    ax2.set_xticklabels(ax2.get_xticklabels())
    if hasattr(bottomframe, 'chart_type'):
        bottomframe.chart_type.get_tk_widget().destroy()
    chart_type = FigureCanvasTkAgg(fig, bottomframe)
    chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bottomframe.chart_type = chart_type

def show_graph5():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['On_Public_Holiday'] = crash_data['ACCIDENT_DATE'].dt.strftime('%d-%m').isin(vicholidays)
    holiday_data = crash_data[crash_data['On_Public_Holiday']]
    non_holiday_data = crash_data[~crash_data['On_Public_Holiday']]
    holiday_counts = holiday_data['ACCIDENT_TYPE'].value_counts()
    non_holiday_counts = non_holiday_data['ACCIDENT_TYPE'].value_counts()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.pie(holiday_counts, labels=holiday_counts.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    ax1.set_title('Accident Types on Public Holidays (All Data)')
    ax2.pie(non_holiday_counts, labels=non_holiday_counts.index, autopct='%1.1f%%', startangle=140)
    ax2.axis('equal')
    ax2.set_title('Accident Types on Non-Holidays (All Data)')
    if hasattr(bottomframe, 'chart_type'):
        bottomframe.chart_type.get_tk_widget().destroy()
    chart_type = FigureCanvasTkAgg(fig, bottomframe)
    chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bottomframe.chart_type = chart_type

def show_graph52():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["YEAR"] = crash_data['ACCIDENT_DATE'].dt.year
    crash_data['ALCOHOL_RELATED'] = crash_data['ALCOHOL_RELATED'].str.lower()
    crash_data['On_Public_Holiday'] = crash_data['ACCIDENT_DATE'].dt.strftime('%d-%m').isin(vicholidays)
    holiday_alcohol_related = crash_data[(crash_data['On_Public_Holiday']) & (crash_data['ALCOHOL_RELATED'] == 'yes')]
    holiday_alcohol_related['HOUR'] = holiday_alcohol_related['HOUR'].astype('int32')
    sorted_holiday_alcohol_related = holiday_alcohol_related['HOUR'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sorted_holiday_alcohol_related.index, sorted_holiday_alcohol_related.values)
    ax.set_title('Number of Alcohol-Related Accidents on Public Holidays 2013-2019')
    ax.set_ylabel('Number of Accidents')
    ax.set_xlabel('Hour of the day')
    ax.set_xticks(sorted_holiday_alcohol_related.index)
    ax.set_xticklabels(sorted_holiday_alcohol_related.index, rotation=0)
    fig.tight_layout()
    if hasattr(bottomframe, 'chart_type'):
        bottomframe.chart_type.get_tk_widget().destroy()
    chart_type = FigureCanvasTkAgg(fig, bottomframe)
    chart_type.get_tk_widget().grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bottomframe.chart_type = chart_type

root.mainloop()




    