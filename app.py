from flask import Flask,render_template,request,jsonify  #Flask for backend app, render_temp for dispay html page, request to get data from js, jsonify sends json back to js

app=Flask(__name__)  #creating app (Flask app)

@app.route("/")
def home():
    return render_template("index.html") #searching for index.html


@app.route("/translate", methods=["POST"])
def translate():
    data=request.get_json() #receives data using json 

    source_text=data.get("text")
    source_lang=data.get("source_lang")
    target_lang=data.get("target_lang")

    print("Text:", source_text)
    print("From:",source_lang)
    print("To:",target_lang)


    translated_text="Translation Text"


    return jsonify({
        "transaltion":translated_text #sending result back
    })


if __name__  == "__main__": #start flask app
    app.run(debug=True) #automatically realaods 

