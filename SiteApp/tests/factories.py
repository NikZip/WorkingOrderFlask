from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence
from datetime import datetime, date
from SiteApp import db
from SiteApp.models import WorkingOrder


class BaseFactory(SQLAlchemyModelFactory):
    """Base Factory"""

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class OrderMainFactory(BaseFactory):
    class Meta:
        model = WorkingOrder

    id = Sequence(lambda n: n)
    state_car_n = '286НА/18'
    work_shift = 1
    work_column = 4
    driver_personal_n = ''
    driver_full_name = 'Макаров В.П'
    conductor_personal_n = ''
    conductor_full_name = 'Козлова Н.В'
    route_name = '28/13'
    route_date = date(2021, 6, 17)
    departure_time = None
    arrival_time = None


class OrderDriverFactory(OrderMainFactory):
    """Factory for testing if it will find it without conductor_personal_n"""
    driver_personal_n = '2222'
    departure_time = datetime(2021, 6, 17, 5, 10)
    arrival_time = datetime(2021, 6, 17, 20, 10)


class OrderConductorFactory(OrderMainFactory):
    """Factory for testing if it will find it without vtab"""
    conductor_personal_n = '2222'
    departure_time = datetime(2021, 6, 17, 10, 10)
    arrival_time = datetime(2021, 6, 17, 15, 10)
