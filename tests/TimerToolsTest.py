from microtools import TimerTools
import unittest
import time

class TimerToolsTest(unittest.TestCase):

    def test_interval(self):
        global diff
        startTime = TimerTools.getMicroTime()
        diff = 0
        def intervalFunc():
            global diff
            endTime = TimerTools.getMicroTime()
            diff = endTime - startTime
            print ("called in:" + str(diff))

        TimerTools.setTimeout(intervalFunc, 3)
        time.sleep(4)
        self.assertTrue(diff >= 3000 and diff < 4000, "Timer must wait for 3 seconds, but was:" + str(diff) )

    def test_intervalStop(self):
        global called
        called = False
        def intervalFunc():
            global called
            called = True
            print ("called in:" + str(diff))
        timer = TimerTools.setTimeout(intervalFunc, 0.5)
        timer.stop()
        time.sleep(1)
        self.assertFalse(called, "Function must be stopped")
    def test_delay(self):
        global called
        called = 0
        def intervalFunc():
            global called
            called += 1
        timer = TimerTools.setDelay(intervalFunc, 0.5)
        time.sleep(2)
        self.assertTrue(called == 3 or called == 4 )
        timer.stop()
        time.sleep(1)
        self.assertTrue(called == 3 or called == 4)





if __name__ == "__main__":
    unittest.main()



