import bcrypt

class User:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role


    def set_name(self):
        #nameprototype = input('Nome completo: ')
        max_length = 30
        n = 1
        while n == 1:
            nameprototype = input('Nome completo: ')
            if len(nameprototype) > max_length:
                print('O nome deve possuir no máximo 30 caracteres.')
            else:
                n = 2
        if nameprototype[0].isnumeric() == False:
            if nameprototype[0].isupper() == True:
                pass
            else:
                raise Exception('A primeira letra dos nomes deve ser maiúscula.')
        else:
            raise TypeError('O nome deve ser composto apenas por letras.')
        i = 0
        for i in range(0, len(nameprototype)):
            if nameprototype[i].isnumeric() == False:
                if nameprototype[i] == ' ' and i != (len(nameprototype)-1) and nameprototype[i + 1] != ' ' and nameprototype[i + 1].isupper() == False:
                    raise Exception('A primeira letra dos nomes deve ser maiúscula.')
                if nameprototype[i] == ' ' and i != (len(nameprototype)-1) and nameprototype[i + 1] == ' ':
                    raise IndexError('Evite espaços desnecessários.')
                elif nameprototype[i] == ' ' and i == (len(nameprototype)-1):
                    raise IndexError('Evite espaços desnecessários.')
            else:
                raise TypeError('O nome deve ser composto apenas por letras.')
            i = i + 1
        self.name = nameprototype

    def set_password(self):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(input('Senha: ').encode('utf-8'), salt)
        return salt

    def set_role(self):
        print('[1] Administrador; [2] Moderador; [3] Usuário')
        i = 1
        while i == 1:
            rolenumber = int(input('Insira o número do cargo: '))
            if rolenumber == 1:
                self.role = 'Administrador'
                i = 2
            elif rolenumber == 2:
                self.role = 'Moderador'
                i = 2
            elif rolenumber == 3:
                self.role = 'Usuário'
                i = 2
            else:
                print('Insira um número dentre 1, 2 e 3.')

    def greet(self):
        print(f'Olá, [{self.role}] {self.name}!')

try:
    print('Insira as seguintes informações para criar um usuário.')
    usuario = User('placeHolder', 'placeHolder', 'placeHolder')
    usuario.set_name()
    salt = usuario.set_password()
    usuario.set_role()
    print('Usuário criado com sucesso!')
    print('LOGIN')
    i = 1
    while i == 1:
        nameverify = input('Insira o nome de usuário: ')
        if nameverify == usuario.name:
            i = 2
            while i == 2:
                passwordverify = bcrypt.hashpw(input('Insira a senha de usuário: ').encode('utf-8'), salt)
                if passwordverify == usuario.password:
                    usuario.greet()
                    i = 3
                else:
                    print('Senha incorreta. Tente novamente.')
        else:
            print('Usuário não encontrado. Tente novamente.')

except ValueError:
    print('Deve-se inserir um número.')
