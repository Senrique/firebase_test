# Adds new rows to an alredy existing datatable on python dash 
import pyrebase
import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html

config = {
    "apiKey": "AIzaSyAhprsOQ0rQ514WqPyERMlvwsQRJJTqpC8",
    "authDomain": "dash-pr.firebaseapp.com",
    "databaseURL": "https://dash-pr.firebaseio.com",
    "projectId": "dash-pr",
    "storageBucket": "dash-pr.appspot.com",
    "messagingSenderId": "159067587973",
    "appId": "1:159067587973:web:977a9594b0d30cc8"
}

app_login_layer = dash.Dash()
app_login_layer.config.suppress_callback_exceptions = True

app_login_layer.layout = html.Div([
    html.Div(dcc.Input(id='input_box', placeholder = 'Enter Email ID', value = '',type='text')),
	html.Div(dcc.Input(id='input_box2', placeholder = 'Enter password', value = '', type='text')),
    html.Button('Sign in', id='signin_button'),
	html.Button('Sign up', id='signup_button'),
    html.Div(id='container-button-basic',
             children=''),
	html.Div(id='container-button-basic2',
             children='')
])

@app_login_layer.callback(
    Output('container-button-basic', 'children'),
    [Input('signup_button', 'n_clicks')],
    [State('input_box', 'value'),
	State('input_box2', 'value')])
	
def store_sign_up(n_clicks, email, password):
	if n_clicks == None:
		return None
	elif n_clicks >= 1:
	
		firebase = pyrebase.initialize_app(config)
		auth = firebase.auth()
		user = auth.create_user_with_email_and_password(email, password)
	return 'Sign in credentials saved' 

@app_login_layer.callback(
    Output('container-button-basic2', 'children'),
    [Input('signin_button', 'n_clicks')],
    [State('input_box', 'value'),
	State('input_box2', 'value')])
	
def store_sign_in(n_clicks, email, password):
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	if n_clicks == None:
		return None
	elif n_clicks >= 1:
		try:
			auth.sign_in_with_email_and_password(email, password)
			variable = 'Login was successful'
		except:
			variable = 'Please check your credentials'
	return variable

		

if __name__ == '__main__':
    app_login_layer.run_server(debug=True)
	
