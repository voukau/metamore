import unittest
import os
import piexif


class TestFunctions(unittest.TestCase):

    def test_01_get(self):
        target = "../samples/Canon_40D.jpg"
        exif_dict = piexif.load(target)
        self.assertIsNotNone(exif_dict)

    def test_02_remove(self):
        target = "../samples/Canon_40D.jpg"
        piexif.remove(target)
        for i in ("0th", "Exif", "GPS", "Interop", "1st"):
            exif_dict = piexif.load(target)
            self.assertEqual(exif_dict[i], {})

    def test_03_transfer(self):
        source = "../samples/Nikon_COOLPIX_P1.jpg"
        target = "../samples/Canon_40D.jpg"
        piexif.transplant(source, target)
        exif_dict = piexif.load(target)
        self.assertIsNotNone(exif_dict)

    def test_04_remove_dir(self):
        target = "../samples"
        directory = os.fsencode(target)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                piexif.remove(target + '/' + filename)
        for _ in os.listdir(directory):
            for i in ("0th", "Exif", "GPS", "Interop", "1st"):
                exif_dict = piexif.load(target + '/' + filename)
                self.assertEqual(exif_dict[i], {})
