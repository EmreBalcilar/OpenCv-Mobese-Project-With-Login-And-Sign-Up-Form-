import os
import subprocess
import sys
import tkinter as tk

OptionList = [
    "Lütfen Otoyol Seçiniz",
    "Beykoz Otoyol",
    "Üsküdar Otoyol",
    "Kadiköy Otoyol",
    "Ümraniye Otoyol"
]

app = tk.Tk()
app.title("Otoyol Seçiniz")
app.geometry('300x300')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 14))
opt.pack(side="top")

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")


def callback(*args):
    labelTest.configure(text="Seçilen Otoyol {}".format(variable.get()))
    if variable.get() == "Beykoz Otoyol":
        py_filepath = 'C:/Users/Lenovo/PycharmProjects/Deneme\CarDetector\PyhtonOpenCvCarCapture.py'
        # py_filepath = 'plots_test.py'

        args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                   py_filepath,  # argv[0]
                                   os.path.basename(py_filepath))  # argv[1]

        proc = subprocess.run(args)
        print('returncode:', proc.returncode)
        sys.exit(app.exec_())
    if variable.get() == "Üsküdar Otoyol":
        py_filepath = r'C:\Users\Lenovo\PycharmProjects\Deneme\CarDetector\uskudar.py'
        # py_filepath = 'plots_test.py'

        args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                   py_filepath,  # argv[0]
                                   os.path.basename(py_filepath))  # argv[1]

        proccces = subprocess.run(args)
        print('returncode:', proccces.returncode)
    if variable.get() == "Kadiköy Otoyol":
        py_filepath = 'C:/Users/Lenovo/PycharmProjects/Deneme\CarDetector\kadıkoy.py'
        # py_filepath = 'plots_test.py'

        args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                   py_filepath,  # argv[0]
                                   os.path.basename(py_filepath))  # argv[1]

        proc = subprocess.run(args)
        print('returncode:', proc.returncode)
        sys.exit(app.exec_())
    if variable.get() == "Ümraniye Otoyol":
        py_filepath = 'C:/Users/Lenovo/PycharmProjects/Deneme\CarDetector\PyhtonOpenCvCarCapture.py'
        # py_filepath = 'plots_test.py'

        args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                   py_filepath,  # argv[0]
                                   os.path.basename(py_filepath))  # argv[1]

        proc = subprocess.run(args)
        print('returncode:', proc.returncode)
        sys.exit(app.exec_())


variable.trace("w", callback)

app.mainloop()
