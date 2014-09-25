from .interfaces import IPublishableThroughAcquisition
from Products.CMFCore.interfaces import IContentish
from ZPublisher.interfaces import IPubAfterTraversal
from zExceptions import NotFound
from zope.component import adapter


@adapter(IPubAfterTraversal)
def avoid_acquired_content(event):
    request = event.request
    parents = request['PARENTS']
    context = parents[0]
    if IPublishableThroughAcquisition.providedBy(context):
        return
    if IContentish.providedBy(context):
        parent_ids = [item.getId() for item in parents]
        parent_ids.reverse()
        acquired = parent_ids != list(context.getPhysicalPath())
        if acquired:
            raise NotFound(request.URL)
