# abouts/urls.py
from django.conf.urls import url
from .views import RulesetsView
from .views import RulesetsWCAGView
from .views import RulesetsRuleView
from .views import RulesetsRuleWCAGView
from .views import RulesetView
from .views import RulesetWCAGView
from .views import RulesetRuleView
from .views import RulesetRuleWCAGView

urlpatterns = [
    url(r'^$',      RulesetsView.as_view(),     name='rulesets'),
    url(r'wcag/$', RulesetsWCAGView.as_view(), name='rulesets_wcag'),
    url(r'^(?P<rule_num>[\d-]+)/$',      RulesetsRuleView.as_view(),     name='rulesets_rule'),
    url(r'^wcag/(?P<rule_num>[\d-]+)/$', RulesetsRuleWCAGView.as_view(), name='rulesets_rule_wcag'),
    url(r'^ruleset/(?P<slug>\w+)/$',      RulesetView.as_view(),     name='ruleset'),
    url(r'^ruleset/wcag/(?P<slug>\w+)/$', RulesetWCAGView.as_view(), name='ruleset_wcag'),
    url(r'^ruleset/(?P<slug>\w+)/(?P<rule_num>[\d-]+)/$',      RulesetRuleView.as_view(),     name='ruleset_rule'),
    url(r'^ruleset/wcag/(?P<slug>\w+)/(?P<rule_num>[\d-]+)/$', RulesetRuleWCAGView.as_view(), name='ruleset_rule_wcag'),
]
