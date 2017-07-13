from pyramid.httpexceptions import HTTPFound


class RedirectionContextManager(object):

    def __init__(self, testCase, expectedLocation):
        self.test = testCase
        self.ecm = testCase.assertRaises(HTTPFound)
        self.expectedLocation = expectedLocation

    def __enter__(self):
        self.ecm_as = self.ecm.__enter__()
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        success = self.ecm.__exit__(exc_type, exc, exc_tb)
        self.exc = exc
        self.test.assertEqual(exc.location, self.expectedLocation)
        return success

    def assertIncludesHeaders(self, expectedHeaders):
        for expectedHeader in expectedHeaders:
            self.test.assertIn(expectedHeader, self.exc.headers)
