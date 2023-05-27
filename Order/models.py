from django.db import models


class Transport(models.Model):
    vin_number = models.CharField(unique=True, max_length=17)
    state_car_n = models.CharField(max_length=9, unique=True)
    car_brand = models.CharField(max_length=60)
    is_broken = models.BooleanField(default=False)
    last_maintenance = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.car_brand} : {self.state_car_n} : {self.is_broken}'


class Route(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class EmployeeType(models.Model):
    type_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.type_name


class Employee(models.Model):
    full_name = models.CharField(max_length=44)
    personal_index = models.CharField(max_length=5)
    type = models.ForeignKey(EmployeeType, on_delete=models.SET_DEFAULT, default=None, null=True)

    def get_position(self):
        return self.type.type_name

    def __str__(self):
        return f'{self.full_name} - {self.type.type_name}'


class WorkingOrder(models.Model):
    working_transport = models.ForeignKey(Transport, on_delete=models.SET_DEFAULT, default=None, null=True)

    workers = models.ManyToManyField(Employee, related_name='working_orders', blank=True)

    route = models.ForeignKey(Route, on_delete=models.SET_DEFAULT, default=None, null=True)

    # Working times
    creation_date = models.DateField(auto_now_add=True)
    departure_time = models.DateTimeField(blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def get_transport(self):
        return self.working_transport.state_car_n

    def get_route(self):
        return self.route.name

    def get_order_workers(self):
        workers = self.workers.all()
        return list(workers)



