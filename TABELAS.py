import pymysql
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'insta'
)
cursor = conexao.cursor()

cursor.execute("CREATE TABLE Perfil(idUsuario VARCHAR(255) NOT NULL, privacidade VARCHAR(255) NOT NULL,nomeReal VARCHAR(255) NOT NULL,biografia VARCHAR(255) NOT NULL,seguidores INT NOT NULL,senha VARCHAR(15) NOT NULL)")
cursor.execute("CREATE TABLE Relacionamento(Perfil_idUsuario VARCHAR(255) NOT NULL)")
cursor.execute("CREATE TABLE Comentario(idComentario VARCHAR(255) NOT NULL, texto VARCHAR(255) NOT NULL, datahora INT NOT NULL, Perfil_idUsuario VARCHAR(255) NOT NULL)")
cursor.execute("CREATE TABLE Notificao(idNot VARCHAR(255) NOT NULL, tipo VARCHAR(255) NOT NULL, datahora INT NOT NULL, Perfil_idUsuario VARCHAR(255) NOT NULL, Comentario_idComentario VARCHAR(255) NOT NULL)")
cursor.execute("CREATE TABLE Postagem(idPostagem VARCHAR(255) NOT NULL, texto VARCHAR(255) NOT NULL, datahora INT NOT NULL, Perfil_idUsuario VARCHAR(255) NOT NULL)")
cursor.execute("CREATE TABLE Postagem_Topico(Postagem_idPostagem VARCHAR(255) NOT NULL, Topico_idTopico INT NOT NULL)")
cursor.execute("CREATE TABLE Topico(idTopico INT NOT NULL, datahora INT NOT NULL)")