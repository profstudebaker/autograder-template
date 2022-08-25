import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        test_runner = JSONTestRunner(visibility='visible', stdout_visibility = "visible", stream=f)
        test_runner.json_data["scoring_type"] = "negative"
        test_runner.run(suite)
