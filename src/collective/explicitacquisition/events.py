from .interfaces import IPublishableThroughAcquisition
from Products.CMFCore.interfaces import IContentish
from zExceptions import NotFound
from zope.component import adapter
from ZPublisher.interfaces import IPubAfterTraversal

from zope.component.hooks import setSite
from zope.component.hooks import site
from zope.component.interfaces import ISite
from zope.component.interfaces import IPossibleSite

try:
    from plone.i18n.utility import setLanguageBinding
except ImportError:
    # No Plone
    setLanguageBinding = None


@adapter(IPubAfterTraversal)
def avoid_acquired_content(event):
    request = event.request
    parents = request["PARENTS"]
    context = parents[0]
    if IPublishableThroughAcquisition.providedBy(context):
        return
    if IContentish.providedBy(context):
        parents = list(reversed(parents))
        parent_ids = [item.getId() for item in parents]
        acquired = parent_ids != list(context.getPhysicalPath())
        if acquired:
            if setLanguageBinding is not None:
                # See if we need to set a different language for the error page.
                sites = [parent for parent in parents if ISite.providedBy(parent)]
                if len(sites) > 1:
                    # url is something like: localhost:8080/nl/es
                    # where both nl and es are Plone Sites in the Zope root.
                    # Take the top one.
                    site = sites[0]
                    # Use context manager to set the site temporarily.
                    # This is enough for changing the language of the error message.
                    # with site(parent):
                    #     utility.setLanguageBinding(request)
                    # But this still shows items from the Spanish site in the navigation bar.
                    # So call setSite for the rest of the request.
                    # But this still uses Spanish in several other parts of the page,
                    # for example in actions.
                    setSite(site)
                    setLanguageBinding(request)

            raise NotFound(request.URL)
