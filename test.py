from tkinter import *

MainWindow = Tk()

pog = 10

HelloText = Label(MainWindow, text = "Welcome to Dakota's Visual sorts!")
HelloText.grid(row = 0, column = 1)

DelayText = Label(MainWindow, text = "Enter Delay in MS 0-.99 :")
DelayText.grid(row = 2, column = 1)
EnterDelay = Entry(MainWindow, bd = 4)
EnterDelay.grid(row = 3, column = 1)

#BubbleSortButton = Button(MainWindow, text = "Bubble Sort", padx = 10, pady = 10, command = lambda: BubbleSort(pog))
BubbleSortButton = Button(MainWindow, text = "Bubble Sort", padx = 11, pady = 10)
BubbleSortButton.grid(row = 6, column = 0)

SelectionSortButton = Button(MainWindow, text = "Selection Sort", padx = 6, pady = 10)
SelectionSortButton.grid(row = 6, column = 1)

InsertionSortButton = Button(MainWindow, text = "Insertion Sort", padx = 6, pady = 10)
InsertionSortButton.grid(row = 6, column = 2)

QuickSortButton = Button(MainWindow, text = "Quick Sort", padx = 14, pady = 10)
QuickSortButton.grid(row = 7, column = 0)

MergeSortButton = Button(MainWindow, text = "Merge Sort", padx = 14, pady = 10)
MergeSortButton.grid(row = 7, column = 1)

HeapSortButton = Button(MainWindow, text = "Heap Sort", padx = 15, pady = 10)
HeapSortButton.grid(row = 7, column = 2)

CountingSortButton = Button(MainWindow, text = "Counting Sort", padx = 7, pady = 10)
CountingSortButton.grid(row = 8, column = 1)

MainWindow.mainloop()