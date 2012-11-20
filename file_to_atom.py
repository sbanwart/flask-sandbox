from urlparse import urljoin
from flask import Flask, request
from werkzeug.contrib.atom import AtomFeed
from time import gmtime, strftime
from datetime import datetime
from uuid import uuid1
from os import listdir

files = listdir('./files')

app = Flask(__name__)

def make_external(url):
    return urljoin(request.url_root, url)

@app.route('/orders.atom')
def recent_feed():
    feed = AtomFeed('Orders', feed_url=request.url, url=request.url_root)
    for fname in files:
        testfile = open('./files/' + fname)
        feed.add("Order", 
                        unicode(testfile.read()),
                        content_type="xml",
                        author="edi",
                        url=uuid1(),
                        updated=datetime.utcnow(),
                        published=datetime.utcnow())
    return feed.get_response()

if __name__ == "__main__":
    app.run(debug=True)
