import unittest

import piexif


class TestFunctions(unittest.TestCase):

    def test_get(self):
        target = "../samples/Canon_40D.jpg"
        exif_dict = piexif.load(target)
        self.assertIsNotNone(exif_dict)

    def test_remove(self):
        target = "../samples/Canon_40D.jpg"
        piexif.remove(target)
        for i in ("0th", "Exif", "GPS", "Interop", "1st"):
            exif_dict = piexif.load(target)
            self.assertEqual(exif_dict[i], {})

    def test_transfer(self):
        source = "../samples/Nikon_COOLPIX_P1.jpg"
        target = "../samples/Canon_40D.jpg"
        piexif.transplant(source, target)
        exif_dict = piexif.load(target)
        self.assertIsNotNone(exif_dict)