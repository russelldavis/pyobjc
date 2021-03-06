import sys

from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKWebViewConfiguration(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.suppressesIncrementalRendering
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setSuppressesIncrementalRendering_, 0
        )

    @onlyOn64Bit
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            WebKit.WKWebViewConfiguration.allowsAirPlayForMediaPlayback
        )
        self.assertArgIsBOOL(
            WebKit.WKWebViewConfiguration.setAllowsAirPlayForMediaPlayback_, 0
        )

    def testConstants(self):
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicyContent, 0)
        self.assertEqual(WebKit.WKUserInterfaceDirectionPolicySystem, 1)

        self.assertEqual(WebKit.WKAudiovisualMediaTypeNone, 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeAudio, 1 << 0)
        self.assertEqual(WebKit.WKAudiovisualMediaTypeVideo, 1 << 1)

        if sys.maxsize > 2 ** 32:
            # The entire enum is only available in 64-bit code.
            self.assertEqual(WebKit.WKAudiovisualMediaTypeAll, sys.maxsize * 2 + 1)
