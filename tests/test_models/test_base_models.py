#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.

Unittest classes:
    instantiation()
    save()
    to_dict()
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModelInitialization(unittest.TestCase):
    """Tests the BaseModel class's initialization."""
    def testDefaultInitialization(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def testCustomInitialization(self):
        customId = "custom"
        customCreatedAt = datetime(2023, 1, 1)
        customUpdatedAt = datetime(2023, 2, 1)
        obj = BaseModel(id=customId, created_at=customCreatedAt,
                        updated_at=customUpdatedAt, customAttribute="test")
        self.assertEqual(obj.id, customId)
        self.assertEqual(obj.created_at, customCreatedAt)
        self.assertEqual(obj.updated_at, customUpdatedAt)
        self.assertEqual(obj.customAttribute, "test")

    def testWithStrDates(self):
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

    # class TestBaseModelStr(unittest.TestCase):
    #     def testStrWithMultipleAttributes(self):

    # class TestBaseModelSaveMethod(unittest.TestCase):
    #     def testSaveUpdatesUpdatedAtMultipleTimes(self):

    #     def testSavePreservesCreatedAtForExistingInstance(self):


if __name__ == '__main__':
    unittest.main()
