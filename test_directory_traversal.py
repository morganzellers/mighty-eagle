import unittest
import tempfile
import os
import shutil
from datetime import datetime
from main import DirectoryTraversal

class TestDirectoryTraversal(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.sub_dir = os.path.join(self.test_dir, "subdir")
        os.mkdir(self.sub_dir)

        # Create a few test files with specific modification times
        self.file1 = os.path.join(self.test_dir, "test_file1.txt")
        self.file2 = os.path.join(self.sub_dir, "test_file2.txt")
        self.file3 = os.path.join(self.sub_dir, "test_file3.txt")

        # Set specific modification times for the test files
        self.modification_time1 = datetime(2023, 1, 1)
        self.modification_time2 = datetime(2023, 2, 1)
        self.modification_time3 = datetime(2023, 3, 1)

        self.create_test_files()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_test_files(self):
        with open(self.file1, "w") as f1, open(self.file2, "w") as f2, open(self.file3, "w") as f3:
            f1.write("File 1 content")
            f2.write("File 2 content")
            f3.write("File 3 content")

        # Set specific modification times for the test files
        os.utime(self.file1, (self.modification_time1.timestamp(), self.modification_time1.timestamp()))
        os.utime(self.file2, (self.modification_time2.timestamp(), self.modification_time2.timestamp()))
        os.utime(self.file3, (self.modification_time3.timestamp(), self.modification_time3.timestamp()))

    def test_list_files_created_dates(self):
        dt = DirectoryTraversal(self.test_dir)

        # Expected file paths and corresponding modification times
        expected_files_and_dates = {
            self.file1: self.modification_time1,
            self.file2: self.modification_time2,
            self.file3: self.modification_time3,
        }

        result_files_and_dates = {}
        for file, date in dt.list_files_created_dates():
            result_files_and_dates[file] = date

        self.assertEqual(expected_files_and_dates, result_files_and_dates)

    def test_get_file_creation_date(self):
        dt = DirectoryTraversal(self.test_dir)

        # Check the modification time of a specific file
        file1_modification_time = dt.get_file_creation_date(self.file1)
        self.assertEqual(file1_modification_time, self.modification_time1)

        # Check a file in a subdirectory
        file2_modification_time = dt.get_file_creation_date(self.file2)
        self.assertEqual(file2_modification_time, self.modification_time2)

        # Check a file in a subdirectory
        file3_modification_time = dt.get_file_creation_date(self.file3)
        self.assertEqual(file3_modification_time, self.modification_time3)

if __name__ == '__main__':
    unittest.main()
