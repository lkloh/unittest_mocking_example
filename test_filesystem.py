

from filesystem import rm_file
from unittest.mock import patch, MagicMock
import unittest

def enclosing_func(any_function, dummy_variable):
	print(str(dummy_variable))
	any_function()

class TestRm(unittest.TestCase):
    
    @patch('filesystem.os')
    def test_rm(self, mock_os):
        rm_file("/any_path")

        # test that rm_file called os.remove with the right parameters
        mock_os.remove.assert_called_with("/any_path")

    @patch(enclosing_func(test_rm_nested, 'dummy'))
    @patch('filesystem.os')
    def test_rm_nested(self, mock_os):
        rm_file("/any_path")

        # test that rm_file called os.remove with the right parameters
        mock_os.remove.assert_called_with("/any_path")

if __name__=='__main__':
	unittest.main()


