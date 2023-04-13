import pytest
from datetime import date
from SiteApp.models import WorkingOrder


@pytest.mark.usefixtures('db')
class TestWorkingOrderModel:

    def test_model_method_get_be_personal_n(self, order_driver, order_conductor):
        test_query = WorkingOrder.get_by_personal_n('2222', date(2021, 6, 17))
        """
        Testing: Correct method behavior 
        Expected: Query should return orders with same personal number
        even if the driver_n or the conductor_n are not specified in different orders
        Also testing if query is sorting by departure time
        """
        assert test_query[0].driver_personal_n == order_driver.driver_personal_n
        assert test_query[1].conductor_personal_n == order_conductor.conductor_personal_n

        assert test_query[0].departure_time < test_query[1].departure_time
