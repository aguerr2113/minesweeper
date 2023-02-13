from tkinter import *
from cell import Cell
import settings
import utilities



root = Tk()
# Over ride the settings of the window
# makes background a color
root.configure(bg='black')
root.geometry(f'{settings.width}x{settings.height}')
root.title('Totally not Minesweeper')


# doesent allow for the window to be resized
root.resizable(False,False)


top_frame = Frame(
    root,
    bg = 'black',
    width = settings.width,
    height = utilities.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='black',
    width = utilities.width_prct(25),
    height= utilities.height_prct(75) #subtract full height of window720 from the previous heigth of top_frame to get this height
)
left_frame.place(x=0,y=utilities.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black',
    width = utilities.width_prct(75),
    height = utilities.height_prct(75)
)

center_frame.place(
    x = utilities.width_prct(25),
    y = utilities.height_prct(25)
)


for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y
        )

# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column = 0,
#     row = 0
# )
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column = 0,
#     row = 1
# )



# Run the Window
root.mainloop()