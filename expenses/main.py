import csv #The Csv Writer
import pandas as pd #convert csv to html table
import matplotlib.pyplot as plt #To Create The Visual Plot

#as long as it is yes the code will be reexecuted

reexecution = 'yes'

#input appears everytime the code is executed

while reexecution == 'yes':
    inputdescription = input("Enter The Name: ")
    inputmoney = input("Enter The Amount: ")
    inputdate  = input("Enter The Date (yyyy/mm/dd): ")
    inputshop = input("Enter The Shop: ")

    #after the user inputted everything The Code Should Save EvryThing To A CSV File Called expenses.CSV

    with open("expenses.csv", "a", newline="\n") as writer:
        csvwriter = csv.writer(writer)
        csvwriter.writerow([inputmoney, inputdate, inputdescription, inputshop])
        writer.close()

    #To Create An Html Table Named "Expenses.html"

    a = pd.read_csv('expenses.csv')
    a.to_html('expenses.html')
    html_file = a.to_html()
    print(a.head())

    #To Create A Visual Plot Using pandas And matplotlib
    
    graphics = str(input("do you want the graphics to appear?: "))
    if graphics == 'yes' or graphics == 'y':
        plt.style.use('bmh')
        df = pd.read_csv('expenses.csv')
        x = df["Amounts"]
        y = df['Date']
        plt.xlabel('Amounts', fontsize=18)
        plt.ylabel('Date', fontsize=18)
        plt.bar(x,y)
        plt.show()
    else: 
        print("as you like babe")
    toreexecute = str(input("do you want to reexecute?: "))
    if toreexecute == 'yes' or toreexecute == 'y':
        reexecution = 'yes'
    else:
        reexecution == 'no'
        print("thanks for passing by")
        break





