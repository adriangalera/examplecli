import os
import re
import unittest


class TestOptions(unittest.TestCase):
    def test_unique_options(self):
        long_opts = self.get_all_options()
        self.assert_no_duplicated_options(long_opts)

    def get_all_options(self):
        options_file_path = os.path.join(os.path.dirname(
            __file__), "../../examplecli/commands/options.py")
        with open(options_file_path, 'r', encoding='utf-8') as options_file:
            options_txt = options_file.read()
            long_opt_regex = r"\"--(.+)\""

            long_opts = []

            long_option_pattern = re.compile(long_opt_regex)
            for match in long_option_pattern.finditer(options_txt):
                long_opts.append(match.group(1))

            return long_opts

    def assert_no_duplicated_options(self, long_opts):
        self.assertEqual(len(long_opts), len(set(long_opts)))
