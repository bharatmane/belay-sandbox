"""Smoke-test fixture: a deliberately slow test so a run can be interrupted mid-suite."""

import time
import unittest


class SlowFixtureTest(unittest.TestCase):
    def test_waits_sixty_seconds(self):
        start = time.monotonic()
        time.sleep(60)
        self.assertGreaterEqual(time.monotonic() - start, 60)


if __name__ == "__main__":
    unittest.main()
