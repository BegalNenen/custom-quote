from flask import Flask, render_template, request
app = Flask(__name__, template_folder="template", static_folder="assets")

@app.route("/")
def index():
	return render_template("/index.html")

@app.errorhandler(404) 
def invalid_route(e): 
    return '<meta name="viewport" content="width=device-width,initial-scale=1.0">Cari apa kak?'	
			
@app.route("/result",methods=["GET","POST"])
def result():
	if request.method == "POST":
		nama = request.form["author"]
		kutipan = request.form["quotes"]
		return render_template("/result.html", author=nama, quote=kutipan)
	else:
		return render_template("/index.html")

if __name__ == '__main__':
	app.run(debug = True)
	
