from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,RadioField,PasswordField,TextAreaField,IntegerField,HiddenField
from wtforms.validators import DataRequired,Optional, Length
from wtforms_components import EmailField
from wtforms.widgets.html5 import NumberInput
class formulario(FlaskForm):
    tipo = "cadastro"
    cod = HiddenField()
    nome = StringField('Nome',validators=[DataRequired()])
    salario = StringField('Salário',validators=[DataRequired()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    sexo = RadioField('Gênero',validators=[DataRequired()],choices=[('F','Feminino'),('M','Masculino')])
    num_filhos = IntegerField('Número de filhos',validators=[DataRequired()],widget=NumberInput(max=99),default=0)
    biografia = TextAreaField('Biografia',validators=[DataRequired(),Length(max=5000,message="O máximo de caracteres é 5000")])
    login =  EmailField('Email',validators=[DataRequired()])
    enviar = SubmitField('Enviar')
