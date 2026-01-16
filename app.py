from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# We use deep_translator for the web demo for speed and reliability
from deep_translator import GoogleTranslator 

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests for local testing

# Language Code Mapping (Matches your HTML dropdowns)
LANG_MAP = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text', '')
        source_lang = data.get('source_lang', 'English')
        target_lang = data.get('target_lang', 'Hindi')

        if not text:
            return jsonify({'translation': ''})

        # Map full names to ISO codes
        src_code = LANG_MAP.get(source_lang, 'en')
        tgt_code = LANG_MAP.get(target_lang, 'hi')

        # Perform Translation
        translator = GoogleTranslator(source=src_code, target=tgt_code)
        translated = translator.translate(text)

        return jsonify({'translation': translated})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)