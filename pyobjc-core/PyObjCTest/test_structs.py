"""
XXX: Add tests that check that the type actually works as expected:

* Use struct value as method argument
* Return struct value from a method

Add tests for nested structs as well (that is assert that NSRect.location is
an NSPoint, but using our own types)
"""
import sys
import warnings

import objc
from PyObjCTest.fnd import NSObject
from PyObjCTest.structs import OC_StructTest
from PyObjCTools.TestSupport import TestCase, main, pyobjc_options

if sys.maxsize > 2 ** 32:
    PTR_SIZE = 8
else:
    PTR_SIZE = 4


class TestStructs(TestCase):
    def testCreateExplicit(self):
        tp = objc.createStructType(
            "FooStruct", b"{_FooStruct=ffff}", ["a", "b", "c", "d"]
        )
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_FooStruct=ffff}")

        self.assertEqual(tp._fields, ("a", "b", "c", "d"))

        o = tp()
        self.assertHasAttr(o, "a")
        self.assertHasAttr(o, "b")
        self.assertHasAttr(o, "c")
        self.assertHasAttr(o, "d")

        with warnings.catch_warnings(record=True):
            self.assertEqual(len(o), 4)

        self.assertHasAttr(objc.ivar, "FooStruct")
        v = objc.ivar.FooStruct()
        self.assertIsInstance(v, objc.ivar)
        self.assertEqual(v.__typestr__, tp.__typestr__)

        self.assertIsSubclass(tp, objc._structwrapper)

    def testNamedTupleAPI(self):
        Point = objc.createStructType("OCPoint", b"{_OCPoint=dd}", ["x", "y"])
        Line = objc.createStructType(
            "OCLine",
            b"{_OCLine={_OCPoint=dd}{_OCPoint=dd}}d",
            ["start", "stop", "width"],
        )

        self.assertEqual(Point._fields, ("x", "y"))
        self.assertEqual(Line._fields, ("start", "stop", "width"))

        p = Point(3, 4)
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)

        self.assertEqual(p._asdict(), {"x": 3.0, "y": 4.0})

        p2 = p._replace(y=5)
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)
        self.assertEqual(p2.x, 3.0)
        self.assertEqual(p2.y, 5)

        ln = Line(Point(1, 2), Point(8, 9), 7)
        self.assertEqual(ln.start.x, 1.0)
        self.assertEqual(ln.start.y, 2.0)
        self.assertEqual(ln.stop.x, 8.0)
        self.assertEqual(ln.stop.y, 9.0)
        self.assertEqual(ln.width, 7.0)

        self.assertEqual(
            ln._asdict(), {"start": Point(1, 2), "stop": Point(8, 9), "width": 7.0}
        )

        ln2 = ln._replace(stop=Point(3, 4), width=0.5)
        self.assertEqual(ln.start.x, 1.0)
        self.assertEqual(ln.start.y, 2.0)
        self.assertEqual(ln.stop.x, 8.0)
        self.assertEqual(ln.stop.y, 9.0)
        self.assertEqual(ln.width, 7.0)

        self.assertEqual(ln2.start.x, 1.0)
        self.assertEqual(ln2.start.y, 2.0)
        self.assertEqual(ln2.stop.x, 3.0)
        self.assertEqual(ln2.stop.y, 4.0)
        self.assertEqual(ln2.width, 0.5)

    def testCreateImplicit(self):
        tp = objc.createStructType("BarStruct", b'{_BarStruct="e"f"f"f"g"f"h"f}', None)
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_BarStruct=ffff}")

        o = tp()
        self.assertHasAttr(o, "e")
        self.assertHasAttr(o, "f")
        self.assertHasAttr(o, "g")
        self.assertHasAttr(o, "h")

        self.assertEqual(tp._fields, ("e", "f", "g", "h"))

        self.assertRaises(
            ValueError, objc.createStructType, "Foo2", b'{_Foo=f"a"}', None
        )
        self.assertRaises(
            ValueError, objc.createStructType, "Foo3", b'{_Foo="a"f', None
        )
        self.assertRaises(
            ValueError, objc.createStructType, "Foo4", b'^{_Foo="a"f}', None
        )

    def testPointerFields(self):
        # Note: the created type won't be all that useful unless the pointer
        # happens to be something that PyObjC knows how to deal with, this is
        # more a check to see if createStructType knows how to cope with
        # non-trivial types.
        tp = objc.createStructType(
            "XBarStruct", b'{_XBarStruct="e"^f"f"^f"g"^@"h"f}', None
        )
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_XBarStruct=^f^f^@f}")

        o = tp()
        self.assertHasAttr(o, "e")
        self.assertHasAttr(o, "f")
        self.assertHasAttr(o, "g")
        self.assertHasAttr(o, "h")

    def testEmbeddedFields(self):
        with pyobjc_options(structs_indexable=False):
            tp = objc.createStructType(
                "BarStruct", b'{FooStruct="first"i"second"i}', None
            )

            v = OC_StructTest.createWithFirst_andSecond_(1, 2)
            self.assertIsInstance(v, tp)

            x = OC_StructTest.sumFields_(v)
            self.assertEqual(x, v.first + v.second)
            self.assertEqual(v.first, 1)
            self.assertEqual(v.second, 2)

            self.assertHasAttr(objc.ivar, "BarStruct")
            v = objc.ivar.BarStruct()
            self.assertEqual(v.__typestr__, b"{FooStruct=ii}")

    def testStructCallback(self):
        """
        Regression test for an issue reported on the PyObjC mailinglist.
        """
        with pyobjc_options(structs_indexable=False):
            tp = objc.createStructType(
                "FooStruct", b'{FooStruct="first"i"second"i}', None
            )

            StructArrayDelegate = objc.informal_protocol(
                "StructArrayDelegate",
                [
                    objc.selector(
                        None, b"arrayOf4Structs:", signature=b"@@:[4{FooStruct=ii}]"
                    )
                ],
            )
            self.assertIsInstance(StructArrayDelegate, objc.informal_protocol)

            class OC_PyStruct(NSObject):
                def arrayOf4Structs_(self, value):
                    return value

            self.assertEqual(
                OC_PyStruct.arrayOf4Structs_.signature,
                b"@@:[4{FooStruct=" + objc._C_INT + objc._C_INT + b"}]",
            )

            o = OC_PyStruct.alloc().init()
            v = OC_StructTest.callArrayOf4Structs_(o)
            self.assertEqual(len(v), 4)
            for i in range(3):
                self.assertIsInstance(v[i], tp)

            self.assertEqual(v[0], tp(1, 2))
            self.assertEqual(v[1], tp(3, 4))
            self.assertEqual(v[2], tp(5, 6))
            self.assertEqual(v[3], tp(7, 8))

    def testStructSize(self):
        tp0 = objc.createStructType("FooStruct", b"{FooStruct=}", None)
        tp1 = objc.createStructType("FooStruct", b'{FooStruct="first"i}', None)
        tp2 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        self.assertEqual(sys.getsizeof(tp0()) + 1 * PTR_SIZE, sys.getsizeof(tp1()))
        self.assertEqual(sys.getsizeof(tp0()) + 2 * PTR_SIZE, sys.getsizeof(tp2()))

    def testStructNotWritable(self):
        tp0 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        with pyobjc_options(structs_indexable=False, structs_writable=False):
            v = tp0(1, 2)

            with self.assertRaises(TypeError):
                v.first = 42

        with pyobjc_options(structs_indexable=True, structs_writable=False):
            v = tp0(1, 2)

            with self.assertRaises(TypeError):
                v.first = 42

            with self.assertRaises(TypeError):
                v[0] = 42

    def testStructNotSequence(self):
        tp0 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        with pyobjc_options(structs_indexable=False, structs_writable=True):
            v = tp0(1, 2)

            with self.assertRaises(TypeError):
                v[0]

            with self.assertRaises(TypeError):
                v[0] = 4

            with self.assertRaises(TypeError):
                len(v)

            self.assertFalse(v == (1, 2))

            self.assertTrue(tp0(1, 2) == tp0(1, 2))
            self.assertFalse(tp0(1, 2) == tp0(1, 3))

            self.assertTrue(tp0(1, 2) != tp0(1, 3))
            self.assertFalse(tp0(1, 2) != tp0(1, 2))

            self.assertTrue(tp0(1, 2) <= tp0(1, 2))
            self.assertTrue(tp0(1, 2) <= tp0(1, 3))
            self.assertFalse(tp0(1, 2) <= tp0(0, 2))
            self.assertFalse(tp0(1, 2) <= tp0(1, 1))

            self.assertTrue(tp0(1, 2) >= tp0(1, 2))
            self.assertTrue(tp0(1, 2) >= tp0(1, 1))
            self.assertFalse(tp0(1, 2) >= tp0(2, 2))
            self.assertFalse(tp0(1, 2) >= tp0(1, 3))

            self.assertTrue(tp0(1, 2) < tp0(1, 3))
            self.assertFalse(tp0(1, 2) < tp0(1, 2))
            self.assertFalse(tp0(1, 2) < tp0(1, 1))

            self.assertTrue(tp0(1, 2) > tp0(1, 1))
            self.assertFalse(tp0(1, 2) > tp0(1, 2))
            self.assertFalse(tp0(1, 2) > tp0(1, 3))

    def testStructConstruction(self):
        with pyobjc_options(structs_indexable=False):
            tp0 = objc.createStructType(
                "FooStruct", b'{FooStruct="first"i"second"i}', None
            )

            v = tp0()
            self.assertEqual(v.first, 0)
            self.assertEqual(v.second, 0)

            v = tp0(2, 3)
            self.assertEqual(v.first, 2)
            self.assertEqual(v.second, 3)

            self.assertRaises(TypeError, tp0, 4, 5, 6)


if __name__ == "__main__":
    main()
