# from Products.CMFPlone.testing import PRODUCTS_CMFPLONE_FUNCTIONAL_TESTING

from plone.testing.z2 import Browser
from urllib2 import HTTPError
from zope.interface import alsoProvides
import unittest
from collective.explicitacquisition.testing import BASE_FUNCTIONAL_TESTING


class TestBadAcquisition(unittest.TestCase):

    layer = BASE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']

    def test_not_found_when_acquired_content(self):
        "browsing to acquired content should trigger a 404"
        self.portal.invokeFactory('Document', 'a_page')
        self.assertTrue('a_page' in self.portal.objectIds())
        self.portal.invokeFactory('Folder', 'a_folder')
        self.assertTrue('a_folder' in self.portal.objectIds())
        import transaction
        transaction.commit()
        browser = Browser(self.app)
        browser.open(self.portal.a_page.absolute_url())
        error = None
        try:
            url = self.portal.absolute_url() + '/a_folder/a_page'
            browser.open(url)
        except HTTPError, e:
            error = e
        self.assertTrue(
            error is not None,
            msg='Acquired content should not be published.')
        self.assertEqual(404, error.code)

    def test_not_found_when_template_on_acquired_content(self):
        "browsing to template on acquired content should trigger a 404"
        self.portal.invokeFactory('Document', 'a_page')
        self.assertTrue('a_page' in self.portal.objectIds())
        self.portal.invokeFactory('Folder', 'a_folder')
        self.assertTrue('a_folder' in self.portal.objectIds())
        import transaction
        transaction.commit()
        browser = Browser(self.app)
        browser.open(self.portal.a_page.absolute_url())
        error = None
        try:
            url = self.portal.absolute_url() + '/a_folder/a_page/document_view'
            browser.open(url)
        except HTTPError, e:
            error = e
        self.assertTrue(
            error is not None,
            msg='Acquired content should not be published.')
        self.assertEqual(404, error.code)

    def test_allow_publication_trough_acquisition_explicitely(self):
        self.portal.invokeFactory('Document', 'a_page')
        self.assertTrue('a_page' in self.portal.objectIds())
        a_page = self.portal['a_page']
        try:
            from Products.CMFPlone.interfaces import IPublishableThroughAcquisition
        except ImportError:
            from collective.explicitacquisition.interfaces import IPublishableThroughAcquisition
        alsoProvides(a_page, IPublishableThroughAcquisition)
        self.portal.invokeFactory('Folder', 'a_folder')
        self.assertTrue('a_folder' in self.portal.objectIds())
        import transaction
        transaction.commit()
        browser = Browser(self.app)
        browser.open(self.portal.a_page.absolute_url())
        error = None
        try:
            url = self.portal.absolute_url() + '/a_folder/a_page'
            browser.open(url)
        except HTTPError, e:
            error = e
        self.assertTrue(error is None)
