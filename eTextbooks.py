from flask import Flask, render_template,request,escape
import pandas as pd

app = Flask(__name__)

def log_request(req, res):
    with open('vsearch.log',mode='a') as log_file:
        print(req.form, file=log_file, end='|')
        print(req.remote_addr, file=log_file, end='|')
        print(req.user_agent, file=log_file, end='|')
        print(res, file=log_file)


# @app.route('/log')
# def view_log()->'html':
#     #results = []
#     with open('vsearch.log') as log_file:
#         # for line in log_file.readlines():
#         #     results.append(line.split('|'))
#         results=[line.split('|') for line in log_file.readlines()]
#         return str(escape(results))
    

@app.route('/')
@app.route('/entry')
def entry_page()->'html':
    books_df = pd.read_excel('Ebook Match with Bookstore Spring 2022.xlsx',header=0,sheet_name="Ebook Library Match")
    books = books_df[['Section Code','Instructor Name','Short Title','Permalink']].sort_values("Section Code").to_dict('records')
    return render_template('row.html',the_title='Welcome to letter search on the web', the_books=books)


if __name__ == "__main__":
    app.run(debug=True)
