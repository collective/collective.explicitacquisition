from plone.app.testing.layers import FunctionalTesting
from Products.CMFPlone.testing import ProductsCMFPloneLayer


class BaseLayer(ProductsCMFPloneLayer):
    def setUpZope(self, app, configurationContext):  # pylint: disable=W0613
        import collective.explicitacquisition

        self.loadZCML(package=collective.explicitacquisition, name="configure.zcml")


BASE = BaseLayer()


BASE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BASE,), name="collective.explicitacquisition:Functional"
)
