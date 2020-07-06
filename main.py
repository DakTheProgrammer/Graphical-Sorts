from graphics import GraphWin, color_rgb, Text, Point, Rectangle, Point
import random
import time

def Main():
    Window = MakeWin()

    Nums = RanArray()

    Recs = MakeGraph(Nums, Window)

    bubbleSort(Nums, Recs, Window)

    Window.getMouse()
    Window.close()
    
def MakeWin():
    Window = GraphWin("The Window", 500, 500)
    Window.setBackground(color_rgb(0,255,255))

    CloseMessage = Text(Point(140, 490), "Click Screen to close when done sorting")
    CloseMessage.setTextColor("Black")
    CloseMessage.setFace("times roman")

    CloseMessage.draw(Window)

    return Window

def RanArray():
    Nums = []

    for i in range(0, 50):
        Nums.insert(i, random.randint(1, 100))

    print(Nums) 
    
    return Nums

def MakeGraph(Nums, Window):
    Recs = []

    for i in range(0,50):
        Recs.insert(i, Rectangle(Point(0 + (i * 10), 0), Point(10 + (i * 10), Nums[i] * 4))) #(-W, -H), (W, H) W = 0 is top left
        Recs[i].setFill("blue") 
        Recs[i].setOutline("white")
        Recs[i].draw(Window)

    return Recs

def ClearGraph(Recs) :
    for i in range(len(Recs)):
        Recs[i].undraw()

def bubbleSort(arr, Recs, Window): 
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
                ClearGraph(Recs)
                Recs = MakeGraph(arr, Window)
                time.sleep(.3) #<----------comment this to see it in its fastest iteration

Main()