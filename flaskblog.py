from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'M Kiran Kumar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 15, 2022'
    },
    {
        'author': 'charan naik',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 16, 2022'
    }
]



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)