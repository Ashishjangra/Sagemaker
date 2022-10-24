import json
import flask

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    try:
        status = 200
    except:
        status = 400
    return flask.Response(response=json.dumps(' '), status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    try:
        if flask.request.content_type.startswith('application/json'):
            data = flask.request.get_data()
            input_json = json.loads(data.decode("utf-8"))
        else:
            return flask.Response(response="Incorrect content format, require JSON", status=400,
                                  mimetype=flask.request.content_type)

        #TODO: Sample line need to implement yourself
        image_name = input_json['image_name']
        prediction = get_result_from_model(image_name)
        # Transform predictions to JSON
        result = {
            'prediction': prediction
        }
        result_json = json.dumps(result)
        return flask.Response(response=result_json, status=200, mimetype='application/json')
    except Exception as e:
        return flask.Response(response="Some Exception Occurred", status=400, mimetype=flask.request.content_type)
