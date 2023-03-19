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
        <html>
            <head>
                <title>GPT Demo</title>
                <style>
                    /* Set global styles */
                    * {{
                        box-sizing: border-box;
                    }}
                    body {{
                        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #F7F7F7;
                    }}
                    h1 {{
                        font-size: 3rem;
                        margin-top: 2rem;
                        margin-bottom: 1.5rem;
                        text-align: center;
                        color: #2a9fd6;
                    }}
                    .links {{
                        max-width: 600px;
                        margin: 0 auto;
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: center;
                        align-items: center;
                    }}
                    .links a {{
                        display: block;
                        padding: 20px;
                        margin: 20px;
                        text-align: center;
                        text-decoration: none;
                        font-size: 1.5rem;
                        color: #2a2a2a;
                        background-color: #FFFFFF;
                        border-radius: 5px;
                        box-shadow: 0px 3px 3px rgba(0,0,0,0.1);
                        transition: all 0.2s ease-in-out;
                    }}
                    .links a:hover {{
                        transform: translateY(-2px);
                        box-shadow: 0px 5px 5px rgba(0,0,0,0.2);
                    }}
                    .links a:focus {{
                        outline: none;
                        background-color: #2a9fd6;
                        color: #FFFFFF;
                    }}
                </style>
            </head>
            <body>
                <h1>GPT Demo</h1>
                <div class="links">
                    <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
                    <a href="{url_for('aboutTianling')}">An about page for Tianling</a>
                    <a href="{url_for('aboutBing')}">An about page for Bing</a>
                    <a href="{url_for('aboutFeifan')}">An about page for Feifan</a>
                    <a href="{url_for('aboutYingshan')}">An about page for Yingshan</a>
                    <a href="{url_for('team')}">Team Page</a>
                    <a href="{url_for('gptdemoFeifan')}">Feifan's demo</a>
                    <a href="{url_for('gptdemoBing')}">Bing's demo</a>
                    <a href="{url_for('gptdemoYingshan')}">Yingshan's demo</a>
                    <a href="{url_for('gptdemoTianling')}">Tianling's demo</a>
                </div>
            </body>
        </html>
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
    return "<h1>The program get_tech_chef_challenge generates a GTP response based on the prompt, \"If software development was a cooking show, what kind of ingredients would each programming language bring to the table?\", and the requirements provided in the text parameter.</h1>"

@app.route('/aboutBing')
def aboutBing():
    return "<h1>The program getPoem generates a poem about the coding and your favorite programming language </h1>"

@app.route('/aboutFeifan')
def aboutFeifan():
    return "<h1>The program get_leetcode_questions is for randomly generating the desired number of LeetCode questions for practice.</h1>"

@app.route('/aboutYingshan')
def aboutYingshan():
    return "<h1>The program getJoke generates a GPT response based on the given topic/prompts</h1>"

@app.route('/team')
def team():
    return '''
    <h1>About our team :)</h1>
    <h2>Tianling Hou</h2>
    <p>Hello, my name is Tianling Hou and I am an MS4 student at Brandeis University. I have a few passions in life, including snowboarding, eating delicious food, and traveling. I find it exhilarating to explore new places, meet new people, and learn about different cultures. When I'm not hitting the slopes or trying out new restaurants, I enjoy working with my team members to help develop and improve our projects. I am a strong team player and I believe in working collaboratively to achieve our goals. I am always looking for ways to contribute to the team and make our projects the best they can be.</p>
    <h2>Bing Han</h2>
    <p>I'm an MS4 student at Brandeis University. I have a little yorkie Luna. My role is to make sure our webpage runs properly.</p>
    <h2>Feifan He</h2>
    <p>I'm an MS4 student at Brandeis University with a passion for longboarding and a cute hamster named Tater Tots. I'm all about creating good vibes and keeping the team motivated. </p>
    <h2>Yingshan Hu</h2>
    <p>I am a MS4 student at Brandeis University.<br> I am also a proud owner of a cute rag doll cat who keeps me company while I study and work on my projects.
    In my free time, I love to travel and explore new places, but when I'm not traveling, I enjoy building webpages and developing my coding skills.As for my role, I love collaborating with my teammates and I help optimize our work’s performance. </p>
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

@app.route('/gptdemoYingshan', methods=['GET', 'POST'])   
def gptdemoYingshan():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getJoke(prompt)
        return f'''
        <h1>Yingshan Demo</h1>
        <pre style="bgcolor:#74b3ce">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemoYingshan')}> make another query</a>
        '''
    else:
        return '''
        <h1>Yingshan's Demo</h1>
        Good Day! I will be generating a joke for you, so please let me know one of your interested topics:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
        
@app.route('/gptdemoTianling', methods=['GET', 'POST'])
def gptdemoTianling():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_tech_chef_challenge(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemoTianling')}> make another query</a>
        '''
    else:
        return '''
        <h1>Tianling's Demo</h1>
        Are you curious about what ingredients each programming language would bring to the table if software development was a cooking show? If so, you're in luck! Simply enter the programming languages you'd like to learn about, as well as any additional requirements or details you're interested in, and we'll generate a GPT response that's sure to satisfy your curiosity.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
if __name__=='__main__':
    # to run the program: bash secretINITIAL.sh 'python3 gptWebApp.py'
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
