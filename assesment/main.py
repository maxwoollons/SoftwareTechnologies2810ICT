import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import tkinter as tk


root = tk.Tk()
root.title("Data Visualization Project - Victoria Crash Data")
root.geometry("800x500")
root.iconbitmap("favicon.ico")

label = tk.Label(root, text="Data Visualization", font=("Arial", 20))
label.pack()

graph1 = tk.Label(root, text="Graph 1: Infomation on Crash over a period of time", font=("Arial", 15))
graph1.pack()
button1 = tk.Button(root, text="Show Graph", command=lambda: show_graph1())
button1.pack()

graph2 = tk.Label(root, text="Graph 2: Number of accidents in each hour of the day", font=("Arial", 15))
graph2.pack()

graph3 = tk.Label(root, text="Graph 3: All accidents caused by an accident type that contains a keyword", font=("Arial", 15))
graph3.pack()

graph4 = tk.Label(root, text="Graph 4: Alcohol Impact in accidents", font=("Arial", 15))
graph4.pack()

graph5 = tk.Label(root, text="Graph 5: Information of all accidents that occurred on a Victorian public holiday", font=("Arial", 15))
graph5.pack()

def show_graph1():
    crash_data = pd.read_csv('data.csv')
    crash_data['ACCIDENT_DATE'] = pd.to_datetime(crash_data['ACCIDENT_DATE'], format='%d/%m/%Y')
    crash_data['MONTH'] = crash_data['ACCIDENT_DATE'].dt.month
    crash_data['DAY'] = crash_data['ACCIDENT_DATE'].dt.day
    crash_data["MALES"] = pd.to_numeric(crash_data["MALES"])
    crash_data["FEMALES"] = pd.to_numeric(crash_data["FEMALES"])
    sns.barplot(x="DAY_OF_WEEK",y="INJ_OR_FATAL",data=crash_data)
    plt.show()






root.mainloop()




    