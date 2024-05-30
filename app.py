from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/admission-procedure', methods=['GET'])
def admission_procedure():
    return jsonify({
        "procedure": "The admission procedure involves filling out an application form, submitting necessary documents, and attending an interview."
    })

@app.route('/requirements', methods=['GET'])
def requirements():
    return jsonify({
        "requirements": "The requirements include high school transcripts, letters of recommendation, and a personal statement."
    })

@app.route('/deadlines', methods=['GET'])
def deadlines():
    return jsonify({
        "deadlines": "The application deadline is June 30th."
    })

if _name_ == '_main_':
    app.run(debug=True)