from flask import Flask, render_template, request
# import pymysql
from ultralytics import YOLO
from bot import get_news, get_links, get_cryp

app = Flask(__name__)
model = YOLO('static/best.pt')


@app.route('/')
def home():
    news = get_news()
    links = get_links()
    cryps = get_cryp()
    return render_template('homepage.html', 
                           Stock1=cryps[0].text+'↗️', 
                           Stock2=cryps[1].text+'↘️', 
                           Stock3=cryps[2].text+'↘️',
                           Stock4=cryps[3].text+'↗️',
                           Stock5=cryps[4].text+'↘️',
                           Stock6=cryps[5].text+'↘️',
                           news1=news[0].text, 
                           news2=news[1].text, 
                           news3=news[2].text, 
                           news4=news[3].text, 
                           news5=news[4].text, 
                           news6=news[5].text, 
                           url1=links[0]['href'],
                           url2=links[1]['href'],
                           url3=links[2]['href'],  
                           url4=links[3]['href'],
                           url5=links[4]['href'],
                           url6=links[5]['href']                  
                           
                           )


@app.route('/upl')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def define():
    file = request.files['file']
    with open('static/saved.png', 'wb') as f:
            f.write(file.read())

    results = model('static/saved.png')
    for result in results:
        id = result.probs.top1
    name = result.names[id]
    
    if name == "DOWN":
        name="Sell ↘️"
    elif name == "UP":
        name="Buy ↗️"

    return render_template('after_upload_predict.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

