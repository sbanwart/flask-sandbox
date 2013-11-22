from urllib.parse import urljoin
from flask import Flask, request, render_template_string, make_response
from werkzeug.contrib.atom import AtomFeed
from time import gmtime, strftime
from datetime import datetime
from uuid import uuid1
from os import listdir

files = listdir('./files')

app = Flask(__name__)

def make_external(url):
    return urljoin(request.url_root, url)

@app.route('/orders.atom', methods=['GET'])
def recent_feed():
    print('Getting orders ATOM feed')
    feed = AtomFeed('Orders', feed_url=request.url, url=request.url_root)
    for fname in files:
        urlid = str(uuid1())
        testfile = open('./files/' + fname)
        feed.add("Order", 
                        testfile.read(),
                        content_type="xml",
                        author="edi",
                        url=make_external(urlid),
                        updated=datetime.utcnow(),
                        published=datetime.utcnow())
    return feed.get_response()

@app.route('/orders', methods=['POST'])
def create_order():
    print('Order data: {}'.format(request.data))
    return make_response(render_template_string('Done'), 201)

if __name__ == "__main__":
    app.run(debug=True)
