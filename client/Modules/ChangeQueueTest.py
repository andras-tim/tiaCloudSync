#!/usr/bin/env python3

import unittest
from ChangeQueue import ChangeQueue

class TestChangeQueue(unittest.TestCase):

    def test_createAnInstance(self):
        ChangeQueue()

    def test_newQueueNotContainedItems(self):
        self.assertFalse(ChangeQueue().hasChange())

    def test_pushOneItem(self):
        queue = ChangeQueue()
        queue.pushChange("xxx", "relative path")
        self.assertTrue(queue.hasChange())

    def test_pushMoreItems(self):
        queue = ChangeQueue()
        queue.pushChange("x", "path1")
        queue.pushChange("y", "path2")
        self.assertTrue(queue.hasChange())

    def test_pushChangeFunctionIsChainable(self):
        queue = ChangeQueue()
        self.assertEqual(queue, queue.pushChange("xxx", "relative path"))

    def test_getOneItemWhatWasPushedPreviously(self):
        queue = ChangeQueue()
        queue.pushChange("xxx", "relative path")

        item = queue.popChange()
        self.assertEqual(item.type_of_change, "xxx")
        self.assertEqual(item.relative_path, "relative path")

    def test_fifoOrderOfPoppedItemsWhatWasPushedPreviously(self):
        queue = ChangeQueue()
        queue.pushChange("x", "path1")
        queue.pushChange("y", "path2")

        item = queue.popChange()
        self.assertEqual(item.type_of_change, "x")
        self.assertEqual(item.relative_path, "path1")
        item = queue.popChange()
        self.assertEqual(item.type_of_change, "y")
        self.assertEqual(item.relative_path, "path2")


if __name__ == '__main__':
    unittest.main()
