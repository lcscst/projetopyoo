def exibir_interface(historico_navegacao, url_atual):
    print(f"\nHistórico de visitas: {historico_navegacao}")
    print(f"Página atual: [{url_atual}]")
    print("Digite a URL, #back para retornar, #add <url> para adicionar, #showhist para mostrar o histórico, ou #sair.")
    url = input("\nurl: ").strip()
    return url