# Alek Ramirez
# 013927364
# 9-24-18
#
# Lab 0
# Section 13
# Purpose: Solving for the weight on different planets
# Comments:

import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()        
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
