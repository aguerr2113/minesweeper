from tkinter import *
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
    bg = 'red',
    width = settings.width,
    height = utilities.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='blue',
    width = utilities.width_prct(25),
    height= utilities.height_prct(75) #subtract full height of window720 from the previous heigth of top_frame to get this height
)
left_frame.place(x=0,y=utilities.height_prct(25))

# Run the Window
root.mainloop()