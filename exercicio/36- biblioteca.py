app = Flask(__name__)

def connect_db():
    return sqlite3.connect('biblioteca.db')

# 1. Cadastro de Livros
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (titulo, autor, isbn, categoria) VALUES (?, ?, ?, ?)',
                   (data['titulo'], data['autor'], data['isbn'], data['categoria']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Livro adicionado com sucesso!'}), 201

# 2. Empréstimo de Livros
@app.route('/emprestimos', methods=['POST'])
def emprestar_livro():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo) VALUES (?, ?, ?)',
                   (data['livro_id'], data['usuario_id'], datetime.now().strftime('%Y-%m-%d')))
    cursor.execute('UPDATE livros SET status = ? WHERE id = ?', ('emprestado', data['livro_id']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Livro emprestado com sucesso!'}), 201

# 3. Cadastro de Usuários
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (data['nome'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201

# 4. Consulta e Busca no Acervo
@app.route('/livros', methods=['GET'])
def listar_livros():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()
    return jsonify(livros), 200

if __name__ == '__main__':
    app.run(debug=True)