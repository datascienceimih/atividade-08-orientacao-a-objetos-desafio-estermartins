
"""
Ester Pereira Martins
Atividade 08 - Projeto Integrador
Jogo
"""
""" Crie outro script chamado jogo.py e nele crie três crianças de verdade (três instâncias da classe abstrata Criança).
Você deve passar na criação o nome, a idade e se a criança é ou não a pegadora.
Essas três crianças vão brincar de pegador. Programe o jogo! Pergunte o nome e a idade das crianças.
Verifique se ela é a pegadora. Use a criatividade. E acima de tudo, Divirta-se, porque programar é bom demais!!!
"""
from Crianca import crianca
from crianca import Pegador

crianca1 = Pegador('Joãozinho', 8)
crianca2 = Crianca('Maria', 9)
crianca3 = Crianca('Serjão Berranteiro', 7)

# Qual o nome de vocês?
print(crianca1.nome)
print(crianca2.nome)
print(crianca3.nome)

# Qual a idade de vocês?
print(crianca1.idade)
print(crianca2.idade)
print(crianca3.idade)

# Algum de vocês é o pegador?
print(crianca1.e_pegador)
print(crianca2.e_pegador)
print(crianca3.e_pegador)

## Let's play
crianca2.correr()
crianca1.correr()
crianca1.pegar(crianca2)
crianca2.correr()
crianca1.pegar(crianca2)
crianca3.salvar(crianca2)
crianca3.correr()
crianca1.pegar(crianca3)
crianca2.salvar(crianca3)
