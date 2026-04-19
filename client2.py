import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 3.227.138.6 -p 5678")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 3.227.138.6 -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)

rep = printer1.printUpperCase("hello from printer1 in upper case!")
print(rep)
rep = printer2.printUpperCase("hello from printer2 in upper case!")
print(rep)

count = printer1.countWords("How many words does this sentence have")
print("Printer1 word count:", count)
count = printer2.countWords("And what about this one here")
print("Printer2 word count:", count)

communicator.waitForShutdown()
