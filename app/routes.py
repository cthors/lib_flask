from app import app
from app.commonFunc import CommonFunctions
from app.addRecords import AddRecords
from flask import render_template, request

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/list')
def show_records():
	allBooks = CommonFunctions.allBooksForDisplay()
	return render_template('list.html', books=allBooks)

@app.route('/add')
def add_records():
	results = AddRecords.addBook()
	return render_template('list_added.html', 
							newBooks=results[0],
							gBooks=results[1],
							oldBooks=results[2],
							noBooks=results[3],
							debugList=results[4],
							gBookIds=results[5])