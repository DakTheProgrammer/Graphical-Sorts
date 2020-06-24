from graphics import *
import random

def Main(Numbers):
    Window = GraphWin("The Window", 500, 500)
    Window.setBackground(color_rgb(0,0,0))

    CloseMessage = Text(Point(75, 10), "Click Screen to close")
    CloseMessage.setTextColor("white")
    CloseMessage.setFace("times roman")

    CloseMessage.draw(Window)
    
    #bubbleSort(Numbers, Window)
    DrawGraph(Window, Numbers)

    

    Window.getMouse()
    Window.close()

def DrawGraph(Window, Numbers):
    Recs = []
    i = 0

    while i < 100:
        Recs.insert(i, Rectangle(Point(0 + (i * 5), 500), Point(5 + (i * 5), Numbers[i])))
        Recs[i].setFill("white")
        Recs[i].draw(Window)
        i += 1

def Data():
    Numbers = []
    scale = []

    i = 0

    while i < 100:
        scale.insert(i, 491 - 4 * (i - 1))  

        i += 1
    
    i = 0

    while i < 100:
        Numbers.insert(i ,random.randint(1,100))

        Numbers[i] = scale[Numbers[i] - 1]

        i += 1

    return Numbers

def bubbleSort(arr, Window): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                DrawGraph(Window,arr)
                

Main(Data())