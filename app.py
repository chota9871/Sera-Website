from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index24.html')  # Home page

@app.route('/about')
def about():
    return render_template('About.html')  # About page

@app.route('/services')
def services():
    return render_template('Service.html')  # Services page

@app.route('/contact')
def contact():
    return render_template('Contact.html')  # Contact page

if __name__ == '__main__':
    # Important: host='0.0.0.0' to accept external traffic on Render
    app.run(host='0.0.0.0', port=5000, debug=True)



