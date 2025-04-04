# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Bill(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price_per_piece = models.PositiveIntegerField()
    gst = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bill'


class BillInvoiceInvoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    vendor_name = models.CharField(max_length=255)
    vendor_gstin = models.CharField(max_length=20, blank=True, null=True)
    vendor_state = models.CharField(max_length=50)
    vendor_state_code = models.CharField(max_length=10)
    consignee_name = models.CharField(max_length=255)
    consignee_gstin = models.CharField(max_length=20, blank=True, null=True)
    consignee_state_code = models.CharField(max_length=10)
    po_number = models.CharField(max_length=50)
    po_date = models.DateField()
    transport_mode = models.CharField(max_length=50, blank=True, null=True)
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    cgst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    sgst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    igst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=255)
    bank_branch = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    cgst = models.DecimalField(max_digits=10, decimal_places=2)
    igst = models.DecimalField(max_digits=10, decimal_places=2)
    sgst = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.BigAutoField(primary_key=True)
    date_supply = models.DateField(blank=True, null=True)
    time_supply = models.CharField(max_length=45, blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    challan_number = models.CharField(db_column='Challan_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    challan_number_date = models.DateField(db_column='Challan_number_date', blank=True, null=True)  # Field name made lowercase.
    field_order_number = models.CharField(db_column=' order_number', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_due_date = models.DateField(db_column=' due_date', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    payment_terms = models.CharField(max_length=45, blank=True, null=True)
    place_supply = models.CharField(max_length=150, blank=True, null=True)
    lr_number = models.CharField(max_length=45, blank=True, null=True)
    lr_date = models.DateField(blank=True, null=True)
    lr_time = models.CharField(max_length=45, blank=True, null=True)
    order_number=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'bill_invoice_invoice'


class BillInvoiceInvoiceitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    hsn_code = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bill_invoice_invoiceitem'


class BillInvoiceVendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_invoice_vendor'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InvoiceConsignee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    gstin = models.CharField(unique=True, max_length=20)
    state_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'invoice_consignee'


class InvoiceProduct(models.Model):
    product_name = models.CharField(max_length=255)
    product_hsn_code = models.CharField(max_length=50)
    product_rate = models.DecimalField(max_digits=10, decimal_places=2)
    gst_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'invoice_product'


class InvoiceRecipient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    gstin = models.CharField(unique=True, max_length=20)
    state_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'invoice_recipient'


class InvoiceSupplier(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    address = models.CharField(max_length=45, blank=True, null=True)
    contact = models.CharField(max_length=45, blank=True, null=True)
    gstin = models.CharField(max_length=45, blank=True, null=True)
    invoice_supply_id = models.IntegerField(db_column='invoice_supply id')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'invoice_supplier'


class ItemStock(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hsn_code = models.CharField(unique=True, max_length=45, blank=True, null=True)
    stock_type = models.CharField(max_length=45, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=500, blank=True, null=True)
    sr_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_stock'


class StockStock(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    total_quantity = models.PositiveIntegerField()
    remaining_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_threshold = models.PositiveIntegerField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_stock'


class StockStocktransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.IntegerField()
    timestamp = models.DateTimeField()
    stock = models.ForeignKey(StockStock, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_stocktransaction'
