import gzip
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/upload", methods=["POST"])
@cross_origin(supports_credentials=True)
def fileUploader():

    file = request.files["file"]
    fileType = file.content_type
    KEYWORDS = ["From: ", "To: ", "Subject: ", "Message-ID: ", "Date: ", "MIME-Version: "]
    RETURN_DATA = []
    def gZipHandler():
        f = gzip.open(file, "rb")
        for line in f:
            print(type(line))
            print( type(line.decode()) )
            new_entry = None
            if any( word in line.decode()  for word in KEYWORDS ):
                new_entry = { "data": line.decode() }
            if(new_entry != None):
                RETURN_DATA.append(new_entry)

        f.close()
    
    if(fileType == "application/x-gzip"):
        gZipHandler()

    return json.dumps(RETURN_DATA)



@app.route("/")
def home(): 
    return "Hello World, Flask omething"




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

    