def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas_turma = {}
    mediant = mennt = maint = 0
    quant_nt = len(notas)
    for nt in notas:
        mediant += nt
    
    mediant = mediant / quant_nt

    for i in range(0, quant_nt):
        if i == 0:
            mennt = maint = notas[i]
        else:
            if notas[i] > maint:
                maint = notas[i]
            if notas[i] < mennt:
                mennt = notas[i]
    
    notas_turma['total'] = quant_nt
    notas_turma['maior'] = maint
    notas_turma['menor'] = mennt
    notas_turma['média'] = mediant

    if sit:
        notas_turma['situação'] = 'Boa' if mediant >= 7 else 'Razoável' if mediant >= 5 else 'Ruim'

    return notas_turma


print(notas(8.2, 9.7, 9, 8.5, sit=True))