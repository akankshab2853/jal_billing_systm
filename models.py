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


class Billinvoice(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=250, blank=True, null=True)
    gst_no = models.CharField(max_length=50, blank=True, null=True)
    consignee_name = models.CharField(max_length=255, blank=True, null=True)
    consignee_state_code = models.CharField(max_length=10, blank=True, null=True)
    consignee_address = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    invoice_date = models.CharField(max_length=50, blank=True, null=True)
    challan_number = models.CharField(max_length=50, blank=True, null=True)
    challan_date = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.CharField(max_length=50, blank=True, null=True)
    veh_no = models.CharField(max_length=50, blank=True, null=True)
    transport_mode = models.CharField(max_length=50, blank=True, null=True)
    due_on = models.CharField(max_length=50, blank=True, null=True)
    time_of_supply = models.CharField(max_length=50, blank=True, null=True)
    payment_terms = models.CharField(max_length=50, blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)
    delivery_terms = models.CharField(max_length=50, blank=True, null=True)
    transport = models.CharField(max_length=50, blank=True, null=True)
    place_of_supply = models.CharField(max_length=100, blank=True, null=True)
    l_r_number = models.CharField(max_length=50, blank=True, null=True)
    l_r_date = models.CharField(max_length=50, blank=True, null=True)
    ref = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billinvoice'


class Billinvoiceitems(models.Model):
    item_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    hsn_code = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit_rate = models.FloatField(blank=True, null=True)
    discount_percentage = models.FloatField(blank=True, null=True)
    gst_rate = models.FloatField(blank=True, null=True)
    cgst = models.FloatField(blank=True, null=True)
    sgst = models.FloatField(blank=True, null=True)
    igst = models.FloatField(blank=True, null=True)
    total_value = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    invoice_number = models.ForeignKey(Billinvoice, models.DO_NOTHING, db_column='invoice_number')

    class Meta:
        managed = False
        db_table = 'billinvoiceitems'


class Defectivestock(models.Model):
    stock = models.CharField(max_length=255, blank=True, null=True)
    stock_type = models.CharField(max_length=100, blank=True, null=True)
    defective_quantity = models.IntegerField()
    reusable_quantity = models.IntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'defectivestock'


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


class Itemstock(models.Model):
    description = models.CharField(unique=True, max_length=255)
    hsn_code = models.CharField(max_length=25, blank=True, null=True)
    stock_type = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.IntegerField()
    supplier = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemstock'


class StaffStaff(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    date_of_joining = models.CharField(max_length=50, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=255, blank=True, null=True)
    aadhar_card_number = models.CharField(unique=True, max_length=12, blank=True, null=True)
    pan_card_number = models.CharField(unique=True, max_length=10, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_staff'


class SupplierSupplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_code = models.CharField(max_length=50, blank=True, null=True)
    supplier_name = models.CharField(max_length=250, blank=True, null=True)
    pan = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    p_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_supplier'


class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50, blank=True, null=True)
    vendor_name = models.CharField(unique=True, max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    pan = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    p_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor'
