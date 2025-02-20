from flask import Flask
import os
import datetime
import pytz
import psutil
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Trinadh Singamapalli "  # Replace with your full name
    username = os.getlogin()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h1>/htop Endpoint</h1>
        <p><strong>Name:Trinadh Singampalli</strong> {name}</p>
        <p><strong>Username: trinadhsin</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
