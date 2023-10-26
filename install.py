import os
import requests
from tkinter import *


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


#download("http://website.com/Motivation-Letter.docx", dest_folder="mydir")

def install():
    #create main dir
    os.mkdir("C:/Users/"+os.getenv("username")+"/AppData/Local/AW2C")
    os.mkdir("C:/Users/"+os.getenv("username")+"/AppData/Local/AW2C/EDBK")
    download("https://packages.niceygylive.xyz/EDBK/edbk.exe", dest_folder="C:/Users/"+os.getenv("username")+"/AppData/Local/AW2C/EDBK")
    download("https://packages.niceygylive.xyz/EDBK/config.txt", dest_folder="C:/Users/"+os.getenv("username")+"/AppData/Local/AW2C/EDBK")

root = Tk()
root.title("EDBK Installer")
root.geometry('380x320')
heading = Label(root, text="Install?", font=("Arial", 20))
heading.pack()
yesBtn = Button(root, text = "Yes" , fg = "red", command=install)
yesBtn.pack()
noBtn = Button(root, text = "No" , fg = "red", command=root.destroy)
noBtn.pack()
root.mainloop()