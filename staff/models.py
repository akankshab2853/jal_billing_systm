from django.db import models
# Staff Management Model
class Staff(models.Model):
    # Personal Details
    full_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    gender_choices = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    gender = models.CharField(
        max_length=10, choices=gender_choices, null=True, blank=True
    )
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    # Job Details
    designation = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    date_of_joining = models.CharField(max_length=50, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Bank Details
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    ifsc_code = models.CharField(max_length=255, null=True, blank=True)
    # Documents
    aadhar_card_number = models.CharField(
        max_length=12, unique=True, null=True, blank=True
    )
    pan_card_number = models.CharField(
        max_length=10, unique=True, null=True, blank=True
    )

    # Upload Photo
    photo = models.ImageField(upload_to="staff_photos/", blank=True, null=True)

    def __str__(self):
        return self.full_name


