from five import grok
from plone import api

from plone.app.contentlisting.interfaces import IContentListing
from Products.CMFCore.interfaces import IContentish

from plone.app.contenttypes.interfaces import INewsItem


class LangingPage(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('langingpage-view')

    def update(self):
        self.has_newsitems = len(self.newsitems()) > 0

    def newsitems(self):
        catalog = api.portal.get_tool(name="portal_catalog")
        items = catalog(object_provides=INewsItem.__identifier__,
                        review_state='published',
                        sort_on='effective',
                        sort_order='reverse',
                        sort_limit=3)[:3]
        results = IContentListing(items)
        return results


class LangingBoxes(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('langingpage-boxes')

    def update(self):
        self.has_newsitems = len(self.newsitems()) > 0

    def newsitems(self):
        catalog = api.portal.get_tool(name="portal_catalog")
        items = catalog(object_provides=INewsItem.__identifier__,
                        review_state='published',
                        sort_on='effective',
                        sort_order='reverse',
                        sort_limit=3)[:3]
        results = IContentListing(items)
        return results
