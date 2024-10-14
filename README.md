# BASE-X | Effortless encoding - Seamless decoding.

This is a simple web application built using Flask that allows users to upload any file and get its Base64 encoded string. It also provides the functionality to decode a Base64 string back into a file.

## How to Run

Follow the steps below to run the application on your local machine:

### Prerequisites

Ensure that you have the following installed:
- Python 3.7 or higher
- Flask

### Tailwind CSS 
Follow these to update tailwind css styling (optional)
```bash
npm install
npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/styles.css --watch
```

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/base64-encoder-decoder.git
   cd base64-encoder-decoder
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```
3. **Install the dependencies**
   ```bash
   pip install Flask
   ```
4. **Set the Flask app environment variable**
   ```bash
   export FLASK_APP=app.py  # For Linux/macOS
   set FLASK_APP=app.py  # For Windows
   ```
5. **Run the Flask application**
   ```bash
   flask run
   ```
6. **Access the application**
   ```bash
   http://127.0.0.1:5000
   ```

Now you can start uploading files for Base64 encoding or paste Base64 strings to decode them back into files.
