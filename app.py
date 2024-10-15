from flask import Flask, request, render_template, redirect, url_for, flash, send_file, send_from_directory
from io import BytesIO
import base64
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# File size limit: 4.5 MB (4.5 * 1024 * 1024 bytes)
MAX_FILE_SIZE = 4.5 * 1024 * 1024  # 4.5MB
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE  # Enforce max file size at Flask level

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/encode', methods=['POST'])
def encode_file():
    if 'file' not in request.files:
        flash('No file part', 'encode')
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'encode')
        return redirect(url_for('index'))

    if file:
        file_data = file.read()

        # Check if the file size exceeds the 4.5MB limit
        if len(file_data) > MAX_FILE_SIZE:
            flash('File exceeds the 4.5MB size limit', 'encode')
            return redirect(url_for('index'))

        # Encode the file data to Base64
        encoded_string = base64.b64encode(file_data).decode('utf-8')

        # Show the encoded string in the template
        return render_template('index.html', base64_string=encoded_string)
    else:
        flash('An error occurred while uploading the file.', 'encode')
        return redirect(url_for('index'))


@app.route('/decode', methods=['POST'])
def decode_string():
    base64_string = request.form['base64_string']

    if not base64_string:
        flash('No Base64 string provided', 'decode')
        return redirect(url_for('index'))

    # Decode the Base64 string back to binary data
    try:
        decoded_data = base64.b64decode(base64_string)
    except Exception as e:
        flash('Invalid Base64 string', 'decode')
        return redirect(url_for('index'))

    # Create an in-memory file from the decoded data
    decoded_file = BytesIO(decoded_data)
    decoded_file.seek(0)

    # Send the decoded file as a download without any extension
    download_filename = "decoded_file"

    return send_file(decoded_file, as_attachment=True, download_name=download_filename)


# Error handler for when file size exceeds the limit
@app.errorhandler(413)
def file_too_large(e):
    flash('File exceeds the 10MB size limit', 'encode')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
