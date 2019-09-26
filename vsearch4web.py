from flask import Flask, render_template,request,escape
from vsearch import search4letters


app = Flask(__name__)

def log_request(req, res):
    with open('vsearch.log',mode='a') as log_file:
        print(req.form, file=log_file, end='|')
        print(req.remote_addr, file=log_file, end='|')
        print(req.user_agent, file=log_file, end='|')
        print(res, file=log_file)

@app.route('/search4', methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    title = 'here are the results'
    log_request(request,results)
    return render_template('results.html', the_results=results, the_title = title, the_letters=letters, the_phrase=phrase)

@app.route('/log')
def view_log()->'html':
    #results = []
    with open('vsearch.log') as log_file:
        # for line in log_file.readlines():
        #     results.append(line.split('|'))
        results=[line.split('|') for line in log_file.readlines()]
        return str(escape(results))
    

@app.route('/')
@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html',the_title='Welcome to letter search on the web')


if __name__ == "__main__":
    app.run(debug=True)
