from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
import wtforms.validators as v


class TabNForm(FlaskForm):
    personal_n = StringField('Табельный №', validators=[v.InputRequired(), v.length(max=10)])
    date = HiddenField('Дата',
                       validators=[v.DataRequired(), ],
                       id='hidden_input',
                       default=datetime.now().date(), )
    submit = SubmitField('Подтвердить')

    class Meta:
        csrf = False
        locales = 'ru'
