from .interfaces import IPublishableThroughAcquisition
from Products.CMFCore.interfaces import IContentish
from zExceptions import NotFound
from zope.component import adapter
from zope.component.interfaces import ISite
from ZPublisher.interfaces import IPubAfterTraversal


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
            sites = [parent for parent in parents if ISite.providedBy(parent)]
            if len(sites) > 1:
                # url is something like: localhost:8080/site1/site2
                # where both site1 and site2 are Plone Sites in the Zope root.
                # Take the top one.
                site = sites[0]
                # Redirect to the site root.
                # Most likely status codes:
                # 301: 'Moved Permanently'
                # 307: 'Temporary Redirect'
                # 308: 'Permanent Redirect'
                # Use a temporary one for now, as we are experimenting.
                request.response.redirect(site.absolute_url(), lock=True, status=307)
                return ""

            raise NotFound(request.URL)
