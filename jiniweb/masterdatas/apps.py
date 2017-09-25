from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

# MasterData Class
class MasterdatasConfig(AppConfig):
    name = 'masterdatas'    
    verbose_name = _('Masterdata')
    verbose_name_plural = _('Masterdatas')

