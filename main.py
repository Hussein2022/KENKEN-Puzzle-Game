from tkinter import *


############################################################
############### window initialization ######################
window = Tk()

icon = PhotoImage(file='img.png')
window.iconphoto(True, icon)

window.geometry("500x500") #size of the window
window.title("KENKEN Puzzle Game")

###############################################################
################## Puzzel Construction ########################
def KENKEN_Construct(start_boarder_x, start_boarder_y, end_boarder_x, end_boarder_y, kenken_order):
    canvas = Canvas(window, height=500, width=500)
    canvas.create_rectangle(start_boarder_x, start_boarder_y, end_boarder_x, end_boarder_y)
    canvas.create_rectangle(
    (start_boarder_x + (end_boarder_x - start_boarder_x)/kenken_order), start_boarder_y,
    start_boarder_x + 2*(end_boarder_x - start_boarder_x) / kenken_order, end_boarder_y)

    canvas.create_rectangle(    start_boarder_x, start_boarder_y+(end_boarder_y-start_boarder_y)/kenken_order,
    end_boarder_x, start_boarder_y+2*(end_boarder_y-start_boarder_y)/kenken_order)
    canvas.pack()

KENKEN_Construct(100, 100, 400, 400, 3)






window.mainloop() #placewindow on computer screen and listen for eventss