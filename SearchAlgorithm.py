import turtle
from turtle import *
from collections import deque as queue
import sys

#Turtle screen
myturtle = turtle.Screen()
myturtle.setup(720, 480)

point = turtle.Turtle()

# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

class Non(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("white","white")   
        self.shapesize(1, 1, 1)         
        self.penup()                    
        self.speed(10)

class PaleGreen(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("black","PaleGreen")   
        self.shapesize(1, 1, 1)         
        self.penup()                    
        self.speed(10)

class White(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("black","white")   
        self.shapesize(1, 1, 1)         
        self.penup()                    
        self.speed(10)

class Gray(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","gray")
        self.shapesize(1, 1, 1)  
        self.penup()
        self.speed(10)

class Orange(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","orange")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(10)
        
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","yellow")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(10)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","green")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(10)    

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","red")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(10)  

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black","blue")
        self.shapesize(1, 1, 1)
        self.penup()
        self.speed(10)  

def Menu():
    print("1. BFS")
    print("2. Uniform-cost search")
    print("3. Iterative deepening search")
    print("4. Greedy-best first search")
    print("5. Graph-search A*")
    print("Enter your choice")
    choice = int(input())
    drawMatrix(white,gray)
    drawObstacle()
    drawSandG()
    if choice == 1:
        BFS()
        drawRoute(goalX, goalY)
    if choice == 2:
        UCS()
        drawRoute(goalX, goalY)
    if choice == 3:
        IterativeDS()
        drawRoute(goalX, goalY)
    if choice == 4:
        GBFS()
        drawRoute(goalX, goalY)
    if choice == 5:
        GSA()
        drawRoute(goalX, goalY)

def readfile():
    file = open('input.txt','r')
    data = file.read()
    Data = data.split('\n')
    return Data

def drawNumber(x, y, number):
    turtle.penup()
    turtle.goto(-325 + (x * 20), -160 + (y * 20))
    turtle.pendown()
    size = 10
    kind =('Times New Roman', size)
    turtle.write(number, font = kind)
    turtle.ht()

def readHeightAndWidth():
    size = data[0].split(' ')
    w = int(size[0]) + 1
    h = int(size[1]) + 1
    return w, h

def createMatrix():
    #global maze

    for i in range(height):
        for j in range(width):
            if (j == width-1 or (i == height-1 ) or j == 0 or i == 0):
                maze[i][j] = 1
    
def drawMatrix(white, gray):
    createMatrix()
    
    for y in range(height):
        for x in range(width):
            character = maze[y][x]
            PosX = -320 + (x * 20)
            PosY = -150  + (y * 20)
            if character == 0:
                white.goto(PosX, PosY)
                white.stamp()
            if character == 1:
                gray.goto(PosX, PosY)
                gray.stamp()
                
    for y in range(height):
        drawNumber(-1, y, y)    
    for x in range(width):
        drawNumber(x, -1, x) 
        
def drawPos(x, y, color):
    PosX = -320 + (x * 20)
    PosY = -150  + (y * 20)
    color.penup()
    color.goto(PosX, PosY)
    color.stamp()  
    color.pendown()
    color.speed(10)
    
def drawEdge(position1, position2, color):
    x1 = position1[0]
    x2 = position2[0]
    y1 = position1[1]
    y2 = position2[1]
    
    a = y1 - y2
    b = x2 - x1
    c = a * x1 + b * y1
    
    maze[y1][x1] = 2
    maze[y2][x2] = 2
    if x1 == x2:
        if y1 < y2:
            for y1 in range(y1 + 1, y2):
                drawPos(x1, y1, color)
                maze[y1][x1] = 2
        else:
            for y2 in range(y2 + 1, y1):
                drawPos(x1, y2, color)
                maze[y2][x1] = 2
    if y1 == y2:
        if x1 < x2:
            for x1 in range(x1 + 1, x2):
                drawPos(x1, y1, color)
                maze[y1][x1] = 2
        else:
             for x2 in range(x2 + 1, x1):
                drawPos(x2, y1, color)
                maze[y1][x2] = 2
    if abs(a) > abs(b):
        if y1 < y2:
            for y1 in range(y1 + 1, y2):
                x = int((c - b*y1) / a)
                drawPos(x,y1,color)
                maze[y1][x] = 2
        else:
            for y2 in range(y2 + 1, y1):
                x = int((c - b * y2) / a)
                drawPos(x, y2, color)
                maze[y2][x] = 2
    else:
        if x1 < x2:
            for x1 in range(x1 + 1, x2):
                y = int((c - a * x1) / b)
                drawPos(x1, y, color)
                maze[y][x1] = 2
        else:
            for x2 in range(x2 + 1, x1):
                y = int((c - a * y2) / b)
                drawPos(x2, y, color)
                maze[y][x2] = 2
    
def drawObstacle():
    numberOfObs = int(data[2])
    for i in range(3, numberOfObs + 3, 1):
        listofVestices = []
        vestices = data[i].split(" ")
        
        for j in range(0, len(vestices), 2):
            posX = int(vestices[j])
            posY = int(vestices[j + 1])
            listofVestices.append([posX, posY]) 
            drawPos(posX, posY, orange)
        
        for k in range (len(listofVestices)):
            if k == len(listofVestices) - 1:
                drawEdge(listofVestices[-1], listofVestices[0], yellow)
            else:
                drawEdge(listofVestices[k], listofVestices[k + 1], yellow)

def drawSandG():
    global source, goal, sourceX, sourceY, goalX, goalY
    
    SandG = data[1].split(' ')
    sourceX = int(SandG[0])
    sourceY = int(SandG[1])
    goalX = int(SandG[2])
    goalY = int(SandG[3])
    
    source = [sourceX, sourceY]
    goal = [goalX, goalY]
    
    maze[sourceY][sourceX] = 2
    maze[goalY][goalX] = 0
    
    drawPos(sourceX, sourceY, red)
    
    drawPos(goalX, goalY, red) 

# SEARCH ALGORITHM 

# Function to check if a cell
# is be visited or not
def isValid(row, col):
    # If cell lies out of bounds
    if (row < 1 or col < 1 or row > height - 2  or  col > width - 2):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False

    # Otherwise
    return True
 
# Function to perform the BFS traversal
def BFS():
    # Stores indices of the matrix cells
    frontier = queue()
    #Cost of expanding
    global ex_cost
    ex_cost = 0
    # Mark the starting cell as visited
    # and push it into the queue
    frontier.append([ sourceX, sourceY ])
    vis[sourceX][sourceY] = True
    
    #Initialize the first element for the path
    path[(sourceX, sourceY)] =  sourceX, sourceY
    # Iterate while the queue
    # is not empty
    while (frontier):
        cell = frontier.popleft()
        x = cell[0]
        y = cell[1]
 
        # Go to the adjacent cells
        if [x, y] != source and [x, y] != goal: drawPos(x, y, blue)
        for i in range(4):
            adj_y = y + dRow[i]
            adj_x = x + dCol[i]
            if (isValid(adj_y, adj_x) and maze[adj_y][adj_x] == 0):
                if [adj_x, adj_y] != source and [adj_x, adj_y] != goal: 
                    drawPos(adj_x, adj_y, palegreen)
                    ex_cost += 1
                frontier.append([adj_x, adj_y])
                path[(adj_x, adj_y)] = x, y
                vis[adj_y][adj_x] = True
        if [adj_x, adj_y] == goal:
            break 

def UCS():
    # Stores indices of the matrix cells
    frontier = []
    #Cost of expanding
    global ex_cost
    ex_cost = 0
    # Mark the starting cell as visited
    # and push it into the queue
    frontier.append([sourceX, sourceY])
    vis[sourceX][sourceY] = True
    
    path[(sourceX, sourceY)] =  sourceX, sourceY
    #Matrix of cost so as to store from the source to current state
    cost = [[ 0 for i in range(width)] for j in range(height)]
    # Iterate while the queue
    # is not empty
    while (frontier):
        min = sys.maxsize
        index = 0
        # Go to the adjacent cells

        if(len(frontier) > 1):
        #find min
            for i in range(len(frontier) - 1):
                temp = frontier[i]
                if(cost[temp[1]][temp[0]] < min):
                    min = cost[temp[1]][temp[0]]
                    index = i
        cell = frontier.pop(index)
        x = cell[0]
        y = cell[1]
        if [x, y] != source and [x, y] != goal: drawPos(x, y, blue)
        if [x, y] == goal:
            break 
        for i in range(4):
            adj_y = y + dRow[i]
            adj_x = x + dCol[i]
            if (isValid(adj_y, adj_x) and maze[adj_y][adj_x] == 0):
                if [adj_x, adj_y] != source and [adj_x, adj_y] != goal: drawPos(adj_x, adj_y, palegreen)
                frontier.append([adj_x, adj_y])
                cost[adj_y][adj_x] = cost[y][x] + 1
                ex_cost+=1
                vis[adj_y][adj_x] = True
                path[(adj_x, adj_y)] = x, y

def IterativeDS():
    # Stores indices of the matrix cells
    frontier = queue()
    #Cost of expanding
    global ex_cost
    ex_cost = 0
    # Mark the starting cell as visited
    # and push it into the queue
    level = 0
    count = 0
    lev = [[ 0 for i in range(width)] for j in range(height)]
    check = False

    while(check == False):
        frontier.append([sourceX, sourceY])
        lev[sourceY][sourceX] = 0

        for i in range(height):
            for j in range(width):
                vis[i][j] = False
        path.clear()

        vis[sourceY][sourceX] = True
        path[(sourceX, sourceY)] =  sourceX, sourceY
        # Iterate while the queue
        # is not empty
        while(frontier):
            cell = frontier.pop()
            x = cell[0]
            y = cell[1]
            # Go to the adjacent cells
            if [x, y] == goal:
                check = True
                break 
            if(lev[y][x] >= level):
                continue
            if [x, y] != source and [x, y] != goal: drawPos(x, y, blue)
            for i in range(4): 
                adj_y = y + dRow[i]
                adj_x = x + dCol[i]
                if (isValid(adj_y, adj_x) and maze[adj_y][adj_x] == 0):
                    if [adj_x, adj_y] != source and [adj_x, adj_y] != goal: drawPos(adj_x, adj_y, palegreen)
                    frontier.append([adj_x, adj_y])
                    lev[adj_y][adj_x] = lev[y][x] + 1
                    ex_cost+=1
                    vis[adj_y][adj_x] = True
                    path[(adj_x, adj_y)] = x, y
        level += 1

def GBFS():
    # Stores indices of the matrix cells
    frontier = []
    #Cost of expanding
    global ex_cost
    ex_cost = 0
    # Mark the starting cell as visited
    # and push it into the queue
    frontier.append([sourceX, sourceY])
    vis[sourceX][sourceY] = True
    cost = [[ 0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            cost[i][j] = abs(i - goalY) + abs(j - goalX)

    path[(sourceX, sourceY)] =  sourceX, sourceY
    # Iterate while the queue
    # is not empty
    while (frontier):
        index = 0
        min = sys.maxsize
        if(len(frontier) > 1):
        #find min
            for i in range(len(frontier) - 1):
                temp = frontier[i]
                if(cost[temp[1]][temp[0]] < min):
                    min = cost[temp[1]][temp[0]]
                    index = i
        cell = frontier.pop(index)
        x = cell[0]
        y = cell[1]
        if [x, y] != source and [x, y] != goal: drawPos(x, y, blue)
        # Go to the adjacent cells
        for i in range(4):
            adj_y = y + dRow[i]
            adj_x = x + dCol[i]
            if (isValid(adj_y, adj_x) and maze[adj_y][adj_x] == 0):
                if [adj_x, adj_y] != source and [adj_x, adj_y] != goal: drawPos(adj_x, adj_y, palegreen)
                vis[adj_y][adj_x] = True
                ex_cost+=cost[adj_y][adj_x]
                frontier.append([adj_x, adj_y])
                path[(adj_x, adj_y)] = x, y
        if [adj_x, adj_y] == goal:
            break

def GSA():
    frontier = []
    #Cost of expanding
    global ex_cost
    ex_cost = 0
    cost_h = [[ 0 for i in range(width)] for j in range(height)]
    cost_f = [[ 0 for i in range(width)] for j in range(height)]
    
    cost_f[sourceY][sourceX] = 0
    frontier.append(source)

    for i in range(height):
        for j in range(width):
            cost_h[i][j] = abs(i - goalY) + abs(j - goalX)

    path[(sourceX, sourceY)] =  sourceX, sourceY
    
    while(frontier):
        index = 0
        min = sys.maxsize
        if(len(frontier) > 1):
        #find min
            for i in range(len(frontier) - 1):
                temp = frontier[i]
                if(cost_f[temp[1]][temp[0]] + cost_h[temp[1]][temp[0]] < min):
                    min = cost_f[temp[1]][temp[0]] + cost_h[temp[1]][temp[0]]
                    index = i
        cell = frontier.pop(index)
        x = cell[0]
        y = cell[1]
        if [x, y] != source and [x, y] != goal: drawPos(x, y, blue)
        if ([x, y] == goal):
            break
        for i in range(4):
            adj_y = y + dRow[i]
            adj_x = x + dCol[i]
            if (isValid(adj_y, adj_x) and maze[adj_y][adj_x] == 0):
                if [adj_x, adj_y] != source and [adj_x, adj_y] != goal: drawPos(adj_x, adj_y, palegreen)
                vis[adj_y][adj_x] = True
                frontier.append([adj_x, adj_y])
                cost_f[adj_y][adj_x] = cost_f[y][x] + 1
                ex_cost = ex_cost + cost_f[adj_y][adj_x] + cost_h[adj_y][adj_x]
                path[(adj_x, adj_y)] = x, y

def drawRoute(x, y):
    cost = 0
    while(x, y) != (sourceX, sourceY):
        temp_x, temp_y = path[x, y][0], path[x, y][1]
        if(x,y) != (goalX, goalY): 
            drawPos(x, y, green)
        cost += 1
        x, y = temp_x, temp_y

    message = 'Cost of path: ' + str(cost) + "\nCost of expanding: " + str(ex_cost)
    penup()
    goto(250, 100)
    color("black")
    pendown()
    write(message, False, align= 'center',font= ('Times New Roman', 15, 'bold'))   
#--------------------------------------------#
#color initialization
palegreen = PaleGreen()
gray = Gray()
white = White()
orange=Orange() 
yellow = Yellow()
green = Green()
red = Red()
blue = Blue()
none = Non()


#Variable declaration
data = readfile()
width, height = readHeightAndWidth()
vis = [[ False for i in range(width)] for j in range(height)]
maze = [[0 for i in range(width)] for j in range(height)]
path = {}

#Menu
Menu()

#Drawing

#Turtle exit
myturtle.exitonclick()