from flask import Flask, request
from flask.ext import restful
from evaluator import evaluate

app = Flask(__name__)
api = restful.Api(app)

class Score(restful.Resource):
    def post(self):
        urls = request.json.get('urls')
        scores = []
        for url in urls:
            scores.append(evaluate(url))
            data = { 'scores': scores }
        return data
    def get(self):
        return evaluate(request.args.get('url'))

api.add_resource(Score, '/api/score')

if __name__ == '__main__':
    app.run(debug=True)