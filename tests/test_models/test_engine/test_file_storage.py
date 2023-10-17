import unittest
from unittest.mock import patch
import json
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class in your_module.

    using the mock module to automate file operations and count calls
    without actually doing any file (write)s or (read)s on the disk.
    """

    def setUp(self):
        """Set up a new instance of FileStorage for each test."""

        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        return super().setUp()

    def tearDown(self):
        """Clean up after each test by resetting the __objects dictionary."""

        FileStorage._FileStorage__objects = {}
        return super().tearDown()

    def test_defaults(self):
        """Test if default values are set correctly."""

        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'Amenity': Amenity, 'City': City, 'Review': Review,
                   'Place': Place}

        self.assertEqual(self.file_path, 'file.json')
        self.assertEqual(self.storage.classes, classes)

    def test_types(self):
        """Test if the types of attributes are correct."""

        self.assertEqual(type(self.storage), FileStorage)
        self.assertEqual(type(self.file_path), str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """Test 'all' method to ensure it returns the __objects dictionary."""

        self.assertIsInstance(self.storage.all(), dict)

        objects = FileStorage._FileStorage__objects
        self.assertEqual(self.storage.all(), objects)
        new_obj = User()
        self.assertEqual(self.storage.all(), objects)

    def test_new(self):
        """Test 'new' method to add a new object to __objects dictionary."""

        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    @patch('builtins.open', create=True)
    def test_save(self, mock_open):
        """Test the 'save' method to ensure proper file writing."""

        with patch('json.dump') as mock_json_dump:
            self.storage.save()

        mock_open.assert_called_once_with(self.file_path, 'w')
        mock_json_dump.assert_called_once()

    @patch('builtins.open', create=True)
    def test_reload(self, mock_open):
        """Test the 'reload' method to ensure proper file reading."""

        with patch('json.load') as mock_json_load:
            self.storage.reload()

        mock_open.assert_called_once_with(self.file_path, 'r')
        mock_json_load.assert_called_once()

    @patch('builtins.open', create=True)
    def test_save_reload_integration(self, mock_open):
        """
        Test the integration of 'save' and 'reload' methods.
        and ensuring they're working with no excessive calls
        for any file operations.
        """

        with patch('json.dump') as mock_json_dump:
            self.storage.save()
        mock_open.assert_called_once_with(self.file_path, 'w')

        mock_json_dump.reset_mock()
        mock_open.reset_mock()

        with patch('json.load') as mock_json_load:
            self.storage.reload()
        mock_open.assert_called_once_with(self.file_path, 'r')
        mock_json_dump.assert_not_called()
