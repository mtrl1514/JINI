"""
Definition of models.
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Customer(models.Model):    
    SELL = '1'
    BUY = '2'
    BUSINESS_DIV_CHOICES = (
        (SELL, _('SELL')),
        (BUY, _('BUY')),
    )

    customer_id = models.CharField(db_column='CUSTOMER_ID', verbose_name=_('Customer|customer id'), max_length=25, primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', verbose_name=_('customer name'), max_length=100)  # Field name made lowercase.    
    business_div = models.CharField(db_column='BUSINESS_DIV', verbose_name=_('business division'), max_length=1, blank=True,
                                    choices=BUSINESS_DIV_CHOICES,
                                    default=SELL)  # Field name made lowercase.
    business_type = models.CharField(db_column='BUSINESS_TYPE', verbose_name=_('business type'), max_length=50, blank=True)  # Field name made lowercase.
    business_no = models.CharField(db_column='BUSINESS_NO', verbose_name=_('business no'), max_length=50, blank=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', verbose_name=_('owner'), max_length=10, blank=True)  # Field name made lowercase.
    business_item = models.CharField(db_column='BUSINESS_ITEM', verbose_name=_('business item'), max_length=100, blank=True)  # Field name made lowercase.
    business_status = models.CharField(db_column='BUSINESS_STATUS', verbose_name=_('business status'), max_length=100, blank=True)  # Field name made lowercase.
    customer_status = models.CharField(db_column='CUSTOMER_STATUS', verbose_name=_('customer status'), max_length=100, blank=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', verbose_name=_('country'), max_length=100, blank=True)  # Field name made lowercase.
    address_1 = models.CharField(db_column='ADDRESS_1', verbose_name=_('address 1'), max_length=100, blank=True)  # Field name made lowercase.
    address_2 = models.CharField(db_column='ADDRESS_2', verbose_name=_('address 2'), max_length=100, blank=True)  # Field name made lowercase.
    post_no = models.CharField(db_column='POST_NO', verbose_name=_('post no'), max_length=100, blank=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', verbose_name=_('phone no'), max_length=100, blank=True)  # Field name made lowercase.
    fax_no = models.CharField(db_column='FAX_NO', verbose_name=_('fax no'), max_length=100, blank=True)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='MOBILE_NO', verbose_name=_('mobile no'), max_length=100, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', verbose_name=_('email'), max_length=100, blank=True)  # Field name made lowercase.
    user_name_1 = models.CharField(db_column='USER_NAME_1', verbose_name=_('user name 1'), max_length=100, blank=True)  # Field name made lowercase.
    mobile_no_1 = models.CharField(db_column='MOBILE_NO_1', verbose_name=_('mobile no 1'), max_length=100, blank=True)  # Field name made lowercase.
    email_1 = models.CharField(db_column='EMAIL_1', verbose_name=_('email 1'), max_length=100, blank=True)  # Field name made lowercase.
    user_name_2 = models.CharField(db_column='USER_NAME_2', verbose_name=_('user name 2'), max_length=100, blank=True)  # Field name made lowercase.
    mobile_no_2 = models.CharField(db_column='MOBILE_NO_2', verbose_name=_('mobile no 2'), max_length=100, blank=True)  # Field name made lowercase.
    email_2 = models.CharField(db_column='EMAIL_2', verbose_name=_('email 2'), max_length=100, blank=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', verbose_name=_('bank name'), max_length=100, blank=True)  # Field name made lowercase.
    account_no = models.CharField(db_column='ACCOUNT_NO', verbose_name=_('account no'), max_length=100, blank=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='ACCOUNT_NAME', verbose_name=_('account name'), max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_1 = models.CharField(db_column='CUS_CMF_1', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_2 = models.CharField(db_column='CUS_CMF_2', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_3 = models.CharField(db_column='CUS_CMF_3', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_4 = models.CharField(db_column='CUS_CMF_4', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_5 = models.CharField(db_column='CUS_CMF_5', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_6 = models.CharField(db_column='CUS_CMF_6', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_7 = models.CharField(db_column='CUS_CMF_7', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_8 = models.CharField(db_column='CUS_CMF_8', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_9 = models.CharField(db_column='CUS_CMF_9', max_length=100, blank=True)  # Field name made lowercase.
    cus_cmf_10 = models.CharField(db_column='CUS_CMF_10', max_length=100, blank=True)  # Field name made lowercase.
    create_user = models.ForeignKey(User, verbose_name=_('create user'), related_name='create_user', default=' ')  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', verbose_name=_('create time'), auto_now_add=True)  # Field name made lowercase.
    update_user = models.ForeignKey(User, verbose_name=_('update user'), related_name='update_user', default=' ')  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', verbose_name=_('update time'), auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'jbascusmst'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
    def __str__(self):
        return self.customer_name
