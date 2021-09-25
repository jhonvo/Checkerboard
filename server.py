from flask import Flask,render_template

app = Flask (__name__)

color1 = 'black'
color2 = 'red'

@app.route ('/', methods=['GET'])
def index():
    return render_template( "index.html", col=8, row=8, color1=color1, color2=color2)

@app.route ('/<int:row>', methods=['GET'])
def indexRow(row):
    return render_templatce( "index.html", col=8, row=row, color1=color1, color2=color2)

@app.route ('/<int:col>/<int:row>', methods=['GET'])
def indexRowColum(col,row):
    return render_template( "index.html", col=col, row=row, color1=color1, color2=color2)

@app.route ('/<int:col>/<int:row>/<col1>', methods=['GET'])
def indexRowColumCol1(col,row,col1):
    return render_template( "index.html", col=col, row=row, color1=col1, color2=color2)

@app.route ('/<int:col>/<int:row>/<col1>/<col2>', methods=['GET'])
def indexRowColumCol2(col,row,col1,col2):
    return render_template( "index.html", col=col, row=row, color1=col1, color2=col2)

if __name__ == "__main__":
    app.run(debug=True)