from flask import Flask, render_template, request, url_for
from googletrans import Translator
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
import os


app = Flask(__name__)

language = ['Auto', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani',
                 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chewa',
                 'Chinese (Simplified)', 'Chinese (Traditional)''Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch',
                 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Galician', 'Georgian', 'German',
                 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
                 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh',
                 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian',
                 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
                 'Marathi', 'Mongolian', 'Nepali', 'Norwegian (Bokmål)', 'Odia', 'Pashto', 'Persian', 'Polish',
                 'Portuguese', 'Punjabi (Gurmukhi)', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
                 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese',
                 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian',
                 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'West Frisian', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']



mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'sahusonu220401@gmail.com',
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@cross_origin()
def home():
    return render_template('home.html', language=language)

@app.route('/', methods=["POST", "GET"])
@cross_origin()
def result():
    froms = str(request.form.get('froms'))
    to = str(request.form.get('to'))
    tex = str(request.form.get('tex'))
    translator = Translator()
    a = translator.translate(tex, dest=to, src=froms)
    a = a.text
    return render_template('result.html',result=a)

@app.route("/about", methods=["GET"])
@cross_origin()
def about():
    return render_template('about.html')

@app.route("/feedback", methods=["GET"])
@cross_origin()
def feedback():
    return render_template('feedback.html')

@app.route("/thanks", methods=["POST", "GET"])
@cross_origin()
def thanks():
    name = request.form.get('Name')
    email = request.form.get('Email')
    feedback = request.form.get('description')
    if name=='' or email=='' or feedback=='':
        return render_template('error.html')
    else:
        with app.app_context():
            msg = Message(subject="translator_feedback",
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=['hsahu615@gmail.com'], # replace with your email for testing
                          body=name+','+email+','+feedback)
            mail.send(msg)
        return render_template('thanks.html', name=name)



port = int(os.getenv("PORT"))
if __name__ == '__main__':
        # app.run(host='0.0.0.0', port=5000)
        app.run(host='0.0.0.0', port=port)
        # app.run(host='127.0.0.1', port=8001, debug=True)
