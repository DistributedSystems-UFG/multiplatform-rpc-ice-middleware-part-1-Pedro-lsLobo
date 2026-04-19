import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)
try:
    base = communicator.stringToProxy("SimplePrinter:tcp -h localhost -p 5678")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World!")

    result = printer.printUpperCase("Hello World!")
    print("Upper case result:", result)

    count = printer.countWords("Hello World from Ice middleware!")
    print("Word count:", count)
finally:
    communicator.destroy()
