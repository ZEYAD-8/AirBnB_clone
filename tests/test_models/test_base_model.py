#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.

Unittest classes:
    instantiation()
    save()
    to_dict()
"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class Test_BaseModel_Initialization(unittest.TestCase):
    """
    Evaluates the initialization
    behavior of the BaseModel class.
    """

    def test_default_initialization(self):
        """
        Verifies that a BaseModel instance, created without
        explicitly setting attributes,
        initializes with default values
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_with_str_dates(self):
        """
        Verifies the BaseModel class's handling of
        string-formatted dates when setting
        created_at and updated_at attributes.
        """
        Date = {"created_at": "2017-09-28T21:05:54.119427",
                "updated_at": "2017-09-28T21:05:54.119427"
                }
        format = "%Y-%m-%dT%H:%M:%S.%f"
        obj = BaseModel(**Date)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertEqual(obj.created_at, datetime.strptime(Date["created_at"],
                                                           format))
        self.assertEqual(obj.updated_at, datetime.strptime(Date["updated_at"],
                                                           format))


class Test_BaseModel_Str(unittest.TestCase):
    """
    Validates the __str__ method of the BaseModel class
    for accurate string representation.
    """

    def test_empty_instance(self):
        """
        Checks the behavior of the BaseModel class when an instance is
        created without explicit attribute values.
        """
        base_model = BaseModel()
        string_repr = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model),  string_repr)
        self.assertIsInstance(string_repr, str)
        self.assertIn('BaseModel', string_repr)
        self.assertIn(base_model.id, string_repr)
        self.assertIn(str(base_model.__dict__), string_repr)

    def test_instance_with_attributes(self):
        """
        Examines the behavior of the BaseModel class when an instance
        is created with specific attribute values.
        """
        attr = BaseModel(id=2, name='Example', value=42)
        expected_output = f"[BaseModel] (2) {attr.__dict__}"
        self.assertEqual(str(attr), expected_output)

    def test_instance_with_special_characters(self):
        """
        Validates the behavior of the BaseModel class when an
        instance includes attributes with special characters.
        """
        special_char = BaseModel(id=4, special_chars='!@#$%^&*')
        expected_output = f"[BaseModel] (4) {special_char.__dict__}"
        self.assertEqual(str(special_char), expected_output)


class Test_Save_Method(unittest.TestCase):
    """
    Evaluates the behavior of the save method
    in the BaseModel class.
    """

    def test_save(self):
        """
        Verifies the functionality
        of the save method in the BaseModel class.
        """
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        with patch('models.storage.save') as mock_save:
            base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)
        mock_save.assert_called_once()

    def test_save_multiple_times(self):
        """
        Validates the behavior of the save method in the BaseModel class
        when invoked multiple times on the same instance.
        """
        model = BaseModel()
        original_updated_at = model.updated_at
        with patch('models.storage.save') as mock_save:
            model.save()
            self.assertNotEqual(original_updated_at, model.updated_at)
            mock_save.assert_called_once()
            mock_save.reset_mock()
            updated_at_after_first_save = model.updated_at
            model.save()
            self.assertNotEqual(updated_at_after_first_save, model.updated_at)
            mock_save.assert_called_once()


class Test_to_dict_Method(unittest.TestCase):
    """
    Evaluates the behavior of the
    to_dict method in the BaseModel class.
    """

    def test_to_dict_structure(self):
        """
        Verifies the structure of the dictionary returned
        by the to_dict method in the BaseModel class.
        """
        obj = BaseModel()
        result_dict = obj.to_dict()
        self.assertIsInstance(result_dict, dict)
        self.assertIn('id', result_dict)
        self.assertIn('created_at', result_dict)
        self.assertIn('updated_at', result_dict)
        self.assertIn('__class__', result_dict)

    def test_to_dict_attribute_types(self):
        """
        Checks the data types of attributes in the dictionary
        returned by the to_dict method in the BaseModel class.
        """
        obj = BaseModel()
        result_dict = obj.to_dict()
        self.assertIsInstance(result_dict['id'], str)
        self.assertIsInstance(result_dict['created_at'], str)
        self.assertIsInstance(result_dict['updated_at'], str)
        self.assertIsInstance(result_dict['__class__'], str)

    def test_to_dict_datetime_format(self):
        """
        Verifies that the datetime values in the
        dictionary returned by the to_dict method in the
        BaseModel class follow the expected string format.
        """
        result_dict = BaseModel().to_dict()
        created_at_iso = datetime.strptime(result_dict['created_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f").isoformat()
        updated_at_iso = datetime.strptime(result_dict['updated_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f").isoformat()
        self.assertEqual(result_dict['created_at'], created_at_iso)
        self.assertEqual(result_dict['updated_at'], updated_at_iso)

    def test_to_dict_class_name(self):
        """
        Checks that the dictionary returned
        by the to_dict method in the BaseModel
        class includes the correct class name.
        """
        result_dict = BaseModel().to_dict()
        self.assertEqual(result_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
