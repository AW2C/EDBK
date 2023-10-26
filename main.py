# Import Module
from tkinter import *
from buttons import conf, writeBackupDir, backup

# create root window
root = Tk()

# root window title and dimension
root.title("EDBK")
# Set geometry(widthxheight)
root.geometry('380x320')

# Add a heading
heading = Label(root, text="Elite:Dangerous Backup tool", font=("Arial", 20))
heading.pack()

# adding a label to the root window
lbl = Label(root, text = "Manual backup:", font=("Arial", 15))
lbl.pack()

# function to display text when
# button is clicked
def backupButton():
    lbl.configure(text = "Starting backup...")
    root.config(cursor="watch")
    root.update()
    backup()
    lbl.configure(text = "Backup complete!")
    root.config(cursor="")


# button widget with red color text
# inside
btn = Button(root, text = "Go" , fg = "red", command=backupButton)
# set Button grid
btn.pack()

#Backup input  (text box & title)
confDirTitle = Label(root, text="Backup file path:", font=("Arial", 15))
confDirTitle.pack()

confDir = Entry(root)
confDir.insert(0, conf(0))
confDir.pack()

confDirConfirm = Button(root, text = "Confirm" , fg = "red", command=lambda: writeBackupDir(confDir.get()))
confDirConfirm.pack()
# Last backup time
lastBackupTitle = Label(root, text="Last backup:", font=("Arial", 15))
lastBackupTitle.pack()

lastBackup = Label(root, text=conf(1))
lastBackup.pack()




# Execute Tkinter
root.mainloop()