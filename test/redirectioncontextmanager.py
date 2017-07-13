from pyramid.httpexceptions import HTTPFound


class RedirectionContextManager(object):

    def __init__(self, testCase, expectedLocation):
        self.test = testCase
        self.ecm = testCase.assertRaises(HTTPFound)
        self.expectedLocation = expectedLocation

    def __enter__(self):
        self.ecm_as = self.ecm.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        success = self.ecm.__exit__(exc_type, exc_val, exc_tb)
        self.test.assertEqual(exc_val.location, self.expectedLocation)
        return success