from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

@app.route('/random-dates', methods=['GET'])
def random_dates():
    start_date = datetime.date.today() + datetime.timedelta(days=random.randint(180, 240))  # 6-8 months ahead
    end_date = start_date + datetime.timedelta(days=5)  # 5 days after start
    return jsonify({
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)
