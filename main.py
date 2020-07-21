from graphics import GraphWin, color_rgb, Text, Point, Rectangle, Point
import random
import time

def Main():
    Window = MakeWin()

    Nums = RanNums()

    Recs = MakeGraph(Nums, Window)

    #BubbleSort(Nums, Recs, Window)
    #SelectionSort(Nums, Recs, Window)
    #InsertionSort(Nums, Recs, Window)
    #QuickSort(Nums, Recs, Window)
    #MergeSort(Nums, Recs, Window)
    #HeapSort(Nums, Recs, Window)
    #CountingSort(Nums, Recs, Window)

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

def RanNums():
    Nums = []

    for i in range(0, 50):
        Nums.insert(i, random.randint(1, 100))
    
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

def DisplayChange(Nums, Recs, Window):
    ClearGraph(Recs)
    Recs = MakeGraph(Nums, Window)
    #time.sleep(.3) #<----------comment this to see it in its fastest iteration
    return Recs

def BubbleSort(Nums, Recs, Window): 
    n = len(Nums) - 1 

    for i in range(n): 
        for j in range(0, n-i): 
            if Nums[j] > Nums[j+1] :
                Nums[j], Nums[j+1] = Nums[j+1], Nums[j]
                Recs = DisplayChange(Nums, Recs, Window)

def SelectionSort(Nums, Recs, Window):
    for i in range(len(Nums)): 
        
        min_idx = i 
        for j in range(i+1, len(Nums)): 
            if Nums[min_idx] > Nums[j]: 
                min_idx = j 
                
        Nums[i], Nums[min_idx] = Nums[min_idx], Nums[i]
        Recs = DisplayChange(Nums, Recs, Window) 

def InsertionSort(Nums, Recs, Window):
    for i in range(len(Nums)): 
        min_idx = i 

        for j in range(i+1, len(Nums)): 
            if Nums[min_idx] > Nums[j]: 
                min_idx = j 
                      
        Nums[i], Nums[min_idx] = Nums[min_idx], Nums[i]
        Recs = DisplayChange(Nums, Recs, Window) 

def QuickSort(Nums, Recs, Window): 
  
    l = 0
    h = 49
    
    size = h - l + 1
    stack = [0] * (size) 
  
    top = -1
  
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1

        i = ( l - 1 ) 
        x = Nums[h] 
    
        for j in range(l, h): 
            if   Nums[j] <= x:  
                i = i + 1
                Nums[i], Nums[j] = Nums[j], Nums[i] 
    
        Nums[i + 1], Nums[h] = Nums[h], Nums[i + 1]
        p = (i + 1) 

        Recs = DisplayChange(Nums, Recs, Window) 
  
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def MergeSort(Nums, Recs, Window):  
      
    current_size = 1
      
    while current_size < len(Nums) - 1:  
          
        left = 0

        while left < len(Nums)-1:  
              
            mid = min((left + current_size - 1),(len(Nums)-1)) 
            
            right = ((2 * current_size + left - 1,  
                    len(Nums) - 1)[2 * current_size  
                        + left - 1 > len(Nums)-1])  
                              
            n1 = mid - left + 1
            n2 = right - mid  
            L = [0] * n1  
            R = [0] * n2  
            for i in range(0, n1):  
                L[i] = Nums[left + i]  
            for i in range(0, n2):  
                R[i] = Nums[mid + i + 1]  
        
            i, j, k = 0, 0, left  
            while i < n1 and j < n2:  
                if L[i] > R[j]:  
                    Nums[k] = R[j]  
                    j += 1
                else:  
                    Nums[k] = L[i]  
                    i += 1
                k += 1
        
            while i < n1:  
                Nums[k] = L[i]  
                i += 1
                k += 1
        
            while j < n2:  
                Nums[k] = R[j]  
                j += 1
                k += 1

            Recs = DisplayChange(Nums, Recs, Window)
            left = left + current_size*2

        current_size = 2 * current_size
    
def Heapify(Nums, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
  
    if l < n and Nums[i] < Nums[l]: 
        largest = l 

    if r < n and Nums[largest] < Nums[r]: 
        largest = r 
   
    if largest != i: 
        Nums[i],Nums[largest] = Nums[largest],Nums[i] 

        Heapify(Nums, n, largest) 
    
def HeapSort(Nums, Recs, Window): 
    n = len(Nums) 
  
    for i in range(n//2 - 1, -1, -1): 
        Heapify(Nums, n, i) 
  
    for i in range(n-1, 0, -1): 
        Nums[i], Nums[0] = Nums[0], Nums[i]
        Recs = DisplayChange(Nums, Recs, Window) 
        Heapify(Nums, i, 0) 

def CountingSort(Nums, Recs, Window):
    max_val = 100
    m = max_val + 1
    count = [0] * m                
    
    for a in Nums:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for _ in range(count[a]):  
            Nums[i] = a
            i += 1
            Recs = DisplayChange(Nums, Recs, Window)  

Main()