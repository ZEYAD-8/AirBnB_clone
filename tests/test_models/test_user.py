#!/usr/bin/python3
"""
Testing the User model by unittest
"""

import unittest
from models.user import User
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_class_attributes(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_default_initialization(self):
        """
        Test the default initialization of the User class.
        """
        user = User()
        
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_types(self):
        """
        tests with random attributes
        """
        user1 =  User(name="test")
        user2 = User(name="test", value=18)
        self.assertIsInstance(user1.name, str)
        self.assertIsInstance(user2.name, str)
        self.assertIsInstance(user2.value, int)

    def test_attributes_assignment(self):
        """
        Test the assignment of attributes in the User class.
        """
        user = User(email="test@example.com", password="sectest", first_name="harry", last_name="potter")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "sectest")
        self.assertEqual(user.first_name, "harry")
        self.assertEqual(user.last_name, "potter")

    def test_2unique_ids(self):
        """
        Test 2 different unique ids
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        """
        Test different created_at
        """
        user1 = User()
        sleep(0.04)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        """
        Test different updated_at
        """
        user1 = User()
        sleep(0.04)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def testNone_kwargs(self):
            with self.assertRaises(TypeError):
                User(id=None, created_at=None, updated_at=None)


class Test_to_dict(unittest.TestCase):
    def test_to_dict_method(self):
        """
        Test the to_dict method in the User class.
        """
        user = User(email="test@example.com", password="secpass", first_name="John", last_name="Doe")
        user_dict = user.to_dict()

        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('id', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('__class__', user_dict)

    def test_attribute_types(self):
        """
        Test the data types of attributes 
        in the dictionary returned by to_dict().
        """
        user_attr = User(email="test@example.com", password="secpass", first_name="harry", last_name="potter")
        result_dict = user_attr.to_dict()

        self.assertIsInstance(result_dict['created_at'], str)
        self.assertIsInstance(result_dict['updated_at'], str)
        self.assertIsInstance(result_dict['id'], str)
        self.assertIsInstance(result_dict['email'], str)
        self.assertIsInstance(result_dict['password'], str)
        self.assertIsInstance(result_dict['first_name'], str)
        self.assertIsInstance(result_dict['last_name'], str)
        
    def test_to_dict_datetime_format(self):
        """
        Test that the datetime values in the 
        dictionary follow the expected string format.
        """
        user = User(email="test@example.com", password="secpass", first_name="harry", last_name="potter")
        result_dict = user.to_dict()

        self.assertRegex(result_dict['created_at'], r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')
        self.assertRegex(result_dict['updated_at'], r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')


class Test_user_save(unittest.TestCase):
    """
    Unittests for testing the save method of the User class.
    """

    def test_save_multiple_times(self):
        """
        Test that calling save multiple times updates 'updated_at' each time.
        """
        user = User()
        sleep(0.04)
        first_updated_at = user.updated_at
        user.save()

        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.04)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

if __name__ == '__main__':
    unittest.main()
