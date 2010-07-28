# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('',
    (r'^$', 'subscription.views.index', {}, 'seriesly-index'),
    (r'^faq/$', direct_to_template, {"template": "faq.html"}, "seriesly-faq"),
    (r'^imprint/$', redirect_to, {'url': '/about/#impressum'}),
    (r'^terms/$', direct_to_template, {"template": "terms.html"}, "seriesly-terms"),
    (r'^about/$', direct_to_template, {"template": "about.html"}, "seriesly-about"),
    (r'^privacy/$', direct_to_template, {"template": "privacy.html"}, "seriesly-privacy"),
    (r'^missing/$', direct_to_template, {"template": "missing.html"}, "seriesly-missing"),
    (r'^webhook-xml/$', direct_to_template, {"template": "webhook_xml.html"}, "seriesly-webhook-xml"),
    (r'^subscribe/$', 'subscription.views.subscribe', {}, 'seriesly-subscribe'),
    (r'^shows/', include('series.urls')),
    (r'^releases/', include('releases.urls')),
    (r'^subscription/', include('subscription.urls')),
    (r'^statistics/', include('statistics.urls')),
    (r'^_ah/xmpp/message/chat/$', 'subscription.views.incoming_xmpp', {}, 'seriesly-incoming_xmpp'),
    (r'^public/([A-Za-z0-9]{32})/$', 'subscription.views.show_public', {}, 'seriesly-subscription-show_public'),
    (r'^public/([A-Za-z0-9]{32})/guide/$', 'subscription.views.guide_public', {}, 'seriesly-subscription-guide_public'),
    (r'^public/([A-Za-z0-9]{32})/rss/$', 'subscription.views.feed_rss_public', {}, 'seriesly-subscription-rss_public'),
    (r'^public/([A-Za-z0-9]{32})/feed/$', 'subscription.views.feed_atom_public', {}, 'seriesly-subscription-atom_public'),
    (r'^public/([A-Za-z0-9]{32})/calendar/$', 'subscription.views.calendar_public', {}, 'seriesly-subscription-calendar_public'),

    (r'^([A-Za-z0-9]{32})/$', 'subscription.views.show', {}, 'seriesly-subscription-show'),
    (r'^([A-Za-z0-9]{32})/confirm/([a-f0-9]{40})/$', 'subscription.views.confirm_mail', {}, 'seriesly-subscription-confirm_mail'),
    (r'^([A-Za-z0-9]{32})/edit/$', 'subscription.views.edit', {}, 'seriesly-subscription-edit'),
    (r'^([A-Za-z0-9]{32})/guide/$', 'subscription.views.guide', {}, 'seriesly-subscription-guide'),
    (r'^([A-Za-z0-9]{32})/rss/$', 'subscription.views.feed_rss', {}, 'seriesly-subscription-rss'),
    (r'^([A-Za-z0-9]{32})/feed/$', 'subscription.views.feed_atom', {}, 'seriesly-subscription-atom'),
    (r'^([A-Za-z0-9]{32})/calendar/$', 'subscription.views.calendar', {}, 'seriesly-subscription-calendar'),

)
