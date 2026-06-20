import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Poprawione os.path.join w funkcjach poniżej:
@app.route('/css/<path:filename>')
def custom_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'), filename)

@app.route('/js/<path:filename>')
def custom_js(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'), filename)

@app.route('/images/<path:filename>')
def custom_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/timer')
def wyswietl_timer():
    return render_template('timer.html')

if __name__ == '__main__':
    app.run(debug=True)