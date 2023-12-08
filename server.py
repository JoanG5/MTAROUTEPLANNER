from flask import Flask, jsonify
from flask_cors import CORS 
import MTAdata

app = Flask(__name__)
CORS(app)

@app.route('/getMTAData')
def get_mta_data_route():
    mta_data = MTAdata.graph_weight(MTAdata.build_graph())
    return jsonify(mta_data)

if __name__ == '__main__':
    app.run(debug=True)
