from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit  # noqa: F401
import objc


class TestWKScriptMessageHandler(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testProtocols10_10(self):
        p = objc.protocolNamed("WKScriptMessageHandler")
        self.assertIsInstance(p, objc.formal_protocol)
