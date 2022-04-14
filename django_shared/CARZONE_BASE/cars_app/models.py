from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

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
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, default='AR', max_length=100)
    city = models.CharField(max_length=100, default='Newyork')
    color = models.CharField(max_length=100, default='white')
    model = models.CharField(max_length=100, default='Sedan')
    year = models.IntegerField(('year'), choices=year_choice, default=2019)
    condition = models.CharField(max_length=100, default='Good')
    price = models.IntegerField(default=4567)
    # # description = models.TextField(max_length=500)
    description = models.TextField(default='Good')
    features = models.CharField(choices=features_choices, max_length=100, default='Airbags')
    body_style = models.CharField(max_length=100, default='Sedan')
    engine = models.CharField(max_length=100, default=1)
    transmission = models.CharField(max_length=100, default='Sedan')
    interrior = models.CharField(max_length=100, default='Sedan')
    miles = models.IntegerField(default=1)
    doors = models.CharField(choices=door_choices , max_length=10, default='2')
    passengers = models.CharField(max_length=100, default='Sedan')
    vin_no = models.CharField(max_length=100, default='Sedan')
    milage = models.CharField(max_length=100, default='Sedan')
    fuel_type = models.CharField(max_length=100, default='Sedan')
    no_of_owners = models.CharField(max_length=100, default='Sedan')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    car_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(default='default.jpg', upload_to = 'photos/%Y/%m/%d/')
    car_photo_2 = models.ImageField(default='default.jpg', upload_to = 'photos/%Y/%m/%d/')
    car_photo_3 = models.ImageField(default='default.jpg', upload_to = 'photos/%Y/%m/%d/')
    car_photo_4 = models.ImageField(default='default.jpg', upload_to = 'photos/%Y/%m/%d/')


    def __str__(self):
        return f'{self.car_title} - {self.model} - {self.year}'
