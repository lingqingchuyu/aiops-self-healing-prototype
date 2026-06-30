from flask import Flask, jsonify
import time
import random
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Histogram, Counter

app = Flask(__name__)

REQUEST_TIME = Histogram('order_request_duration_seconds', 'Order request duration')
REQUEST_COUNT = Counter('order_requests_total', 'Total order requests', ['status'])

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/order')
@REQUEST_TIME.time()
def create_order():
    delay = random.uniform(0.1, 1.2)
    time.sleep(delay)

    if random.random() < 0.2:
        REQUEST_COUNT.labels(status='error').inc()
        return jsonify({"status": "error", "msg": "Database connection timeout"}), 500

    REQUEST_COUNT.labels(status='success').inc()
    return jsonify({"status": "success", "order_id": random.randint(1000, 9999)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)