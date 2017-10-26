from flask import Flask, request
from flask.ext import restful

import sys
sys.path.append('screenshots/')
sys.path.append('evaluator/')

from screenshotter import capture
from evaluator import img2score

app = Flask(__name__)
api = restful.Api(app)

def url2score(url):
    print('>>> Working on %s' % url)
    file_name = capture(url)
    return img2score(file_name)

class Score(restful.Resource):
    def post(self):
        urls = request.json.get('urls')
        scores = []
        for url in urls:
            scores.append(url2score(url))
            data = { 'scores': scores }
        return data
    def get(self):
        url = request.args.get('url')
        return url2score(url)

class Image(restful.Resource):
    def post(self):
        file_name = 'upload_cache.png'
        request.files['file'].save(file_name) # save image to local
        return img2score(file_name)

api.add_resource(Score, '/api/score')
api.add_resource(Image, '/api/image')

if __name__ == '__main__':
    app.run(debug=True)
