import unittest
import ledCheck.light as l

class TestLights(unittest.TestCase):
    
    def testCountSample(self):
        print("Count Sample:")
        print(10)
        myTest = l.Light(10)
        self.assertEqual(myTest.count(),0)
        count = 0
        for i in myTest.grid:
            for j in i:
                count+=1
        self.assertEqual(count, 10**2)
        
    def testCountGeneral(self):
        print("Count General:")
        for n in range(0, 1000, 21):
            print(n)
            myTest = l.Light(n)
            self.assertEqual(myTest.count(),0)
            count = 0
            for i in myTest.grid:
                for j in i:
                    count+=1
            self.assertEqual(count, n**2)
    
    def testOnOffSwitchSample(self):
        print("On/Off/Switch Sample:")
        print(10)
        myTest = l.Light(10)
        self.assertEqual(myTest.count(), 0)
        myTest.on(0,0,9,9)
        self.assertEqual(myTest.count(), 100)
        myTest.off(1,1,8,8)
        self.assertEqual(myTest.count(), 36)
        myTest.switch(0,0,9,9)
        self.assertEqual(myTest.count(), 64)
    
    def testOnOffSwitchGeneral(self):
        print("On/Off/Switch General:")
        for i in range(3, 1000, 41):
            print(i)
            myTest = l.Light(i)
            self.assertEqual(myTest.count(), 0)
            myTest.on(0,0,i-1,i-1)
            self.assertEqual(myTest.count(), i**2)
            myTest.off(1,1,i-2,i-2)
            self.assertEqual(myTest.count(), i*4 - 4)
            myTest.switch(0,0,i-1,i-1)
            self.assertEqual(myTest.count(), i**2 - i*4 + 4)
        
    def testOnOffSwitchExceptions(self):
        print("On/Off/Switch Exceptions:")
        print(0)
        myTest = l.Light(0)
        self.assertEqual(myTest.count(), 0)
        myTest.on(0,0,0,0)
        self.assertEqual(myTest.count(), 0)
        myTest.off(0,0,0,0)
        self.assertEqual(myTest.count(), 0)
        myTest.switch(0,0,0,0)
        self.assertEqual(myTest.count(), 0)
        
        print(1)
        myTest = l.Light(1)
        self.assertEqual(myTest.count(), 0)
        myTest.on(0,0,0,0)
        self.assertEqual(myTest.count(), 1)
        myTest.off(0,0,0,0)
        self.assertEqual(myTest.count(), 0)
        myTest.switch(0,0,0,0)
        self.assertEqual(myTest.count(), 1)
        
        print(2)
        myTest = l.Light(2)
        self.assertEqual(myTest.count(), 0)
        myTest.on(0,0,1,1)
        self.assertEqual(myTest.count(), 4)
        myTest.off(0,0,1,0)
        self.assertEqual(myTest.count(), 2)
        myTest.switch(0,0,1,1)
        self.assertEqual(myTest.count(), 2)
        
    def testOnOffSwitchReverse(self):
        print("On/Off/Switch Reverse")
        print(10, "normal")
        myTest = l.Light(10)
        myTest.on(2,2,6,6)
        self.assertEqual(myTest.count(), 25)
        myTest.off(3,3,5,5)
        self.assertEqual(myTest.count(), 16)
        myTest.switch(2,2,6,6)
        self.assertEqual(myTest.count(), 9)
        print(10, "reverse")
        myTest = l.Light(10)
        myTest.on(6,6,2,2)
        self.assertEqual(myTest.count(), 25)
        myTest.off(5,5,3,3)
        self.assertEqual(myTest.count(), 16)
        myTest.switch(6,6,2,2)
        self.assertEqual(myTest.count(), 9)
        print(10, "semi-reverse")
        myTest = l.Light(10)
        myTest.on(6,2,2,6)
        self.assertEqual(myTest.count(), 25)
        myTest.off(5,3,3,5)
        self.assertEqual(myTest.count(), 16)
        myTest.switch(2,6,6,2)
        self.assertEqual(myTest.count(), 9)


if __name__ == '__main__':
    unittest.main()