import sys

from PyObjCTools.TestSupport import TestCase, min_os_level

if sys.maxsize > 2 ** 32:
    import PushKit

    class TestPKPushCredentials(TestCase):
        @min_os_level("10.15")
        def test_classes(self):
            PushKit.PKPushCredentials
