import unittest

from exception.mydict import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_arrrerror(self):
        d = Dict()

        with self.assertRaises(AttributeError):
            value = d.empty

    def test_abs(self):
        self.assertEqual(abs(-1), 1)

if __name__ == '__main__':
    unittest.main()