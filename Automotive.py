#Mark Hall
#Final project Joe's Automotive
#11/15/21

#imports
import tkinter
import tkinter.messagebox

#define the class
class JoeAuto:
    def __init__(self):
        
        #Create main window
        self.mainWindow = tkinter.Tk()
        #Title for the main window
        self.mainWindow.title('Joe\'s')

        #Frame for check buttons and frame for display charges and quit buttons
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)
        
        #Variables associated with check buttons
        self.checkButton1 = tkinter.IntVar()
        self.checkButton2 = tkinter.IntVar()
        self.checkButton3 = tkinter.IntVar()
        self.checkButton4 = tkinter.IntVar()
        self.checkButton5 = tkinter.IntVar()
        self.checkButton6 = tkinter.IntVar()
        self.checkButton7 = tkinter.IntVar()
        
        #Initialize the check buttons to zero
        self.checkButton1.set(0)
        self.checkButton2.set(0)
        self.checkButton3.set(0)
        self.checkButton4.set(0)
        self.checkButton5.set(0)
        self.checkButton6.set(0)
        self.checkButton7.set(0)
        
        #Create all of the check buttons
        self.oilChangeCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Oil Change - $30.00', variable = self.checkButton1)
        self.lubeJobCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Lube Job - $20.00', variable = self.checkButton2)
        self.radiatorFlushCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Radiator Flush - $100.00', variable = self.checkButton3)
        self.transmissionFlushCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Transmission Flush - $100.00', variable = self.checkButton4)
        self.inspectionCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Inspection - $35.00', variable = self.checkButton5)
        self.mufflerReplacementCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Muffler Replacement - $200.00', variable = self.checkButton6)
        self.tireRotationCheckButton = tkinter.Checkbutton(self.topFrame, \
                    text = 'Tire Rotation - $20.00', variable = self.checkButton7)

        #Pack the check buttons
        self.oilChangeCheckButton.pack()
        self.lubeJobCheckButton.pack()
        self.radiatorFlushCheckButton.pack()
        self.transmissionFlushCheckButton.pack()
        self.inspectionCheckButton.pack()
        self.mufflerReplacementCheckButton.pack()
        self.tireRotationCheckButton.pack()

        #Create display charges button and quit button
        self.displayChargesButton = tkinter.Button(self.bottomFrame, \
                      text = 'Display Charges', command = self.calculateTotal)
        self.quitButton = tkinter.Button(self.bottomFrame, \
                      text = 'Quit', command = self.mainWindow.destroy)

        #pack buttons
        self.displayChargesButton.pack(side = 'left')
        self.quitButton.pack(side = 'left')

        #pack frames
        self.topFrame.pack()
        self.bottomFrame.pack()
        
        #main loop
        tkinter.mainloop()

    #Calculate the total when display charges button clicked 
    def calculateTotal(self):

        #Establish the charges for each service type and assign to variable
        oilChange = 30.00
        lubeJob = 20.00
        radiatorFlush = 40.00
        transmissionFlush = 100.00
        inspection = 35.00
        mufflerReplacement = 200.00
        tireRotation = 20.00

        #Initialize the total
        total = 0

        #Test to see which buttons are checked. If checked, add the price
        #to the total variable.
        if self.checkButton1.get() == 1:
            total += oilChange
        if self.checkButton2.get() == 1:
            total += lubeJob
        if self.checkButton3.get() == 1:
            total += radiatorFlush
        if self.checkButton4.get() == 1:
            total += transmissionFlush
        if self.checkButton5.get() == 1:
            total += inspection
        if self.checkButton6.get() == 1:
            total += mufflerReplacement
        if self.checkButton7.get() == 1:
            total += tireRotation

        #Create a formatted message to display the toal charges
        self.message = 'Total Charges = ${:,.2f}'.format(total)
        #Display total in dialog box
        tkinter.messagebox.showinfo('Total Charges', self.message)


#Create an instance of the class
joe = JoeAuto()


