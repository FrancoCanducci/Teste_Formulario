from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Caminho para o ChromeDriver
service = Service("C:/Users/franc/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Configurar o WebDriver com o caminho correto para o seu chromedriver
driver = webdriver.Chrome(service=service)

# Abrir o formulário com o caminho correto para o arquivo HTML
driver.get("file:///C:/Users/franc/Downloads/form.html")

# Função para testar o preenchimento do formulário
def testar_formulario(nome, email, email_confirm, senha):
    driver.find_element(By.ID, "nome").send_keys(nome)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "emailConfirm").send_keys(email_confirm)
    driver.find_element(By.ID, "senha").send_keys(senha)
    driver.find_element(By.XPATH, "//button[text()='Cadastrar']").click()

# Função para limpar o formulário
def limpar_formulario():
    driver.execute_script("document.getElementById('formCadastro').reset();")

# Testes de Cenários

# 1. Preencher o formulário corretamente e enviar
print("Teste 1: Preencher o formulário corretamente e enviar...")
testar_formulario("João Silva", "joao@teste.com", "joao@teste.com", "Senha123")
time.sleep(2)  # Esperar 2 segundos para visualizar a mensagem
if "Cadastro realizado com sucesso!" in driver.page_source:
    print("Resultado: Sucesso! A mensagem de sucesso foi exibida.")
else:
    print("Resultado: Falha! A mensagem de sucesso não foi exibida.")

# 2. Deixar campos obrigatórios vazios
print("\nTeste 2: Deixar campos obrigatórios vazios...")
limpar_formulario()  # Limpar o formulário
testar_formulario("", "", "", "")
time.sleep(2)
if "Todos os campos devem ser preenchidos!" in driver.page_source:
    print("Resultado: Sucesso! A mensagem de erro foi exibida.")
else:
    print("Resultado: Falha! A mensagem de erro não foi exibida.")

# 3. Digitar uma senha fraca
print("\nTeste 3: Digitar uma senha fraca...")
limpar_formulario()  # Limpar o formulário
testar_formulario("João Silva", "joao@teste.com", "joao@teste.com", "12345")
time.sleep(2)
if "A senha deve ter no mínimo 8 caracteres" in driver.page_source:
    print("Resultado: Sucesso! A mensagem de erro foi exibida.")
else:
    print("Resultado: Falha! A mensagem de erro não foi exibida.")

# 4. Digitar e-mails diferentes nos campos de "E-mail" e "Confirmação de E-mail"
print("\nTeste 4: Digitar e-mails diferentes nos campos de 'E-mail' e 'Confirmação de E-mail'...")
limpar_formulario()  # Limpar o formulário
testar_formulario("João Silva", "joao@teste.com", "diferente@teste.com", "Senha123")
time.sleep(2)
if "Os e-mails não coincidem!" in driver.page_source:
    print("Resultado: Sucesso! A mensagem de erro foi exibida.")
else:
    print("Resultado: Falha! A mensagem de erro não foi exibida.")

# Fechar o navegador
driver.quit()
