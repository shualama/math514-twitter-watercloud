import tweepy as tw
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from flask import Flask, redirect, url_for, render_template, request, send_file


consumer_key = 'kG5dlAXTpG1hbqV1mhnROHrv2'
consumer_secret = '8YfinITSHB1vKFzEAphuUh02D9ocw75ZXEFI6qgdXYfbJx8gqw'
access_token = '787885458-8vFRPXbZfATtJVZjRUmXF7RQZS5w90tNd8QZxJgp'
access_token_secret = 'NS8Lk9xiSVdsVVIuVQNMzS3IhMDW9Jn1WXujlVRnI1WxQ'
auth = tw.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# if you got this error in running the scrip,
#INTEL MKL ERROR: The operating system cannot run %1. mkl_intel_thread.dll.
#Here's the solution:


@app.route('/wordcloud', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':

        wordcloud = request.form['wordcloud']

        tweets = tw.Cursor(api.search, q=wordcloud, lang="en").items(100)
        cloud = ""
        for each in tweets:
            cloud = cloud + each.text
        cloud = WordCloud(background_color="white").generate(cloud)
        plt.axis('off')
        image = np.array(cloud)

        im = Image.fromarray(image)
        im.save("static/cloud.jpg")
        return render_template('wordcloud.html', wordcloud=wordcloud)



#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == "__main__":
    app.run()











