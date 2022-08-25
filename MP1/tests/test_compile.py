import unittest, os
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files

# CHANGE FOR NEW ASSIGNMENT
DRIVER_NAME = 'Drawing.java'

class TestCompile(unittest.TestCase):
    @weight(-50.0)
    def test_compile(self):
        """
        Check if all files compile (-50pt if compile error)
        """
        # 0 if no error, 256 if compile error
        status = os.system(f"javac {DRIVER_NAME}")
        
        # we annoyingly have to do this backwards
        # to force negative scoring 
        self.assertEqual(status, 256, 'Files compiled successfully! No deductions.')
        print('Your java files failed to compile (50 POINT DEDUCTION). You can resubmit until the deadline.')
