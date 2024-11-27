from utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$')
resumo(p, 30, 7)