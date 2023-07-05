import tests

from pyVim import connect
from pyVmomi import vim


class SoapAdapterTests(tests.VCRTestBase):
    def test_invoke_method_login_session_exception(self):
        def login_fail(*args, **kwargs):
            raise vim_session.SESSION_EXCEPTIONS[0]()

        stub = connect.SoapStubAdapter()
        vim_session = connect.VimSessionOrientedStub(stub, login_fail)
        self.assertRaises(vim.fault.NotAuthenticated, vim_session.InvokeAccessor, "mo", "info")
