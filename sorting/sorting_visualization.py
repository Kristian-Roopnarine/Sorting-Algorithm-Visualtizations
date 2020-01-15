import sys
import pygame
import time
from pygame.locals import *
import random

# set up constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
HEIGHT = 800
WIDTH = 800
ARRAYSIZE = (600, 300)
FPS = 60
mainClock = pygame.time.Clock()


class App:

    def __init__(self, height, width, background):
        self.width = height
        self.height = width
        self.background = background
        self.window = pygame.display.set_mode((HEIGHT, WIDTH))

    def start_app(self):
        array = create_array()
        array_rectangles = create_rectangles(array)
        draw_rectangles(array_rectangles,self.window)
        cooldownTimer = 0

        #loop to get window showing
        array_sorted = False
        quicksort_button = Button(WHITE,50,50,100,100,'Quicksort me!')
        new_array_button = Button(WHITE,300,50,120,100,'Create new Array')
        insertion_sort_button = Button(WHITE,175,50,100,100,'Insert sort me!')

        while True:
            quicksort_button.draw(self.window)
            new_array_button.draw(self.window)
            insertion_sort_button.draw(self.window)
            cooldownTimer += 1
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    sys.exit(1)


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quicksort_button.isOver(pos) and not array_sorted:
                        array_sorted = True
                        quicksort(array,self.window,array_rectangles)
                    if new_array_button.isOver(pos):
                        array_sorted = False
                        self.window.fill(BLACK)
                        array = create_array()
                        array_rectangles = create_rectangles(array)
                        draw_rectangles(array_rectangles,self.window)
                    if insertion_sort_button.isOver(pos) and not array_sorted:
                        array_sorted = True
                        insertionSort(array,self.window)
                        #array_rectangles = create_rectangles(array)
                        #self.window.fill(BLACK)
                        #draw_rectangles_insertion(array_rectangles,self.window)


                mainClock.tick(FPS)

            pygame.display.update()
    
class Button:
    def __init__(self,color,x,y,width,height,text=''):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font=pygame.font.SysFont('comicsans',20)
            text = font.render(self.text,1,BLACK)
            win.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self,pos):
        # Pos is the position of the mouse as a tuple of (x,y) coordinates.
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class Text:
    def __init__(self,color,text,width,height,x,y):
        self.color = color
        self.text=text
        self.width=width
        self.height = height
        self.x = x
        self.y = y

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)
        font=pygame.font.SysFont('comicsans',20)
        text = font.render(self.text,1,WHITE)
        win.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))


def create_rectangles(arr):
    array_rectangles = []
    rectangle_width = ARRAYSIZE[0]//len(arr)
    for i in range(len(arr)):
    # the (1 + i) helps space the bars out to give a "line" effect
        b = pygame.Rect(50 + (rectangle_width * i + (1+i)), 700, rectangle_width, -arr[i]*300)
        array_rectangles.append(b)
    return array_rectangles

def update_quicksort(A,win,pivot,border=None,current=None):
    """
    Parameters- 
    A: Current array being sorted.
    win: surface object to draw the updated array on.
    pivot: the pivot index for quicksort
    border: border index for quicksort
    current: current index being checked by quicksort
    """

    new_rect = create_rectangles(A)
    win.fill(BLACK)
    draw_rectangles(new_rect, win, pivot,border,current)
    pygame.display.update()
    time.sleep(.05)


def draw_rectangles(arr,win,pivot=None,border=None,current=None):
    """ Takes in array of rectangles to draw."""
    for j in range(len(arr)):
        if j == pivot:
            pygame.draw.rect(win,RED,arr[j])
        elif j == border:
            pygame.draw.rect(win,YELLOW,arr[j])
        elif j == current:
            pygame.draw.rect(win,GREEN,arr[j])
        else:
            pygame.draw.rect(win,BLUE,arr[j])

#function to create a random array
def create_array():
    """ 
    Creates a list with 10 random integers. 
    These integers are going to be the heights of the rectangles.
    """
    random_array = [random.random() for i in range(50)]
    return random_array


""" Sorting functions. """

def partition(A,low,hi,win,A_r):
    """
    Pushes any values lower than the pivot value to the left of the border.

    Parameters- 
    A: Current array being sorted
    low: lowest index
    hi: highest index
    win: surface object to draw on
    A_r: array of pygame.rect objects

    Returns the border index.
    """
    pivotIndex = get_pivot(A,low,hi)
    pivotValue = A[pivotIndex]
    update_quicksort(A,win,pivotIndex,)
    A[pivotIndex],A[low] = A[low],A[pivotIndex]
    update_quicksort(A,win,pivotIndex,low,)
    time.sleep(.1)
    border = low

    for i in range(low,hi+1):
        update_quicksort(A,win,pivotIndex,border,i,)
        if A[i] < pivotValue:
            border +=1
            update_quicksort(A,win,pivotIndex,border,i,)
            A[i],A[border] = A[border],A[i]
            update_quicksort(A,win,pivotIndex,border,i)

    A[low], A[border] = A[border], A[low]
    update_quicksort(A,win,pivotIndex,border)
    return border

def get_pivot(A,low,hi):
    """ 
    Finds pivot index for current recursive call.

    Parameters-
    A: Current array being sorted.
    low: lowest index value
    hi: highest index value

    Returns the pivot index
    """

    mid = (low+hi) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot=mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot

def quicksort2(A,low,hi,win,A_r):
    """
    Recursively calls quicksort on an array.

    Parameters-
    A: Array of integers to be sorted.
    low: lowest index (default 0)
    hi: highest index (default len(A)-1)
    win: surface object to draw on
    A_r: list of pygame.rect objects.

    Returns a sorted list.
    """
    if low < hi:
        p = partition(A,low,hi,win,A_r)
        quicksort2(A,low,p-1,win,A_r)
        quicksort2(A,p+1,hi,win,A_r)

def quicksort(A,win,A_r):
    quicksort2(A,0,len(A)-1,win,A_r)

def draw_rectangles_insertion(A_r,win,j_index):
    """
    Parameters-
    A_r: List of pygame.rect objects
    win: surface object to draw one
    j_index: key index
    j_index + 1: value being compared
    """
    for r in range(len(A_r)):
        if r == j_index:
            pygame.draw.rect(win,RED,A_r[r])
        elif r == j_index + 1:
            pygame.draw.rect(win,YELLOW,A_r[r])
        else:
            pygame.draw.rect(win,BLUE,A_r[r])

def update_insertion_sort(A,win,j_index):
    new_rect = create_rectangles(A)
    win.fill(BLACK)
    draw_rectangles_insertion(new_rect, win,j_index)
    pygame.display.update()

def insertionSort(arr,win):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
            update_insertion_sort(arr,win,j)
            time.sleep(.1)
            update_insertion_sort(arr,win,j+1)
        update_insertion_sort(arr,win,j)
    return arr





if __name__ == '__main__':
    
    pygame.init()
    sorting = App(HEIGHT, WIDTH, BLACK)
    sorting.start_app()