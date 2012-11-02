from urlparse import urljoin
from flask import Flask, request
from werkzeug.contrib.atom import AtomFeed
from time import gmtime, strftime
from datetime import datetime

app = Flask(__name__)

def make_external(url):
    return urljoin(request.url_root, url)

@app.route('/moops.atom')
def recent_feed():
    feed = AtomFeed('Orders', feed_url=request.url, url=request.url_root)
    feed.add("Order", unicode("<order><id>1000</id><customer>1023</customer><total>$20.94</total></order>"), content_type="xml", author="edi", url=make_external("orders/1000"), updated=datetime.utcnow(), published=datetime.utcnow())
    feed.add("Order", unicode("<order><id>1001</id><customer>2034</customer><total>$443.76</total></order>"), content_type="xml", author="edi", url=make_external("orders/1001"), updated=datetime.utcnow(), published=datetime.utcnow())
    return feed.get_response()

if __name__ == "__main__":
    app.run(debug=True)
