from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Inicio - Aplicación Flask</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(to right, #74ebd5, #acb6e5);
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
                text-align: center;
                width: 90%;
                max-width: 600px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            p {
                color: #666;
                font-size: 1.1em;
                margin-bottom: 30px;
            }
            a.button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 6px;
                transition: background-color 0.3s ease;
            }
            a.button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenido a mi Aplicación Flask</h1>
            <p>Explora cómo usar patrones de diseño empresariales con Python y Flask.</p>
            <a class="button" href="/customers">Ir a Clientes</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
