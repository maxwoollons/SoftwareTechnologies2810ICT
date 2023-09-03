import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox


options = [
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019"  
]

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

button2 = tk.Button(framebtn2, text="Show Graph", command=lambda: show_graph1())
button2.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry3 = tk.Entry(framebtn2)
entry3.insert(0,"Start: yyyy (Min: 2013)")
entry3.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry4 = tk.Entry(framebtn2)
entry4.insert(0,"End: yyyy (Max: 2019)")
entry4.grid(row=0, column=2, sticky="ew", padx=5, pady=5)


# Third Option

graph3 = tk.Label(root, text="Graph 3: All accidents caused by an accident type that contains a keyword", font=("Arial", 15))
graph3.pack()

framebtn3 = tk.Frame(root)
framebtn3.columnconfigure(0, weight=1)
framebtn3.columnconfigure(1, weight=1)

framebtn3.pack()

button3 = tk.Button(framebtn3, text="Show Graph", command=lambda: show_graph1())
button3.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry5 = tk.Entry(framebtn3)
entry5.insert(0,"Keyword")
entry5.grid(row=0, column=1, sticky="ew", padx=5, pady=5)


# Fourth Option

graph4 = tk.Label(root, text="Graph 4: Alcohol Impact in accidents", font=("Arial", 15))
graph4.pack()
framebtn4 = tk.Frame(root)
framebtn4.columnconfigure(0, weight=1)
framebtn4.columnconfigure(1, weight=1)
framebtn4.columnconfigure(2, weight=1)
framebtn4.pack()

button4 = tk.Button(framebtn4, text="Show Graph 1", command=lambda: show_graph1())
button4.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button5 = tk.Button(framebtn4, text="Show Graph 2", command=lambda: show_graph1())
button5.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
button6 = tk.Button(framebtn4, text="Show Graph 3", command=lambda: show_graph1())
button6.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

graph5 = tk.Label(root, text="Graph 5: Information of all accidents that occurred on a Victorian public holiday", font=("Arial", 15))
graph5.pack()


# Fifth Option
framebtn5 = tk.Frame(root)
framebtn5.columnconfigure(0, weight=1)
framebtn5.pack()
button7 = tk.Button(framebtn5, text="Show Graph", command=lambda: show_graph1())
button7.grid(row=0, column=0, sticky="ew", padx=5, pady=5)



def show_graph1():
    # For a user-selected period, display the information of all accidents that happened in the period.
    date1 = entry1.get()
    date2 = entry2.get()
    print(date1)
    print(date2)

    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["HOUR"] = crash_data['ACCIDENT_TIME'].str[:2]
    crash_data["MALES"] = pd.to_numeric(crash_data["MALES"])
    crash_data["FEMALES"] = pd.to_numeric(crash_data["FEMALES"])
    if date1 > date2:
        print("Error")
        messagebox.showinfo("Error", "Start date cannot be greater than end date")
    elif date1 == date2:
        crash_data = crash_data[crash_data['ACCIDENT_DATE'] == date1]
        plt.figure(figsize=(10,5))
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%')
        plt.title('Types of Accidents')
        plt.ylabel('')
        plt.show()
    else:
        crash_data = crash_data[(crash_data['ACCIDENT_DATE'] >= date1) & (crash_data['ACCIDENT_DATE'] <= date2)]    
        plt.figure(figsize=(10,5))
        
        crash_data['ACCIDENT_TYPE'].value_counts().plot(kind='pie',autopct='%1.1f%%')
        plt.title('Types of Accidents')
        plt.ylabel('')
        plt.show()
        


def show_graph2():
    # For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).
    crash_data = pd.read_csv('data.csv')


def show_graph3():
    # For a user-selected period, retrieve all accidents caused by an accident type that contains a keyword (user entered), e.g. collision, pedestrian.
    crash_data = pd.read_csv('data.csv')

def show_graph4():
    # Allow the user to analyze the impact of alcohol in accidents – ie: trends over time, accident types involving alcohol, etc.
    crash_data = pd.read_csv('data.csv')

def show_graph5():
    # For a user-selected period, display the information of all accidents that occurred on a Victorian public holiday.
    crash_data = pd.read_csv('data.csv')






root.mainloop()




    