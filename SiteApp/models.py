from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer, String, Date, DateTime, and_, or_

db = SQLAlchemy()


class WorkingOrder(db.Model):
    __tablename__ = 'WorkingOrderSite'

    id = Column(Integer, primary_key=True)
    state_car_n = Column(String(23))
    work_shift = Column(Integer)
    work_column = Column(Integer)

    # Driver
    driver_personal_n = Column(String(10))
    driver_full_name = Column(String(44))

    # Conductor
    conductor_personal_n = Column(String(10))
    conductor_full_name = Column(String(44))

    # Route
    route_name = Column(String(25))
    route_date = Column(Date, nullable=False)

    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)

    @staticmethod
    def get_by_personal_n(personal_n, date):
        """
        SQL query like:
        SELECT *
          FROM (Table)
          WHERE route_date = 'date' and (driver_personal_n = 'personal_n' or conductor_personal_n = 'personal_n')
          ORDER BY departure_time
        """

        query = (
            WorkingOrder.query.where(
                and_(
                    WorkingOrder.route_date == date,
                    or_(
                        WorkingOrder.driver_personal_n == personal_n,
                        WorkingOrder.conductor_personal_n == personal_n)))
            .order_by(WorkingOrder.departure_time)
            .all()
        )
        return query

    def __repr__(self):
        """
        Representation method for class WorkingOrder
        :return: WorkingOrder(*values)
        """
        keys = [column.key for column in self.__table__.columns]
        values = [getattr(self, column) for column in keys]
        return "WorkingOrder{}".format(tuple(values))
