from flask import  render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Pessoa, Usuarios





@app.route('/')
def index():
    lista = Pessoa.query.order_by(Pessoa.id)

    return render_template('index.html', titulo = "pessoa" , pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('novo')))
    return render_template('novo.html', titulo = "Cadastrar")

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoa.query.filter_by(nome=nome).first()

    if pessoa:
        flash("Pessoa já existente")
        return redirect(url_for('index'))
    
    nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('editar')))
    
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('editar.html', titulo = 'Editar Pessoa', pessoa = pessoa)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    # Obter os dados enviados pelo formulário
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    # Encontrar a pessoa pelo nome
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    if pessoa:
        # Atualizar os dados da pessoa
        pessoa.idade = idade
        pessoa.altura = altura
        # Commit para salvar as alterações no banco de dados
        db.session.commit()
        flash('Dados atualizados com sucesso!')
    else:
        flash('Pessoa não encontrada.')
    
    # Redirecionar de volta para a página principal
    return redirect(url_for('index'))

@app.route('/login')
def login():

    proximo = request.args.get('proximo')

    return render_template('login.html', proximo =proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:

        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname  + 'Você está logado')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    else:
            flash("Senha incorreta")
            return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash("Você foi desconectado")
    return redirect('/login')
