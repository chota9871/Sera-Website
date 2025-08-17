from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index24.html')  # Home page

@app.route('/about')
def about():
    return render_template('about.html')  # About page

@app.route('/services')
def services():
    return render_template('service.html')  # Services page

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Contact page

if __name__ == '__main__':
    app.run(debug=True)
