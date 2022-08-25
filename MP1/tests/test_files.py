import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files

FILES_TO_CHECK = ['Drawing.java']

class TestFiles(unittest.TestCase):
    @weight(0)
    def test_submitted_files(self):
        """Check that all required files are submitted."""
        missing_files = check_submitted_files(FILES_TO_CHECK)
        for path in missing_files:
            print('Missing {0}'.format(path))
        self.assertEqual(len(missing_files), 0, 'Missing some required files, please re-submit!')
        print('All required files submitted!')
