from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/services')
def services():
    services_data = [
        {"name": "Web Development", "desc": "Building fast, responsive websites."},
        {"name": "Automation", "desc": "Automate boring stuff with Python."},
        {"name": "Data Analysis", "desc": "Visualize and analyze data easily."}
    ]
    return render_template("services.html", services=services_data)



if __name__ == '__main__':
    app.run(debug=True)
