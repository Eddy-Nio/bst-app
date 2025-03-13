import unittest
from unittest.mock import patch, MagicMock
import io
import sys
from main import main

@patch('main.Fore.CYAN', '')
@patch('main.Style.RESET_ALL', '')
class TestMain(unittest.TestCase):
    @patch('builtins.input')
    @patch('main.clear_screen')
    @patch('main.print_menu')
    def test_quit_option(self, mock_menu, mock_clear, mock_input):
        """Test quit option exits program"""
        mock_input.return_value = 'q'
        main()
        mock_clear.assert_called_once()
        mock_menu.assert_called_once()

    @patch('builtins.input')
    @patch('main.clear_screen')
    @patch('main.print_menu')
    @patch('main.BinarySearchTree')
    def test_sort_numbers_workflow(self, mock_bst, mock_menu, mock_clear, mock_input):
        """Test number sorting workflow"""
        # Mock sequence of inputs including "Press Enter" prompts
        mock_input.side_effect = ['1', '5 3 7 1 9', '', 'q']
        
        # Mock BST operations
        mock_bst_instance = MagicMock()
        mock_bst_instance.reverse_in_order.return_value = [9,7,5,3,1]
        mock_bst.return_value = mock_bst_instance

        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Numbers in descending order", output)
        self.assertIn("9 7 5 3 1", output)

    @patch('builtins.input')
    @patch('main.clear_screen')
    @patch('main.print_menu')
    @patch('main.WordFrequencyBST')
    def test_word_frequency_workflow(self, mock_word_bst, mock_menu, mock_clear, mock_input):
        """Test word frequency workflow"""
        # Mock inputs including "Press Enter" prompts
        mock_input.side_effect = ['2', 'hello world hello python', '', 'q']
        
        # Mock WordFrequencyBST operations
        mock_bst_instance = MagicMock()
        mock_bst_instance.in_order_traversal.return_value = [
            ("hello", 2),
            ("world", 1),
            ("python", 1)
        ]
        mock_word_bst.return_value = mock_bst_instance

        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Word frequencies", output)
        self.assertIn("hello", output)
        self.assertIn("2", output)

    @patch('builtins.input')
    @patch('main.clear_screen')
    @patch('main.print_menu')
    def test_invalid_option(self, mock_menu, mock_clear, mock_input):
        """Test invalid menu option handling"""
        mock_input.side_effect = ['x', '', 'q']
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Invalid option", output)

    @patch('builtins.input')
    def test_keyboard_interrupt(self, mock_input):
        """Test KeyboardInterrupt handling"""
        mock_input.side_effect = KeyboardInterrupt()
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Program terminated by user", output)

    @patch('main.clear_screen')
    @patch('main.print_menu')
    @patch('builtins.input')
    def test_general_exception(self, mock_input, mock_menu, mock_clear):
        """Test general exception handling"""
        def input_sequence(*args):
            # First call raises exception
            if mock_input.call_count == 1:
                raise Exception("Test error")
            # Subsequent calls return 'q' to exit
            return 'q'
        
        mock_input.side_effect = input_sequence
        
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            main()
        except Exception as e:
            self.fail(f"Exception not properly handled: {e}")
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("An unexpected error occurred", output)
        self.assertIn("Test error", output)

if __name__ == '__main__':
    unittest.main()