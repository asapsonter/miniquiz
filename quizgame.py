from tkinter import *
from tkinter import ttk
from typing import TextIO

# create frame
y = 0
a =ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

# add framework with text
def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="QS")
    # use lable to display the questions and font size
    Label(frame1, text="Nigeria has how many states?", font = ("Ariel", 55, "bold")). grid(row=2, column=2)
    # create options buttons
    Button(frame1, text= "36", font=("Ariel", 30 , "bold"),bg="lightgreen", command=correct_ans).grid(row=3, column=1)
    Button(frame1, text= "26", font=("Ariel", 30 , "bold"),bg="lightgreen", command=wrong_ans).grid(row=3, column=2)
    Button(frame1, text= "40", font=("Ariel", 30 , "bold"),bg="lightgreen", command=wrong_ans).grid(row=3, column=2)
    
    # question 2
    Label(frame2, text="In what year did Nigeria gain her Indepence?", font = ("Ariel", 55, "bold")). grid(row=2, column=2)
    
    Button(frame2, text= "1872", font=("Ariel", 30 , "bold"),bg="lightblue", command=wrong_ans2).grid(row=3, column=1)
    Button(frame2, text= "1990", font=("Ariel", 30 , "bold"),bg="lightblue", command=wrong_ans2).grid(row=3, column=2)
    Button(frame2, text= "1960", font=("Ariel", 30 , "bold"),bg="lightblue", command=correct_ans2).grid(row=3, column=2)
    
    # question 3
    Label(frame3, text="What is the capital of Nigeria?", font = ("Ariel", 55, "bold")). grid(row=2, column=2)
    
    Button(frame3, text= "Lagos", font=("Ariel", 30 , "bold"),bg="blue", command=wrong_ans3).grid(row=3, column=1)
    Button(frame3, text= "Benue", font=("Ariel", 30 , "bold"),bg="blue", command=wrong_ans3).grid(row=3, column=2)
    Button(frame3, text= "Abuja", font=("Ariel", 30 , "bold"),bg="blue", command=correct_ans3).grid(row=3, column=2)
    
    # question 4
    Label(frame3, text="Which is the most spoken local dilect in Nigeria", font = ("Ariel", 55, "bold")). grid(row=2, column=2)
    
    Button(frame4, text= "Hausa", font=("Ariel", 30 , "bold"),bg="black", command=correct_ans4).grid(row=3, column=1)
    Button(frame4, text= "Igbo", font=("Ariel", 30 , "bold"),bg="black", command=wrong_ans4).grid(row=3, column=2)
    Button(frame4, text= "Tiv", font=("Ariel", 30 , "bold"),bg="black", command=wrong_ans4).grid(row=3, column=3)
    
    # question 5
    Label(frame5, text="Which is the most popular sport in Nigeria", font = ("Ariel", 55, "bold")). grid(row=2, column=2)
    
    Button(frame5, text= "Handball", font=("Ariel", 30 , "bold"),bg="pink", command=wrong_ans5).grid(row=3, column=1)
    Button(frame5, text= "Basketball", font=("Ariel", 30 , "bold"),bg="pink", command=wrong_ans5).grid(row=3, column=2)
    Button(frame5, text= "Football", font=("Ariel", 30 , "bold"),bg="pink", command=correct_ans5).grid(row=3, column=3)
    
# functions to declare wrong anf right ans 
def correct_ans():
    Label(frame1, text = "Right!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame1, text = "Scores: 1", font = ("Ariel", 45 , "bold"), background="grey", fg= "blue").grid(row=1, column=2)
    
def wrong_ans():
    Label(frame1, text = "Wrong!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame1, text = "Scores: 0", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def correct_ans2():
    Label(frame2, text = "Right!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame2, text = "Scores: 1", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def wrong_ans2():
    Label(frame2, text = "Wrong!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame2, text = "Scores: 0", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def correct_ans3():
    Label(frame3, text = "Right!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame3, text = "Scores: 1", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def wrong_ans3():
    Label(frame3, text = "Wrong!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame3, text = "Scores: 0", font = ("Ariel", 45 , "bold"), background="red", fg= "red").grid(row=1, column=2)

def correct_ans4():
    Label(frame4, text = "Right!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame4, text = "Scores: 1", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def wrong_ans4():
    Label(frame4, text = "Wrong!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame4, text = "Scores: 0", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)

def correct_ans5():
    Label(frame5, text = "Right!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame5, text = "Scores: 1", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=2)
    
def wrong_ans5():
    Label(frame5, text = "Wrong!", font = ("Ariel", 45 , "bold"), background ="green", fg = "blue").grid(row=1, column=1)
    Label(frame5, text = "Scores: 0", font = ("Ariel", 45 , "bold"), background="grey", fg= "red").grid(row=1, column=3)

quiz(y)

a.pack()
a.mainloop()