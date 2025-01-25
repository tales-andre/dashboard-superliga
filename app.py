from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios da Superliga de Vôlei
dados_superliga = [
    {"time": "Sada Cruzeiro", "vitorias": 20, "derrotas": 2},
    {"time": "Taubaté", "vitorias": 18, "derrotas": 4},
    {"time": "Flamengo", "vitorias": 15, "derrotas": 7},
    {"time": "Minas Tênis Clube", "vitorias": 12, "derrotas": 10}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', dados=dados_superliga)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
