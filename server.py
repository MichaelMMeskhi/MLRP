from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("")

@app.route("", methods=["POST"])
def upload():
	target = os.path.join(APP_ROOT, "")
	print(target)
	if not os.path.isdir(target):
		os.mkdir(target)
	else:
		print("Couldn't create upload directory: {}".format(target))
	print(request.files.getlist("file"))
	for upload in request.files.getlist("file"):
		print(upload)
		print("{} is the file name".format(upload.filename))
		filename = upload.filename
		destination = "/".join([target, ""])
		print("Accepting incoming resume:", filename)
		upload.save(destination)


	return render_template("")


if __name__ == "__main__:
	app.run(port=4555, debug=True)
