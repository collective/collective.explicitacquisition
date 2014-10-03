from plone.app.testing.layers import FunctionalTesting
from Products.CMFPlone.testing import ProductsCMFPloneLayer


class BaseLayer(ProductsCMFPloneLayer):
    def setUpZope(self, app, configurationContext):  # pylint: disable=W0613
        import plone.app.imaging
        self.loadZCML(package=plone.app.imaging, name='configure.zcml')
        import collective.explicitacquisition
        self.loadZCML(package=collective.explicitacquisition, name='configure.zcml')
        # self.loadZCML(package=collective.explicitacquisition, name='testing.zcml')


BASE = BaseLayer()


BASE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BASE, ),
    name="collective.explicitacquisition:Functional"
)
