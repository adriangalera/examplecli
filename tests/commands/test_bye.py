import unittest
from unittest.mock import patch
from examplecli.commands.bye import say_bye


class TestBye(unittest.TestCase):
    @patch("examplecli.commands.bye.info")
    @patch("examplecli.commands.bye.debug")
    def test_bye(self, debug_patch, info_patch):
        say_bye("test")
        debug_patch.assert_called_with("Saying bye to test")
        info_patch.assert_called_with("Bye test")
