Modelagem de Domínio e Práticas Ágeis de Software

📌 Estrutura dos Exercícios
Atividade 1: Design vs Código
Objetivo: Estruturar assinaturas do domínio e relações de multiplicidade mantendo o controle de estado coeso.

Entidades: Livro, Usuario e Emprestimo.

Conceito: Separação das fases do SDLC e preservação da coesão do objeto.

Atividade 2: Entrega Incremental
Objetivo: Fatiar o domínio comercial em unidades autônomas evitando arquiteturas monolíticas (Big Bang).

Entidades: Produto e ItemPedido.

Conceito: Encapsulamento de preços com @property e descentralização da matemática financeira no método subtotal().

Atividade 3: Validação com TDD
Objetivo: Utilizar o ciclo Red-Green-Refactor para ditar a arquitetura do código e prevenir erros em tempo de execução.

Entidade: Aluno + Suíte de testes unittest.

Conceito: Proteção contra exceções aritméticas (ZeroDivisionError) ao calcular a média acadêmica.

Atividade 4: Simplicidade e XP
Objetivo: Refatorar código procedural/monolítico para Orientação a Objetos com responsabilidade única.

Entidade: Pedido.

Conceito: Eliminação de escopo global e transição de estado sensível via método controlado atualizar_status().

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Framework de Testes: unittest (nativo do Python)

🚀 Como Executar os Testes
Para rodar os testes unitários da Atividade 3, execute o comando abaixo no terminal:
