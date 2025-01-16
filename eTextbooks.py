from flask import Flask, render_template,request
import pandas as pd
from markupsafe import escape

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

# use pandas to read the log file
    


@app.route('/')
@app.route('/entry')
def entry_page()->'html':
    #books_df = pd.read_excel('Ebook Match with Bookstore Spring 2022.xlsx',header=0,sheet_name="Ebook Library Match")
    books_df = pd.read_excel('/Users/dpalmquist/source/eTextBookList/etextbooks-list-f24.xlsx',header=0,sheet_name="books")
    books = books_df[['SectionCode','Instructor','Title','URL']].sort_values("SectionCode").to_dict('records')
    return render_template('row.html',the_title='No cost textbooks', the_books=books)


if __name__ == "__main__":
    app.run(debug=True)
