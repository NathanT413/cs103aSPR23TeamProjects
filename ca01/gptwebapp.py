'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, redirect, url_for, Flask
from gpt import GPT


import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
	''' display a link to the general query page '''
	print('processing / route')
	return f'''
		<h1>GPT Demo</h1>
		<h2><a href="{url_for('gptdemo')}">Ask questions to GPT</a></h2>
		<br>
		<h2><a href="{url_for('about')}">About</a><h2>
		<br>
		<h2><a href="{url_for('team')}">Team</a></h2>
		<br>
		<h2><a href="{url_for('gpt_code_docs')}'>Code Documentation</a></h2>
		<br>
	 '''


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
	'''
	handle a get request by sending a form 
	and a post request by returning the GPT response
	'''
	if request.method == 'POST':
		prompt = request.form['prompt']
		answer = gptAPI.getResponse(prompt)
		return f'''
			<h1>GPT Demo</h1>
			<pre style="bgcolor:yellow">{prompt}</pre>
			<hr>
			Here is the answer in text mode:
			<div style="border:thin solid black">{answer}</div>
			Here is the answer in "pre" mode:
			<pre style="border:thin solid black">{answer}</pre>
			<a href={url_for('gptdemo')}> make another query</a>
		'''
	else:
		return '''
			<h1>GPT Demo App</h1>
			Enter your query below
			<form method="post">
				<textarea name="prompt"></textarea>
				<p><input type=submit value="get response">
			</form>
		'''


@app.route('/about')
def about():
	'''
	A page to describe the intent of gptwebapp.py.
	'''
	return '''
		<h1>About</h1>
		<h2>Description</h2>
		<p></p>
	'''


@app.route('/team')
def team():
	'''
	A page with a short biography about each team member.
	Brandon J. Lacy (AG3NTZ3R0)
	'''
	return f'''
		<h1>Team</h1>
		<h2>Brandon J. Lacy</h2>
		<h3>Biography</h3>
		<p>Brandon earned a Bachelor of Science degree in computer science and cybersecurity from Sacred Heart University. He has experience in both the public and private sector. He has worked as a member of the 
incident response team for the Office of the Comptroller of the Commonwealth of Massachusetts and as a member of the data science and insights team for Hubbell Inc. Brandon is excited to expand his knowledge of machine learning 
in an academmic setting to allow him to gain a deeper understand of the technology from both an application and mathematical perspective.</p>
		<h3>Role</h3>
		<p>Brandon was responsible for the the creation of the ca01 folder, the duplication of the gptwebapp.py and gpt.py files from lesson15, the creation of the <a href={url_for('gpt_code_docs')}>/gpt_code_docs</a> and 
<a href={url_for('gpt_code_docs_about')}>/gpt_code_docs/about</a> routes in gptwebapp.py and code_docs method in gpt.py, the creation of the team page, the creation of the about page, and his personal page.</p>
	'''


@app.route('/code_docs', methods=['GET', 'POST'])
def gpt_code_docs():
	'''
	Create documentation for an undocumented code file.
	Brandon J. Lacy (AG3NTZ3R0)
	'''
	if request.method == 'POST':
		lang = request.form['lang']
		code = request.form['code']
		answer = gptAPI.code_docs(lang, code)
		return f'''
			<h1>ChatGPT Code Documentation</h1>
			<h2><a href={url_for('gpt_code_docs_about')}>About</a></h2>
			<h2>Response</h2>
			<pre style="border:thin solid black">{answer}</pre>
			<h2><a href={url_for('index')}>Index</a></h2>
		'''
	else:
		return f'''
			<h1>ChatGPT Code Documentation</h1>
			<h2><a href={url_for('gpt_code_docs_about')}>About</a></h2>
			<h2>Query</h2>
			<form method="post">
				<h3><label for="lang">Programming Language</label></h3>
				<textarea name="lang"></textarea>
				<br>
				<h3><label for="code">Code: <label></h3>
				<textarea name="code"></textarea>
				<br>
				<input type=submit>
			</form>
			<h2><a href={url_for('index')}>Index</a></h2>
		'''


@app.route('/code_docs/about')
def gpt_code_docs_about():
	'''
	The about page that corresponds with gpt_code_docs and explains the intent as well as the way to operate the route.
	Brandon J. Lacy (AG3NTZ3R0)
	'''
	return f'''
		<h1>About Code Documentation</h1>
		<h2>Description</h2>
		<p>The purpose of this route is to provide a programmer with the ease of convenience in code documentation. A majority of the time a programmer documents their code haphazardly as they believe there is more important 
work to be completed, which leads to trouble down the road when maintenance needs to be performed on an application. Though we do not condone haphazard code documentation and recommend the individual to dedicate time to this 
critical development practice, we want to avoid the pain for the developer down the road that may need to interact with code with lackluster documentation.</p>
		<h2>Instructions</h2>
		<p>The route is incredibly simple to use, as we understand your lack of time on unnecessary tasks. Simply enter the programming language of the code and the code in their respective text boxes.</p>
		<h2><a href={url_for('gpt_code_docs')}>Back to Code Documentation</a></h2>
	'''


if __name__=='__main__':
    # MacOS uses 5000 so need to run on 5001
    app.run(debug=True,port=5001)
