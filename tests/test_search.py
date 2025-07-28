import unittest


class DummyArgs:
    def __init__(self, exclude=None, repo_pattern=None,
                 ignore_comments=False, comment_marker='#', context_lines=0):
        self.exclude = exclude or []
        self.repo_pattern = repo_pattern or ''
        self.ignore_comments = ignore_comments
        self.comment_marker = comment_marker
        self.context_lines = context_lines


class TestBeagleSearchExclude(unittest.TestCase):
    def setUp(self):
        # Simulate results as returned by hound.query
        self.results = {
            'repo1': {
                'Matches': [
                    {'Filename': 'src/main.py',
                     'Matches': [{'LineNumber': 1,
                                  'Line': 'foo', 'Before': [], 'After': []}]},
                    {'Filename': 'src/test_utils.py',
                     'Matches': [{'LineNumber': 2,
                                  'Line': 'bar', 'Before': [], 'After': []}]},
                    {'Filename': 'docs/readme.py',
                     'Matches': [{'LineNumber': 3, 'Line': 'baz',
                                  'Before': [], 'After': []}]},
                ]
            }
        }

    def test_exclude_pattern(self):
        from beagle.search import Search
        search = Search(app=None, app_args=None)
        args = DummyArgs(exclude=['*test*', '*doc*'])
        found = list(search._flatten_results(self.results, args))
        # Only src/main.py should remain
        self.assertEqual(len(found), 1)
        self.assertIn('src/main.py', found[0])

    def test_no_exclude(self):
        from beagle.search import Search
        search = Search(app=None, app_args=None)
        args = DummyArgs(exclude=[])
        found = list(search._flatten_results(self.results, args))
        self.assertEqual(len(found), 3)
        self.assertIn('src/main.py', found[0])
        self.assertIn('src/test_utils.py', found[1])
        self.assertIn('docs/readme.py', found[2])

    def test_partial_exclude(self):
        from beagle.search import Search
        search = Search(app=None, app_args=None)
        args = DummyArgs(exclude=['*test*'])
        found = list(search._flatten_results(self.results, args))
        self.assertEqual(len(found), 2)
        self.assertIn('src/main.py', found[0])
        self.assertIn('docs/readme.py', found[1])


if __name__ == '__main__':
    unittest.main()
