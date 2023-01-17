import logging
from random import choice
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/healthz', methods=['GET'])
def healthz():
    status = choice([200, 500])
    if status == 500:
        logger.warning("Returning HTTP 500 error")
        abort(500)
    else:
        logger.info("Returning HTTP 200 status code")
        return jsonify(status=status)

@app.route('/started', methods=['GET'])
def started():
    logger.info("Returning HTTP 200 status code")
    return jsonify(status=200)

if __name__ == '__main__':
    app.run()
