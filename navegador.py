import os
from validar_url import validar_url

class NavegadorWebSimulado:

    def __init__(self, arquivo_urls):
        self.paginas = {
            "www.ifpb.edu.br": ["/tsi", "/rc"],
            "www.ifpb.edu.br/tsi": ["/professores", "/alunos"],
            "www.ifpb.edu.br/rc": ["/coordenacao"],
            "www.ifpb.edu.br/rc/coordenacao": ["/matriz_curricular"],
            "www.google.com.br": ["/search", "/images"],
            "www.apple.com": ["/iphone", "/mac"],
            "www.detran.pb.gov.br": ["/servicos", "/contato"],
        }
        self.historico_navegacao = []
        self.historico_completo = []
        self.home = ""
        self.url_atual = ""

        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        caminho_completo_arquivo = os.path.join(diretorio_do_script, arquivo_urls)

        self.carregar_urls_validas(caminho_completo_arquivo)

    def carregar_urls_validas(self, caminho_completo_arquivo):
        try:
            print(f"\nCarregando URLs válidas do arquivo:\n{caminho_completo_arquivo}...\n")
            with open(caminho_completo_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    url = linha.strip()
                    if validar_url(url):
                        if url not in self.paginas:
                            self.paginas[url] = []
                            print(f"URL válida carregada: {url}")
                        else:
                            print(f"URL já existe no sistema: {url}")
                    else:
                        print(f"URL inválida ignorada: {url}")
        except FileNotFoundError:
            print(f"\nErro: Arquivo '{caminho_completo_arquivo}' não encontrado.")
        except Exception as e:
            print(f"\nOcorreu um erro ao carregar URLs: {e}")

    def navegar_para(self, url):
        try:
            if url.startswith("/"):
                if self.url_atual and url in self.paginas.get(self.url_atual, []):
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                    self.url_atual += url
                    self.home = self.url_atual
                    self.exibir_links_disponiveis()
                elif self.home and url in self.paginas.get(self.home, []):
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                    self.url_atual = self.home + url
                    self.exibir_links_disponiveis()
                else:
                    print("\nPágina não encontrada!")
            elif url in self.paginas:
                if self.url_atual:
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                self.url_atual = url
                self.home = url
                self.exibir_links_disponiveis()
            else:
                print("\nPágina não encontrada!")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {str(e)}")

    def exibir_links_disponiveis(self):
        print(f"\nPágina encontrada: {self.url_atual}\n")
        print("Links disponíveis:")
        links = self.paginas.get(self.url_atual, [])
        if links:
            for link in links:
                print(f"  {link}")
        else:
            print("Nenhum link disponível.")

    def executar_comando(self, comando):
        try:
            if comando.startswith("#add "):
                url = comando.split(" ")[1]
                if validar_url(url):
                    if url not in self.paginas:
                        self.paginas[url] = []
                        print(f"\n{url} adicionado com sucesso!")
                    else:
                        print("\nA URL já existe no sistema.")
                else:
                    print("\nFormato de URL inválido!\nExemplo de formato válido: www.url.com")
            elif comando == "#back":
                if self.historico_navegacao:
                    self.url_atual = self.historico_navegacao.pop()
                    self.exibir_links_disponiveis()
                else:
                    print("\nNão há páginas anteriores.")
            elif comando == "#sair":
                print("\nFechando o navegador...\n")
                return False
            elif comando == "#showhist":
                print(f"\nHistórico completo:\n{self.historico_completo}")
            else:
                print("\nComando inválido.\n")
        except Exception as e:
            print(f"\nOcorreu um erro ao executar o comando: {str(e)}")
        return True