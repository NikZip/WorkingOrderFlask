from flask import url_for


class TestSiteApp:

    def test_get_homepage_status_code(self, test_app):
        """
        Testing: if there is reply from homepage
        Expected: code is 200
        """
        response = test_app.get(url_for("site_bp.main"))
        assert response.status_code == 200

    def test_post_if_order_not_exist(self, test_app):
        """
        Testing: if there is success post to homepage and data is not found text
        Expected: code for post is 200 and there is text that data is not found
        """
        response = test_app.post(url_for("site_bp.render_order"), data={
            "personal_n": '2222',
            "date": '2021-09-02'
        })
        assert response.status_code == 200
        assert bytes("Для этого табельного номера нет разнарядки на 2021-09-02", 'utf-8') in response.data

    def test_get_if_order_exist(self, test_app, order_driver):
        """
        Testing: if there is success post to homepage and data is found
        Expected: code for post is 200 and there is created table with data
        """
        response = test_app.post(url_for("site_bp.render_order"), data={
            "personal_n": '2222',
            "date": '2021-06-17'
        })
        assert response.status_code == 200
        assert bytes('<table class="table table-bordered table-hover', 'utf-8') in response.data
        assert bytes('2222' and '2021-06-17' and 'Макаров В.П', 'utf-8') in response.data
