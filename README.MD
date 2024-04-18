# Desafio Python DB / Sicredi

## Sumário

- [Introdução](#Introdução)
- [Projeto](#Projeto)
- [Testes](#Testes)
- [Resultados](#Resultados)
- [Conclusão](#Conclusão)
- [Referências](#Referências)

## Introdução
O projeto tem como objetivo demonstrar as habilidades e conhecimentos para a vaga de Desenvolvedor Python na DB / Sicredi. O detalhamento técnico do problema e as instruções de desenvolvimento podem ser encontrados no [arquivo](TECHNICAL_CHALLENGE.md).

## Projeto
Dentro da pasta `src` tem as duas proposta de resolução dos algoritmos propostos pelo teste técnico. Contendo o melhor e o pior caso de performance.

- [Resolução questão 1 com melhor performance.](src/question1.py)
- [Resolução questão 2 com melhor performance.](src/question2.py)
- [Resolução questão 1 com pior performance.](src/worst_question1.py)
- [Resolução questão 2 com pior performance.](src/worst_question2.py)

Para rodar o projeto tem duas opções:

### 1) Poetry:

- Instale o Poetry (version 1.8.2). Caso não tenha o tutorial siga o [tutorial](https://python-poetry.org/docs/#installing-with-the-official-installer).
- Rode o comando para instalar as dependências do projeto e ativar o ambiente virtual:
```bash
poetry install
poetry shell
```

### 2) Pip-tools:

- Crie um ambiente virtual, ative o ambiente virtual e instale as dependências do projeto.
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Rode os testes unitários para as resoluções do algoritmos:
```bash
task test
```

## Testes

Os testes de desempenho foram padronizados com base na quantidade de "Contratos" e envolveram a medição do consumo de memória durante a execução do código, além do tempo necessário para a conclusão. Os testes estão localizados na pasta "scripts" e incluem informações sobre o código de teste, os resultados obtidos e as tabelas exibidas no terminal pela biblioteca responsável por medir o consumo de memória ([memory profiler](https://github.com/pythonprofilers/memory_profiler)).

Para executar os testes de performance rode o seguinte comando:

```bash
mprof run script/best_performance/question1.py
mprof run script/best_performance/question2.py
mprof run script/worst_performance/question1.py
mprof run script/worst_performance/question2.py
```

OBS: Para os comandos de `worst_performance` o tempo de execução pode chegar a 1 hora de execução.

## Resultados

Resultados dos testes para a resolução da `question1` melhor e pior performance:

| Best Memory (MiB) | Worst Memory (MiB)  | Best Time (seg) | Worst Time (seg)  | Contracts |
|-------------------|---------------------|-----------------|-------------------|-----------|
| 22.1              | 21.1                | 0.02875         | 0.34731           | 1000      |
| 22.7              | 22.8                | 0.12148         | 8.26991           | 5000      |
| 23.5              | 23.5                | 0.23698         | 32.7354           | 10000     |
| 28.9              | 29.7                | 1.19454         | 807.073           | 50000     |
| 35.1              | 36.5                | 2.34761         | 3220.42           | 100000    |

Resultados dos testes para a resolução da `question2` melhor e pior performance:

| Best Memory (MiB) | Worst Memory (MiB)  | Best Time (seg) | Worst Time (seg)  | Contracts |
|-------------------|---------------------|-----------------|-------------------|-----------|
| 21.9              | 21.9                | 0.02739         | 0.34633           | 1000      |
| 21.9              | 21.9                | 0.11780         | 8.26991           | 5000      |
| 22.3              | 22.3                | 0.23496         | 30.8287           | 10000     |
| 24.3              | 23.8                | 1.26651         | 779.166           | 50000     |
| 26.5              | 26.2                | 2.85426         | 3104.65           | 100000    |

## Conclusão

Com base nos testes realizados anteriormente, foram identificadas algumas questões relacionadas ao desempenho:

- Otimizar um algoritmo para entregar resultados com alta performance e no menor tempo possível pode reduzir os custos de operação do servidor.
- O uso de geradores em Python pode auxiliar na eficiência do tempo de execução e no gerenciamento de memória.
- Compreender como as funções internas do Python, como `sorted`, podem ser mais eficazes do que implementar algoritmos como o `bubble sort`.

Segundo Jakob Nielsen o tempo de resposta de um recurso deve seguir os critérios:

| Tempo   | Estado      | Descrição                                                                                      |
|---------|-------------|-----------------------------------------------------------------------------------------------|
| 0 a 0.1 | Perfeito    | O usuário se sente no comando e a experiência é gratificante.                                |
| 0.1 a 1 | Aceitável   | Desde que haja uma indicação do que está ocorrendo.                                          |
| 1 a 10  | Problemático | Aqui o feedback é vital, mas o usuário provavelmente tentará outra atividade.                |
| > 10    | Inviável    | A não ser que seja um fator físico ou algo do gênero, e mesmo assim não pode interromper a navegação. |

Neste exemplo, a lógica que responde à API pode demorar para fornecer uma resposta, dependendo da implementação. Os dados foram gerados a partir de uma classe `Contract`, mas em um sistema real, esses dados provavelmente viriam de um banco de dados. Saber otimizar as consultas no banco de dados e implementar os melhores algoritmos para resolver o problema pode impactar positivamente no tempo de resposta do recurso, proporcionando uma melhor experiência para o usuário final e diminuir os custos de infraestrutura.


## Referências

- [Medindo consumo de memória em Python](http://igormontagner.blogspot.com/2017/05/medindo-consumo-de-memoria-em-python.html#:~:text=A%20op%C3%A7%C3%A3o%20%2DU%20pode%20ser,usu%C3%A1rio%20em%20sistemas%20Unix%2Dlike.&text=Este%20comando%20imprime%20um%20relat%C3%B3rio,contexto%20o%20consumo%20pode%20diminuir)
- [Como tratar o tempo de resposta em aplicações web](https://brasil.uxdesign.cc/como-tratar-o-tempo-de-resposta-em-aplica%C3%A7%C3%B5es-web-e4ee7c42ebc4)
- [Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/)
- [Powers of 10: Time Scales in User Experience](https://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/)
- [Memory Profiler](https://github.com/pythonprofilers/memory_profiler)
