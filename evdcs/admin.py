from django.contrib import admin
from .models import Profile, Driver, Subcity, Vehicle, Penalty, Station, Machine, MachineData, Route, RouteTypes, Deployment, WaitingTime, VehiclesLocation, AssignVehicle

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'phone')
    list_filter = ('sex', 'reg_date')

# Custom admin for the Vehicle model
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'driver', 'plate_no', 'subcity')
    search_fields = ('plate_no', 'driver__profile__first_name', 'driver__profile__last_name')

# Custom admin for the Penalty model
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('penalty_type', 'vehicle_plate', 'reg_date')
    list_filter = ('penalty_type', 'reg_date')
    date_hierarchy = 'reg_date'
    search_fields = ('vehicle_plate', 'penalty_type')

# Register your models with the custom admins
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Penalty, PenaltyAdmin)
admin.site.register(Driver)
admin.site.register(Subcity)
admin.site.register(Station)
admin.site.register(Machine)
admin.site.register(MachineData)
admin.site.register(Route)
admin.site.register(RouteTypes)
admin.site.register(Deployment)
admin.site.register(WaitingTime)
admin.site.register(VehiclesLocation)
admin.site.register(AssignVehicle)
