# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
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

class Index(restful.Resource):
    def get(self):
        return render_template('index.html')

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

# router
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
