from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMCSSPrimitiveValue(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_CSS_UNKNOWN, 0)
        self.assertEqual(WebKit.DOM_CSS_NUMBER, 1)
        self.assertEqual(WebKit.DOM_CSS_PERCENTAGE, 2)
        self.assertEqual(WebKit.DOM_CSS_EMS, 3)
        self.assertEqual(WebKit.DOM_CSS_EXS, 4)
        self.assertEqual(WebKit.DOM_CSS_PX, 5)
        self.assertEqual(WebKit.DOM_CSS_CM, 6)
        self.assertEqual(WebKit.DOM_CSS_MM, 7)
        self.assertEqual(WebKit.DOM_CSWebKit.S_IN, 8)
        self.assertEqual(WebKit.DOM_CSS_PT, 9)
        self.assertEqual(WebKit.DOM_CSS_PC, 10)
        self.assertEqual(WebKit.DOM_CSS_DEG, 11)
        self.assertEqual(WebKit.DOM_CSS_RAD, 12)
        self.assertEqual(WebKit.DOM_CSS_GRAD, 13)
        self.assertEqual(WebKit.DOM_CSS_MS, 14)
        self.assertEqual(WebKit.DOM_CSS_S, 15)
        self.assertEqual(WebKit.DOM_CSS_HZ, 16)
        self.assertEqual(WebKit.DOM_CSS_KHZ, 17)
        self.assertEqual(WebKit.DOM_CSS_DIMENSION, 18)
        self.assertEqual(WebKit.DOM_CSS_STRING, 19)
        self.assertEqual(WebKit.DOM_CSS_URI, 20)
        self.assertEqual(WebKit.DOM_CSS_IDENT, 21)
        self.assertEqual(WebKit.DOM_CSS_ATTR, 22)
        self.assertEqual(WebKit.DOM_CSS_COUNTER, 23)
        self.assertEqual(WebKit.DOM_CSS_RECT, 24)
        self.assertEqual(WebKit.DOM_CSS_RGBCOLOR, 25)
        self.assertEqual(WebKit.DOM_CSS_VW, 26)
        self.assertEqual(WebKit.DOM_CSS_VH, 27)
        self.assertEqual(WebKit.DOM_CSS_VMIN, 28)
        self.assertEqual(WebKit.DOM_CSS_VMAX, 29)
