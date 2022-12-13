import unittest
from unittest.mock import patch
from examplecli.commands.hello import say_hello


class TestHello(unittest.TestCase):
    @patch("examplecli.commands.hello.info")
    @patch("examplecli.commands.hello.debug")
    def test_hello(self, debug_patch, info_patch):
        say_hello("test")
        debug_patch.assert_called_with("Saying hello to test")
        info_patch.assert_called_with("Hello test")
