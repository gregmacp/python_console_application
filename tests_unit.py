import unittest
from unittest import mock
from unittest import TestCase
import bbc_tech_challenge_greg_macpherson
from bbc_tech_challenge_greg_macpherson import get, add, update, delete


class test_testy(TestCase):
    @mock.patch('bbc_tech_challenge_greg_macpherson.input', create=True)
    def test_get_gorillaz(self, mocked_input):

        # Fake input to simulate user searching for Gorillaz
        mocked_input.side_effect = ['artist', 'Gorillaz']

        result = get()
        expected_output = [['19fe1358-70b0-419a-b58b-c5da5990a75e', 'Demon Days', 'Gorillaz', '2005'], ['77b0b2a6-1fb3-4f7f-adcd-df2c1be11416', 'Plastic Beach', 'Gorillaz', '2010'], ['b0f4e28a-f41b-4b79-96a4-2776bfb73c7b', 'Demon Days', 'Gorillaz', '2005']]
        self.assertEqual(result, expected_output)

    def test_add(self):
        result = add('Curtis', "Curtis Mayfield", "1970")
        expected_output = ['Curtis', 'Curtis Mayfield', '1970']

        # compare expected_output to the results but remove the uuid as this is uniquely generated at runtime
        self.assertEqual(expected_output, result[1:])

    @mock.patch('bbc_tech_challenge_greg_macpherson.input', create=True)
    def test_get_id(self, mocked_input):
        mocked_input.side_effect = ['id', 'f337fd51-7bf5-44bf-9553-5826162bc83a']
        result = get()
        expected_output = [['f337fd51-7bf5-44bf-9553-5826162bc83a', 'Pink Noise', 'Laura Mvula', '2021']]
        self.assertEqual(result, expected_output)

    @mock.patch('bbc_tech_challenge_greg_macpherson.input', create=True)
    def test_update_melodrama_year(self, mocked_input):
        mocked_input.side_effect = ['album', 'Melodrama', 'year', '2017']
        result = update()
        expected_output = ['c2263b8c-6718-4494-8218-1e739cf04e0a', 'Melodrama', 'Lorde', '2017']
        self.assertEqual(result, expected_output)

    def test_delete(self):
        result = delete('f23844ec-3e6f-4e92-afc2-578c3d1fac7a')
        expected_output = ['f23844ec-3e6f-4e92-afc2-578c3d1fac7a', 'Discovery', 'Daft Punk', '2001']
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()





















# import unittest
# import bbc_tech_challenge_greg_macpherson
# from unittest.mock import patch
# from unittest import TestCase
#
# class TestAll(unittest.TestCase):
#     @patch('bbc_tech_challenge_greg_macpherson.Main', return_value='3')
#     def test_addAlbum(self, input):
#         self.assertEqual(answer(), "hasuih")
#
#
#
#         # assert output == {"",""}
#         # self.assertEqual
#
#
#         # if __name__ == "__main__":
#         #     unittest.main()
#
#
#
#         # set_keyboard_input({"3", "Curtis", "Curtis Mayfield", "1970"})
#         # output = get_display_output()
#
#
#
#
#
#
#
#
#         #
#         # import bbc_tech_challenge_greg_macpherson
#         # from tud_test_base import set_keyboard_input, get_display_output
#         #
#         # class TestAll(unittest.TestCase):
#         #     def test_addAlbum():
#         #         set_keyboard_input({"3", "Curtis", "Curtis Mayfield", "1970"})
#         #
#         #         # result = os.system("bbc_tech_challenge_greg_macpherson.py")
#         #         main()
#         #
#         #         output = get_display_output()
#         #
#         #         assert output == {"",""}
#         #
#         #         self.assertEqual
#         #
#         #     # def test_getAlbum(self):
#         #     #
#         #     # def test_getAll(self):
#         #     #
#         #     # def test_updateYear(self):
#         #     #
#         #     # def test_delete():
#         #
#         # # if __name__ == "__main__":
#         # #
