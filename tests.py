# !python3
import unittest
import app
import xmlrunner


class TestCase(unittest.TestCase):
    def test_import_param_test(self):
        print('running unit test sort test...')
        test_string = '[z,y,x,w,v,u]'
        returned_str = app.import_params(test_string)
        returned_str = returned_str.replace(' ', '')
        # ensure order of elements changed
        self.assertNotEqual(test_string, returned_str)
        # ensure reverse order sort
        self.assertEqual(test_string[1:12][::-1], returned_str[1:12])
        # ensure the same char count
        self.assertEqual(len(test_string), len(returned_str))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))


