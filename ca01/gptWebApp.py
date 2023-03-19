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
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)

gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
#app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a><br>
        <a href="{url_for('aboutTianling')}">An about page for Tianling</a><br>
        <a href="{url_for('aboutBing')}">An about page for Bing</a><br>
        <a href="{url_for('aboutFeifan')}">An about page for Feifan</a><br>
        <a href="{url_for('aboutYingshan')}">An about page for Yingshan</a><br>
        <a href="{url_for('team')}">Team Page</a><br>
        <a href="{url_for('gptdemoFeifan')}">Feifan's demo</a><br>
         <a href="{url_for('gptdemoBing')}">Bing's demo</a><br>
    '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form
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

@app.route('/aboutTianling')
def aboutTianling():
    return "<h1>The program is about Tianling</h1>"

@app.route('/aboutBing')
def aboutBing():
    return "<h1>The program getPoem generates a poem about the coding and your favorite programming language </h1>"

@app.route('/aboutFeifan')
def aboutFeifan():
    return "<h1>The program get_leetcode_questions is for randomly generating the desired number of LeetCode questions for practice.</h1>"

@app.route('/aboutYingshan')
def aboutYingshan():
    return "<h1>The program is about....</h1>"

@app.route('/team')
def team():
    return '''
    <h1>About our team :)</h1>
    <h2>Tianling Hou</h2>
    <p></p>
    <h2>Bing Han</h2>
    <p><I'm an MS4 student at Brandeis University. I have a little yorkie Luna. My role is to make sure our webpage runs properly./p>
    <h2>Feifan He</h2>
    <p>I'm an MS4 student at Brandeis University with a passion for longboarding and a cute hamster named Tater Tots. I'm all about creating good vibes and keeping the team motivated. </p>
    <h2>Yingshan Hu</h2>
    <p></p>
    '''

@app.route('/gptdemoFeifan', methods=['GET', 'POST'])
def gptdemoFeifan():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_leetcode_questions(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemoFeifan')}> make another query</a>
        '''
    else:
        return '''
        <h1>Feifan's Demo</h1>
        Enter the number of LeetCode questions to generate:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/gptdemoBing', methods=['GET', 'POST'])
def gptdemoBing():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getPoem(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:pink">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemoBing')}> make another query</a>
        '''
    else:
        return '''
        <h1>Bing's Demo</h1>
        Enter your favorite programming language:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
if __name__=='__main__':
    # to run the program: bash secretINITIAL.sh 'python3 gptWebApp.py'
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)