class User:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def set_name(self):
        self.name = input('Nome completo: ')

    def set_password(self):
        self.password = input('Senha: ')

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
    usuario.set_password()
    usuario.set_role()
    print('Usuário criado com sucesso!')
    print('LOGIN')
    i = 1
    while i == 1:
        nameverify = input('Insira o nome de usuário: ')
        if nameverify == usuario.name:
            i = 2
            while i == 2:
                passwordverify = input('Insira a senha de usuário: ')
                if passwordverify == usuario.password:
                    usuario.greet()
                    i = 3
                else:
                    print('Senha incorreta. Tente novamente.')
        else:
            print('Usuário não encontrado. Tente novamente.')

except ValueError:
    print('Deve-se inserir um número.')
