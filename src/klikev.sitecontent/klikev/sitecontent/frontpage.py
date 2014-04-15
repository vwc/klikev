from five import grok
from plone import api

from plone.app.contentlisting.interfaces import IContentListing
from plone.app.layout.navigation.interfaces import INavigationRoot


class FrontpageView(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('frontpage-view')

    def update(self):
        self.has_newsitems = len(self.newsitems()) > 0

    def newsitems(self):
        catalog = api.portal.get_tool(name="portal_catalog")
        items = catalog(portal_type='plone.app.contenttypes.content.NewsItem',
                        review_state='published',
                        sort_on='effective',
                        sort_order='reverse')
        results = IContentListing(items)
        return results
