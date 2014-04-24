from Acquisition import aq_inner
from five import grok
from plone import api

from plone.app.contentlisting.interfaces import IContentListing
from Products.CMFCore.interfaces import IContentish


class LandingPage(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('landingpage-view')


class LandingBoxes(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('landingpage-boxes')

    def update(self):
        self.has_items = len(self.items()) > 0

    def items(self):
        context = aq_inner(self.context)
        catalog = api.portal.get_tool(name="portal_catalog")
        items = catalog(path=dict(query='/'.join(context.getPhysicalPath()),
                                  depth=1),
                        review_state='published',
                        sort_on='getObjPositionInParent',
                        sort_limit=3)[:3]
        results = IContentListing(items)
        return results

    def get_icon_klass(self, idx):
        available = ['fa fa-users fa-2x',
                     'fa fa-expand fa-2x',
                     'fa fa-check fa-2x']
        return available[int(idx)]
