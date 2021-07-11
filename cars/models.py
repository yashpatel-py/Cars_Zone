from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):
    state_choice = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))


    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=255)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=100)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interier = models.CharField(max_length=255)
    miles = models.IntegerField()
    doors = models.IntegerField(choices=door_choices)
    pissengers = models.IntegerField()
    vin_no = models.CharField(max_length=255)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_if_owners = models.CharField(max_length=255)
    is_features = models.BooleanField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        return self.car_title