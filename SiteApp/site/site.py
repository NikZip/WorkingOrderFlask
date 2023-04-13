from flask import Blueprint, render_template, request
from SiteApp.forms import TabNForm
from SiteApp.models import WorkingOrder

site_bp = Blueprint('site_bp', __name__,
                    template_folder='templates')


@site_bp.get('/')
def main():
    form = TabNForm()
    return render_template('site.html', personal_n_form=form, order_data='')


@site_bp.post('/')
def render_order():
    form = TabNForm(request.form)

    """ if form validate then send data and render """

    if form.validate_on_submit():

        personal_n = form.personal_n.data
        date = form.date.data

        order_data = WorkingOrder.get_by_personal_n(personal_n, date)
        return render_template('site.html',
                               personal_n_form=form,
                               order_data=order_data)
    else:
        return render_template('site.html', personal_n_form=form, order_data='')
