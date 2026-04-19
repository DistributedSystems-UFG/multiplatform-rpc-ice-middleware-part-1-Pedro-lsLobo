import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def printUpperCase(self, s, current=None):
        result = s.upper()
        print(result)
        return result

    def countWords(self, s, current=None):
        count = len(s.split())
        print(f"Word count of '{s}': {count}")
        return count

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()