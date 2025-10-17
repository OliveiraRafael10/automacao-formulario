# Teste Automatizado de Formulário Web com Selenium

Projeto de automação de testes para formulários web utilizando Python e Selenium WebDriver.

## Descrição

Este projeto demonstra como automatizar o teste de um formulário de cadastro HTML utilizando Selenium. O script Python preenche automaticamente os campos do formulário com dados carregados de um arquivo de texto, simula o envio e valida se o cadastro foi bem-sucedido.

## Estrutura do Projeto

```
TesteFormSelenium/
├── formulario.html          # Página HTML com o formulário de cadastro
├── styles.css               # Estilos CSS para o formulário
├── script.js                # Script JavaScript do formulário
├── teste_automatizado.py    # Script Python com os testes automatizados
├── dados_teste.txt          # Arquivo com cenários de teste
├── requirements.txt         # Dependências Python do projeto
└── venv/                    # Ambiente virtual Python
```

## Requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone ou baixe este repositório

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

Execute o script de teste automatizado:

```bash
python teste_automatizado.py
```

O script irá:
1. Abrir o navegador Chrome
2. Carregar o formulário HTML
3. Executar todos os cenários de teste do arquivo `dados_teste.txt`
4. Preencher o formulário automaticamente
5. Validar se a mensagem de sucesso aparece
6. Fechar o navegador ao final

## Formulário de Cadastro

O formulário contém os seguintes campos:
- Nome Completo (mínimo 10 caracteres)
- E-mail (validação de formato)
- Telefone (formato brasileiro)
- Senha (mínimo 6 caracteres)
- Confirmar Senha (deve ser igual à senha)

## Arquivo de Dados de Teste

O arquivo `dados_teste.txt` contém os cenários de teste no formato:

```
nome=João Pedro Oliveira
email=joao.pedro@example.com
telefone=(11) 99876-5432
senha=Senha@2024
confirmarSenha=Senha@2024
---
```

- Use `---` para separar diferentes cenários
- Linhas iniciadas com `#` são comentários
- Formato: `chave=valor`

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação
- **Selenium WebDriver**: Automação de navegadores
- **WebDriver Manager**: Gerenciamento automático de drivers do Chrome
- **HTML/CSS/JavaScript**: Interface do formulário

## Funcionalidades do Script

- Carregamento automático de múltiplos cenários de teste
- Preenchimento automático de formulários
- Validação de mensagens de sucesso
- Relatório de execução no console
- Espera inteligente de elementos (WebDriverWait)

## Personalização

Para adicionar novos testes, edite o arquivo `dados_teste.txt` e adicione novos cenários seguindo o formato existente.

## Observações

- O navegador Chrome será aberto automaticamente durante os testes
- Aguarde a conclusão de todos os testes antes de fechar manualmente
- Os testes incluem pausas estratégicas para visualização do processo
- Certifique-se de que o Google Chrome está instalado no sistema

## Autor

Projeto desenvolvido para fins acadêmicos e demonstração de automação de testes.

