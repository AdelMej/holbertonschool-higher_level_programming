from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open("items.json", "r") as f:
        data = json.load(f)

    return render_template('items.html', items=data["items"])


@app.route('/products')
def products():
    source = request.args.get('source')
    opt_id = request.args.get('id')
    output = None

    if source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                output = [items for items in reader]
        except Exception:
            pass

    if source == "json":
        try:
            with open("products.json", "r") as f:
                output = json.load(f)
        except Exception:
            pass

    if not output:
        return render_template('product_display.html', error='Wrong source')

    if opt_id:
        output = next((p for p in output if str(p.get("id")) == str(opt_id)), None)

        if not output:
            return render_template('product_display.html', error='Product not found')

        return render_template('product_display.html', items=[output])

    return render_template('product_display.html', items=output)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
