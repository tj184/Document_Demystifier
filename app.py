import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flashing messages

# Folder to save uploads
UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed file types
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            flash("File uploaded successfully!")
            return redirect(url_for("upload_file"))
        else:
            flash("Invalid file type! Please upload images or PDFs.")
            return redirect(request.url)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)
