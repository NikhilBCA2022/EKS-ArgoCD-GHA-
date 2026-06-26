from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Cloud App</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Segoe UI;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;

            background:
            linear-gradient(
            135deg,
            #667eea,
            #764ba2,
            #ff6b6b);

            color:white;
        }

        .card{
            width:700px;

            background:rgba(255,255,255,0.12);

            backdrop-filter:blur(18px);

            border-radius:20px;

            padding:50px;

            text-align:center;

            box-shadow:
            0 20px 50px rgba(0,0,0,0.3);
        }

        h1{
            font-size:52px;
            margin-bottom:20px;
        }

        .badge{
            display:inline-block;

            padding:10px 20px;

            border-radius:30px;

            background:#00ff95;

            color:black;

            font-weight:bold;

            margin-bottom:25px;
        }

        p{
            font-size:20px;
            opacity:0.9;
        }

        .btn{
            margin-top:35px;

            display:inline-block;

            text-decoration:none;

            background:white;

            color:#764ba2;

            padding:14px 30px;

            border-radius:10px;

            font-weight:bold;

            transition:0.3s;
        }

        .btn:hover{
            transform:scale(1.08);
        }

        .footer{
            margin-top:25px;
            opacity:0.8;
        }
    </style>

</head>

<body>

<div class="card">

<h1>🚀 Flask + Docker</h1>

<div class="badge">
Application Running
</div>

<p>
Beautiful containerized Flask application
running inside Kubernetes.
</p>

<a href="/health" class="btn">
Health Check
</a>

<div class="footer">
Made with Flask ❤️
</div>

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return {
        "status": "running",
        "service": "flask-app",
        "message": "Application Healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )