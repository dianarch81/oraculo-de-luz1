from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
import random

app = Flask(__name__)

# ✉️ Configuración del correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'infinite.guidance8@gmail.com'
app.config['MAIL_PASSWORD'] = 'uxoqkmhoxlphsrdq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# 🧠 Base de datos temporal: email -> código
codigos_temp = {}

# 🌐 Página inicial
@app.route('/')
def home():
    return '''
    <html>
    <head><title>Oráculo ✨</title></head>
    <body style="text-align:center; margin-top:100px; font-family:Georgia;">
    <h1>Bienvenido al Oráculo ✨</h1>
    <p>Ingresa tu correo para recibir una frase inspiradora:</p>
    <form action="/enviar_codigo" method="POST">
    <input type="email" name="email" placeholder="Tu correo" required>
    <button type="submit">Recibir código</button>
    </form>
    </body>
    </html>
    '''

# 💌 Enviar código
@app.route('/enviar_codigo', methods=['POST'])
def enviar_codigo():
    email = request.form['email']
    codigo = str(random.randint(100000, 999999))
    codigos_temp[email] = codigo

    msg = Message("Tu código del Oráculo ✨",
    sender='infinite.guidance8@gmail.com',
    recipients=[email])
    msg.body = f"Tu código para acceder a tu frase es: {codigo}"
    mail.send(msg)

    # Página para ingresar el código
    codigo_html = '''
    <html>
    <head><title>Ingresa tu código</title></head>
    <body style="text-align:center; margin-top:100px; font-family:Georgia;">
        <h2>Código enviado al correo {{ email }} ✨</h2>
        <p>Ingresa el código para recibir tu frase:</p>
        <form action="/verificar-codigo" method="POST">
            <input type="text" name="codigo" placeholder="Código recibido" required>
            <input type="hidden" name="email" value="{{ email }}">
            <button type="submit">Ver frase sagrada</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(codigo_html, email=email)

# ✅ Verificar código
from datetime import date

@app.route('/verificar-codigo', methods=['POST'])
def verificar_codigo():
    email = request.form['email']
    codigo_ingresado = request.form['codigo']

    if codigos_temp.get(email) == codigo_ingresado:
        # Si hoy es 2025‑04‑24, retorna la frase especial:
        if date.today() == date(2025, 4, 24):
            frase = ("Camina con certeza, \n"
                    "porque los caminos invisibles ya están abriéndose para ti, \n" 
                    "Tu verdad será reconocida, \n"
                    "porque quien camina con el corazón limpio \n"
                    "hace visible lo invisible.\n"
                    )
        else:
            # tu frase por defecto
            frase = "Esta es la frase que tu alma necesitaba leer hoy ✨💛"
        return render_template_string(f"""
        <h1 style="font-family:Georgia;text-align:center;margin-top:100px;">
            {frase}
        </h1>
        """)
    else:
        return "<h1 style='text-align:center;color:red;'>Código incorrecto. Intenta nuevamente.</h1>"


if __name__ == '__main__':
    pass # Esto evita el error de indentación
