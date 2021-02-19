import tkinter
import statistics

numList = []
x = 0

def addNum(event=None):
    global x
    x = x + 1
    numList.append(int(numEntry.get()))
    numLB.insert(x, numEntry.get())
    print(str(x) + " " + str(int(numEntry.get())))
    numEntry.delete(0, 'end')

def showMean():
    meanRes = statistics.mean(numList)
    resultLabel.config(text = "Result: " + str(meanRes))

def showMedian():
    medianRes = statistics.median(numList)
    resultLabel.config(text = "Result: " + str(medianRes))

def showMode():
    modeRes = statistics.mode(numList)
    resultLabel.config(text = "Result: " + str(modeRes))

def clearList(event=None):
    numList.clear()
    numLB.delete(0, 'end')
    resultLabel.config(text = "Result: -")

def delNum(event=None):
    numLB.delete(numLB.curselection())


mw = Tk()
mw.title("Mean Median Mode")


enLabel = Label(mw, text = "Enter number").grid(row = 0, column = 0, sticky = W)
numEntry = Entry(mw)
numEntry.grid(row = 0, column = 1, sticky = "we")
numEntry.focus()

enButton = Button(mw, text = "Add to list", width = 10, command=addNum)
enButton.grid(row = 0, column = 2, sticky = E)
mw.bind('<Return>', addNum)
mw.bind('<Delete>', delNum)

ClearBtn = Button(mw, text = "Clear", command = clearList)
ClearBtn.grid(row=0, column = 3)

meanBtn = Button(mw, text = "Mean", command=showMean)
meanBtn.grid(row = 1, column = 0)

medianBtn = Button(mw, text = "Median", command=showMedian)
medianBtn.grid(row = 1, column = 1)

modeBtn = Button(mw, text = "Mode", command=showMode)
modeBtn.grid(row = 1, column = 2)

resultLabel = Label(mw, text = "Result: -", font = (None, 10))
resultLabel.grid(row = 2, column = 0, columnspan = 3, sticky = "nwes", pady = 7)

listLabel = Label(mw, text = "Added numbers").grid(row = 0, column = 4)
numLB = Listbox(mw)
numLB.grid(row = 1, rowspan = 3, column = 4)

mw.mainloop()