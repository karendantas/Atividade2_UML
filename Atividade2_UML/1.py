import datetime

class autenticaMixIn:

    def autentica(self, user, login, senha):
        ''' Verifica se o login e a senha do usuario conferem com o cadastrado'''
        if login in user.getlogin() and senha in user.getsenha():
            return True
    
class Usuario(autenticaMixIn):
    def __init__(self, id, nome, login, senha):
        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__senha = senha


    def getlogin(self):
        return self.__login
    def getsenha(self):
        return self.__senha


class Postagem:
    def __init__(self, id, titulo, texto, ano, mes, dia, userid):
        self.__id = id
        self.__titulo = titulo
        self.__texto = texto
        self.__dataPublicacao = datetime.date(ano, mes, dia)
        self.__autor = userid
    
    #Gets e Sets
    def getid(self):
        return self.__id
    def setid(self, novo):
        self.__id = novo
        return self.__id
    def getsenha(self):
        return self.__senha
    def getdata(self):
        return self.__dataPublicacao
    def setdata(self):
        return self.__dataPublicacao
    def gettitulo(self):
        return self.__titulo
    def gettexto(self):
        return self.__texto
    def getautor(self):
        return self.__autor


class Blog(autenticaMixIn):

    def __init__(self):
        self.__postagens = []
        self.__postagens_publicadas = []
        self.__usuarios_autenticados = []

    #Gets e Sets
    def get_postagem(self):
        return self.__postagens
    def get_autenticados(self):
        self.__usuarios_autenticados
    def set_postagem(self, postagem):
        return self.__postagens.remove(postagem)
    def get_postagem_pub(self):
        return self.__postagens_publicadas
    def set_postagem_pub(self, postagem):
        return self.__postagens_publicadas.remove(postagem)

    def adicionarPostagem(self, postagem):
        if postagem.getautor() in self.__usuarios_autenticados:
            self.__postagens.append(postagem)
        else:
            print("Usuário não autenticado")
        return True
    
    def publicarPostagem(self, postagem):
        '''Nesse sistema, estou levando em consideração que na hora da criação da postagem
        o usário determina a data em que a postagem vai ser públicada, e não a data da sua criação'''
        if postagem in self.__postagens and postagem.getdata() <=datetime.date.today():
            self.__postagens_publicadas.append(postagem)
        return "Publicada com sucesso"
    
    def listarPostagensPublicadas(self):
        print("listar todas postagens publicadas")
       
        for p in self.__postagens_publicadas:
            if p.getdata() <= datetime.date.today():
                print(p)
    
    def listarTodasPostagens(self):
        return self.__postagens
    
    def apagarPostagem(self, postagem):
        self.set_postagem(postagem)
        self.set_postagem_pub(postagem)
        print("Postagem apagada")


    def autentica(self, user):
        login = input("Digite seu login:")
        senha = input("Digite sua senha: ")
        if user.autentica(user, login, senha):
            print("Autenticagem realizada!")
            self.__usuarios_autenticados.append(user)


    

blog1 = Blog()
usuario1 = Usuario(1,"Brenin", "login1", "123")
postagem1 = Postagem(1,"Titulo1", "Textinho", 2023,12,4, usuario1)

print("Realizando autenticagem do usuário:")
blog1.autentica(usuario1)
print("\nUsuário tentando adicionar a postagem:")
blog1.adicionarPostagem(postagem1)
print("\nVerficando se a postagem pode ser publicada:")
blog1.publicarPostagem(postagem1)
print("\nListando todas as postagens:")
print(blog1.listarTodasPostagens())
print("\nListando somente as postagens publicadas")
print(blog1.listarPostagensPublicadas())
print("\nApagando uma postagem do blog:")
blog1.apagarPostagem(postagem1)
print("\nListando novamente para conferir:")
print("Listando todas as postagens:")
print(blog1.listarTodasPostagens())
print("\nListando somente as postagens publicadas")
print(blog1.listarPostagensPublicadas())