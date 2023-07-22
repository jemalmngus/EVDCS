from django.db import models
from django.utils import timezone
import datetime

# Profile model to store user profiles
class Profile(models.Model):
    # Fields for user profile
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    sex = models.CharField(max_length=200, choices=(('male', 'Male'), ('female', 'Female')))
    phone = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Driver model to store driver information
class Driver(models.Model):
    # Fields for driver information
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    driver_license = models.CharField(max_length=200, unique=True)
    license_issued_date = models.DateTimeField('issued date')
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.profile.first_name} - {self.driver_license}"

# Subcity model to store subcity information
class Subcity(models.Model):
    # Fields for subcity information
    subcity_name = models.CharField(max_length=200)
    number_of_stations = models.PositiveIntegerField()
    number_of_machines = models.PositiveIntegerField()
    number_of_routes = models.PositiveIntegerField()
    number_of_vehicles = models.PositiveIntegerField()
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return self.subcity_name

# Vehicle model to store vehicle information
class Vehicle(models.Model):
    # Fields for vehicle information
    vehicle_name = models.CharField(max_length=200)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    plate_no = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200)
    vehicle_size = models.PositiveSmallIntegerField()
    subcity = models.ForeignKey(Subcity, on_delete=models.CASCADE, default=None)
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return self.plate_no

# Penalty model to store penalty information
class Penalty(models.Model):
    # Fields for penalty information
    penalty_type = models.CharField(max_length=200)
    # driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle_plate = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date registered', default=timezone.now)
    trip_no = models.IntegerField(null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.penalty_type

# Station model to store station information
class Station(models.Model):
    # Fields for station information
    station_name = models.CharField(max_length=200)
    number_of_routes = models.PositiveIntegerField()
    # Using PointField for location
    # location = models.PointField()
    subcity = models.ForeignKey(Subcity, on_delete=models.CASCADE)
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return self.station_name

# Machine model to store machine information
class Machine(models.Model):
    # Fields for machine information
    machine_id = models.CharField(max_length=200, unique=True)
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Using PointField for location
    # location = models.PointField()
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return self.machine_id

# MachineData model to store machine data
class MachineData(models.Model):
    # Fields for machine data
    destination = models.CharField(max_length=200)
    machine_id = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return self.destination

# Route model to store route information
class Route(models.Model):
    # Fields for route information
    route_type = models.CharField(max_length=200, default="normal")
    length = models.CharField(max_length=200)
    price = models.FloatField()
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="dest")
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.source.station_name} to {self.destination.station_name}"

# RouteTypes model to store route types information
class RouteTypes(models.Model):
    # Fields for route types information
    name = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'route_types'


# Deployment model to store deployment information
class Deployment(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    rounde = models.PositiveIntegerField()
    vehicle_plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route_type = models.CharField(max_length=20, null=True)
    route_length = models.CharField(max_length=200, null=True)
    route_price = models.FloatField(null=True)
    source_name = models.CharField(max_length=200, null=True)
    destination_name = models.CharField(max_length=200, null=True)
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.vehicle_plate.plate_no} by {self.route_id}"

# WaitingTime model to store waiting time information
class WaitingTime(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    coming_time = models.DateTimeField('coming time')
    going_time = models.DateTimeField('going time')
    reg_date = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return str(self.route_id)

# VehiclesLocation model to store vehicle location information
class VehiclesLocation(models.Model):
    # location = models.PointField()
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reg_date = models.DateTimeField('date registered', default=timezone.now)
    device_id = models.CharField(max_length=200)

    def __str__(self):
        return self.device_id

# AssignVehicle model to store assigned vehicle information
class AssignVehicle(models.Model):
    length = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    vehicles_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    assign_date = models.DateTimeField('date assigned', default=timezone.now)
    status = models.CharField(max_length=200, default="pending")

    def __str__(self):
        return self.status

# Attendance model (Commented as it may be duplicate with the Driver model)
# class Attendance(models.Model):
#     id = models.AutoField(primary_key=True)
#     date = models.DateTimeField()
#     driver = models.CharField(max_length=20)
#     trip_no = models.IntegerField()
#     phone = models.CharField(max_length=200, null=True)
#
#     class Meta:
#         db_table = 'attendance'

