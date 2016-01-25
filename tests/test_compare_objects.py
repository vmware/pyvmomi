import tests
from pyVmomi import vim
from operator import eq as equals


class CompareTests(tests.VCRTestBase):

    def test_compare_objects(self):
        compare_str = "Test"
        compare_obj = vim.Datastore
        self.assertFalse(equals(compare_str, compare_obj))
        self.assertTrue(equals(compare_obj, compare_obj))
