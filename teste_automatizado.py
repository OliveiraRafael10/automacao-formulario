"""
TESTE AUTOMATIZADO DE FORMULÁRIO WEB COM SELENIUM
Apresentação Acadêmica - Automação de Testes

Este script demonstra como automatizar testes de formulários web usando Python e Selenium.
Os dados de teste são carregados de um arquivo externo (dados_teste.txt).

"""

# ==================== IMPORTAÇÕES ====================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# ==================== CLASSE PRINCIPAL ====================
class BotTestadorFormulario:
    """Classe que automatiza os testes do formulário"""
    
    def __init__(self):
        """Inicializa o testador"""
        # Caminhos dos arquivos
        self.diretorio = os.path.dirname(os.path.abspath(__file__))
        self.caminho_html = os.path.join(self.diretorio, 'formulario.html')
        self.caminho_dados = os.path.join(self.diretorio, 'dados_teste.txt')
        
        # Navegador Selenium
        self.driver = None
        
        # Lista para armazenar resultados
        self.resultados = []
    
    # ========== CARREGAR DADOS DO ARQUIVO ==========
    def carregar_dados_teste(self):
        """Lê o arquivo dados_teste.txt e retorna lista de cenários"""
        
        cenarios = []
        cenario_atual = {}
        
        # Abre o arquivo
        with open(self.caminho_dados, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                
                # Ignora linhas vazias e comentários (#)
                if not linha or linha.startswith('#'):
                    continue
                
                # Separador de cenários (---)
                if linha == '---':
                    if cenario_atual:
                        cenarios.append(cenario_atual)
                        cenario_atual = {}
                    continue
                
                # Lê dados no formato: chave=valor
                if '=' in linha:
                    chave, valor = linha.split('=', 1)
                    cenario_atual[chave.strip()] = valor.strip()
        
        # Adiciona o último cenário
        if cenario_atual:
            cenarios.append(cenario_atual)
        
        print(f"✓ {len(cenarios)} cenários carregados\n")
        return cenarios
    
    # ========== CONFIGURAR NAVEGADOR ==========
    def configurar_driver(self):
        """Inicia o navegador Chrome"""
        
        self.driver = webdriver.Chrome()
        print("✓ Navegador Chrome iniciado\n")
    
    # ========== ABRIR PÁGINA DO FORMULÁRIO ==========
    def abrir_pagina(self):
        """Abre o formulário HTML no navegador"""
        
        # Converte caminho para URL: file:///C:/...
        url = f"file:///{self.caminho_html.replace(os.sep, '/')}"
        self.driver.get(url)
        
        print(f"✓ Formulário aberto\n")
        time.sleep(2)
    
    # ========== PREENCHER CAMPO ==========
    def preencher_campo(self, id_campo, valor):
        """Localiza um campo e preenche com o valor"""
        
        # Localiza o campo pelo ID
        campo = self.driver.find_element(By.ID, id_campo)
        
        # Limpa o campo
        campo.clear()
        # Preenche o campo com o valor
        campo.send_keys(valor)
        
        print(f"  ✓ {id_campo}: {valor}")
    
    # ========== CLICAR NO BOTÃO ==========
    def clicar_botao(self):
        """Clica no botão Cadastrar"""
        
        botao = self.driver.find_element(By.ID, 'btnEnviar')
        botao.click()
        
        print("  ✓ Botão clicado")
        time.sleep(2)
    
    # ========== VERIFICAR MENSAGEM DE SUCESSO ==========
    def verificar_sucesso(self):
        """Verifica se a mensagem de sucesso apareceu"""
        
        # Aguarda a mensagem aparecer (máximo 5 segundos)
        mensagem = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'mensagemSucesso'))
        )
        
        print(f"  ✓ Sucesso: {mensagem.text}\n")
        return True
    
    # ========== EXECUTAR TESTE COMPLETO ==========
    def executar_teste(self, dados):
        """Executa um teste completo: preencher e validar"""
        
        print(f"{'='*60}")
        print(f"🧪 TESTE: {dados['nome']}")
        print(f"{'='*60}\n")
        
        # Preenche todos os campos
        print("📝 Preenchendo formulário...")
        self.preencher_campo('nome', dados['nome'])
        self.preencher_campo('email', dados['email'])
        self.preencher_campo('telefone', dados['telefone'])
        self.preencher_campo('senha', dados['senha'])
        self.preencher_campo('confirmarSenha', dados['confirmarSenha'])
        
        # Envia o formulário
        print("\n📤 Enviando...")
        self.clicar_botao()
        
        # Verifica sucesso
        print("✅ Verificando...")
        self.verificar_sucesso()
    
    # ========== FECHAR NAVEGADOR ==========
    def fechar(self):
        """Fecha o navegador"""
        self.driver.quit()
        print("🔒 Navegador fechado")


# ==================== FUNÇÃO PRINCIPAL ====================
def main():
    """Função que executa todos os testes"""
    
    print("\n" + "="*60)
    print("  SISTEMA DE TESTES AUTOMATIZADOS - SELENIUM")
    print("="*60 + "\n")
    
    # 1. Criar bot
    bot = BotTestadorFormulario()
    
    try:
        # 2. Iniciar navegador
        bot.configurar_driver()
        
        # 3. Abrir formulário
        bot.abrir_pagina()
        
        # 4. Carregar dados do arquivo
        print("📂 Carregando dados de teste...")
        cenarios = bot.carregar_dados_teste()
        
        # 5. Executar cada cenário
        for i, dados in enumerate(cenarios, 1):
            print(f"\n[CENÁRIO {i}/{len(cenarios)}]\n")
            bot.executar_teste(dados)
            time.sleep(2)  # Pausa entre testes
        
        # 6. Mensagem final
        print("\n" + "="*60)
        print(f"✓ {len(cenarios)} testes executados com sucesso!")
        print("="*60 + "\n")
        
        # Aguarda 5 segundos antes de fechar
        time.sleep(5)
        
    except Exception as erro:
        print(f"\n✗ Erro: {erro}\n")
    
    finally:
        # Sempre fecha o navegador
        bot.fechar()


# ==================== EXECUTAR ====================
if __name__ == "__main__":
    main()

