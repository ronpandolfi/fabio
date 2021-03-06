#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Project: Fable Input Output
#             https://github.com/silx-kit/fabio
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
# Unit tests

builds on stuff from ImageD11.test.testpeaksearch
Jerome Kieffer 04/12/2014
"""
from __future__ import print_function, with_statement, division, absolute_import
import unittest
import sys
import os

if __name__ == '__main__':
    import pkgutil
    __path__ = pkgutil.extend_path([os.path.dirname(__file__)], "fabio.test")
from .utilstest import UtilsTest


logger = UtilsTest.get_logger(__file__)
fabio = sys.modules["fabio"]

from fabio.openimage import openimage
from fabio.edfimage import edfimage
from fabio.marccdimage import marccdimage
from fabio.fit2dmaskimage import fit2dmaskimage
from fabio.OXDimage import OXDimage
from fabio.brukerimage import brukerimage
from fabio.adscimage import adscimage


class TestOpenEdf(unittest.TestCase):
    """openimage opening edf"""

    def checkFile(self, filename):
        """ check we can read EDF image with openimage"""
        obj = openimage(filename)
        obj2 = edfimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testEdf(self):
        fname = "F2K_Seb_Lyso0675.edf.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testEdfGz(self):
        fname = "F2K_Seb_Lyso0675.edf.gz"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)

    def testEdfBz2(self):
        fname = "F2K_Seb_Lyso0675.edf.bz2"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)


class TestOpenMccd(unittest.TestCase):
    """openimage opening mccd"""

    def checkFile(self, filename):
        """ check we can read it"""
        obj = openimage(filename)
        obj2 = marccdimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testMccd(self):
        fname = "somedata_0001.mccd.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testMccdGz(self):
        fname = "somedata_0001.mccd.gz"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)

    def testMccdBz2(self):
        fname = "somedata_0001.mccd.bz2"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)


class TestOpenMask(unittest.TestCase):
    """openimage opening fit2d msk"""

    def checkFile(self, filename):
        """ check we can read Fit2D mask with openimage"""
        obj = openimage(filename)
        obj2 = fit2dmaskimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testMask(self):
        """openimage opening fit2d msk"""
        fname = "face.msk.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testMaskGz(self):
        """openimage opening fit2d msk gzip"""
        fname = "face.msk.gz"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)

    def testMaskBz2(self):
        """openimage opening fit2d msk bzip"""
        fname = "face.msk.bz2"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)


class TestOpenBruker(unittest.TestCase):
    """openimage opening bruker"""

    def checkFile(self, filename):
        """ check we can read it"""
        obj = openimage(filename)
        obj2 = brukerimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testBruker(self):
        """openimage opening bruker"""
        fname = "Cr8F8140k103.0026.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testBrukerGz(self):
        """openimage opening bruker gzip"""
        fname = "Cr8F8140k103.0026.gz"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)

    def testBrukerBz2(self):
        """openimage opening bruker bzip"""
        fname = "Cr8F8140k103.0026.bz2"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)


class TestOpenAdsc(unittest.TestCase):
    """openimage opening adsc"""

    def checkFile(self, filename):
        """ check we can read it"""
        obj = openimage(filename)
        obj2 = adscimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testAdsc(self):
        """openimage opening adsc"""
        fname = "mb_LP_1_001.img.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testAdscGz(self):
        """openimage opening adsc gzip"""
        fname = "mb_LP_1_001.img.gz"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)

    def testAdscBz2(self):
        """openimage opening adsc bzip"""
        fname = "mb_LP_1_001.img.bz2"
        filename = UtilsTest.getimage(fname)
        self.checkFile(filename)


class TestOpenOxd(unittest.TestCase):
    """openimage opening adsc"""

    def checkFile(self, filename):
        """ check we can read OXD images with openimage"""
        obj = openimage(filename)
        obj2 = OXDimage()
        obj2.read(filename)
        self.assertEqual(obj.data[10, 10], obj2.data[10, 10])
        self.assertEqual(type(obj), type(obj2))
        self.assertEqual(abs(obj.data.astype(int) - obj2.data.astype(int)).sum(), 0)

    def testOxd(self):
        """openimage opening adsc"""
        fname = "b191_1_9_1.img.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)

    def testOxdUnc(self):
        """openimage opening adsc"""
        fname = "b191_1_9_1_uncompressed.img.bz2"
        filename = UtilsTest.getimage(fname)[:-4]
        self.checkFile(filename)


def suite():
    loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
    testsuite = unittest.TestSuite()
    testsuite.addTest(loadTests(TestOpenAdsc))
    testsuite.addTest(loadTests(TestOpenBruker))
    testsuite.addTest(loadTests(TestOpenEdf))
    testsuite.addTest(loadTests(TestOpenMask))
    testsuite.addTest(loadTests(TestOpenMccd))
    testsuite.addTest(loadTests(TestOpenOxd))
    return testsuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
