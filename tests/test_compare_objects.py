import tests
from pyVmomi import vim
from operator import eq as equals


class CompareTests(tests.VCRTestBase):

    def test_compare_objects(self):
        compare_str = "Test"
        compare_obj = vim.Datastore
        self.assertFalse(equals(compare_str, compare_obj))
        self.assertTrue(equals(compare_obj, compare_obj))

    def test_compare_objects_unicode(self):
        compare_str = u"Test"
        compare_obj = vim.Datastore
        self.assertFalse(equals(compare_str, compare_obj))
        self.assertTrue(equals(compare_obj, compare_obj))

    def test_compare_objects_bytes(self):
        compare_str = b"Test"
        compare_obj = vim.Datastore
        self.assertFalse(equals(compare_str, compare_obj))
        self.assertTrue(equals(compare_obj, compare_obj))
