import unittest
from io import StringIO
import sys

class TestFindMaxNumber(unittest.TestCase):

    def test_find_max(self):
        # Redirect sys.stdout to capture the program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Import and call the main function from the FindMaxNumber module
        from FindMaxNumber import main
        main()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Expected output
        expected_output = 78

        # Convert captured output to an integer and check if it matches the expected result
        self.assertEqual(expected_output, int(captured_output.getvalue().strip()))

    def test_find_max_negative_numbers(self):
        # Test with negative numbers
        captured_output = StringIO()
        sys.stdout = captured_output
        
        from FindMaxNumber import main
        main()

        sys.stdout = sys.__stdout__

        expected_output = -2
        self.assertEqual(expected_output, int(captured_output.getvalue().strip()))

    def test_find_max_single_element(self):
        # Test with a single element list
        captured_output = StringIO()
        sys.stdout = captured_output
        
        from FindMaxNumber import main
        main()

        sys.stdout = sys.__stdout__

        expected_output = 42
        self.assertEqual(expected_output, int(captured_output.getvalue().strip()))

if __name__ == '__main__':
    unittest.main()
