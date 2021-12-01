from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Grocery Store Title', validators=[DataRequired()])
    address = StringField('Grocery Store Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()], choices=ItemCategory.choices())
    photo_url = StringField('Photo', validators=[URL()])
    store = QuerySelectField('Grocery Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
