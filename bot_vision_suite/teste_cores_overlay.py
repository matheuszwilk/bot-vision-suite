"""
🌈 Teste de Cores do Overlay - Bot Vision Suite

Script para testar visualmente todas as cores disponíveis.
"""

def main():
    print("🌈 TESTE DE CORES DO OVERLAY")
    print("=" * 50)
    
    try:
        from bot_vision import BotVision
        
        # Listar cores
        cores = BotVision.get_available_overlay_colors()
        print(f"📋 {len(cores)} cores disponíveis:")
        for i, cor in enumerate(cores, 1):
            print(f"   {i:2d}. {cor.upper()}")
        
        print("\n" + "=" * 50)
        print("👁️ TESTE VISUAL")
        print("=" * 50)
        print("Este teste mostrará cada cor por 2 segundos.")
        print("Olhe para o centro da tela!")
        
        resposta = input("\nPressione ENTER para começar o teste visual (ou 'n' para pular): ")
        
        if resposta.lower() not in ['n', 'no', 'nao', 'não']:
            bot = BotVision()
            bot.test_overlay_colors(duration=2000)
        
        print("\n" + "=" * 50)
        print("🔧 EXEMPLOS DE CONFIGURAÇÃO")
        print("=" * 50)
        
        exemplos = [
            ("Vermelho Clássico", {"color": "red", "duration": 1000, "width": 4}),
            ("Azul Profissional", {"color": "blue", "duration": 1500, "width": 6}),
            ("Verde Sucesso", {"color": "green", "duration": 1200, "width": 5}),
            ("Amarelo Atenção", {"color": "yellow", "duration": 2000, "width": 8}),
            ("Roxo Criativo", {"color": "purple", "duration": 1800, "width": 7}),
        ]
        
        for nome, config in exemplos:
            print(f"\n📌 {nome}:")
            print(f"   bot = BotVision()")
            print(f"   bot.configure_overlay(**{config})")
            
            # Testar configuração
            try:
                bot = BotVision()
                bot.configure_overlay(**config)
                atual = bot.get_overlay_config()
                print(f"   ✅ Configurado: cor={atual['color']}, duração={atual['duration']}ms, largura={atual['width']}")
            except Exception as e:
                print(f"   ❌ Erro: {e}")
        
        print("\n" + "=" * 50)
        print("🚀 TESTE INTERATIVO")
        print("=" * 50)
        
        while True:
            print("\nEscolha uma opção:")
            print("1. Testar cor específica")
            print("2. Configuração personalizada") 
            print("3. Listar cores disponíveis")
            print("4. Sair")
            
            opcao = input("\nOpção (1-4): ").strip()
            
            if opcao == "1":
                print("\nCores disponíveis:")
                for i, cor in enumerate(cores, 1):
                    print(f"   {i}. {cor}")
                
                try:
                    escolha = input("\nDigite o nome da cor: ").strip().lower()
                    if escolha in cores:
                        print(f"🎨 Testando cor '{escolha}' por 2 segundos...")
                        bot = BotVision()
                        bot.configure_overlay(color=escolha, duration=2000, width=6)
                        
                        # Mostrar overlay de teste
                        from bot_vision.core.overlay import VisualOverlay
                        overlay = VisualOverlay(color=escolha, width=6, duration=2000)
                        overlay.show((400, 300, 200, 100), blocking=True)
                        
                        print(f"✅ Teste da cor '{escolha}' concluído!")
                    else:
                        print(f"❌ Cor '{escolha}' não encontrada!")
                except Exception as e:
                    print(f"❌ Erro: {e}")
            
            elif opcao == "2":
                try:
                    print("\n🔧 Configuração Personalizada:")
                    cor = input("Cor (red/blue/green/etc): ").strip().lower()
                    duracao = int(input("Duração em ms (ex: 1500): ").strip())
                    largura = int(input("Largura da linha (ex: 6): ").strip())
                    
                    bot = BotVision()
                    bot.configure_overlay(color=cor, duration=duracao, width=largura)
                    
                    print(f"✅ Configurado: {cor}, {duracao}ms, largura {largura}")
                    
                    teste = input("Testar agora? (s/n): ").strip().lower()
                    if teste in ['s', 'sim', 'y', 'yes']:
                        from bot_vision.core.overlay import VisualOverlay
                        overlay = VisualOverlay(color=cor, width=largura, duration=duracao)
                        overlay.show((400, 300, 200, 100), blocking=True)
                        print("✅ Teste concluído!")
                        
                except ValueError as e:
                    print(f"❌ Erro de validação: {e}")
                except Exception as e:
                    print(f"❌ Erro: {e}")
            
            elif opcao == "3":
                print(f"\n🌈 {len(cores)} cores disponíveis:")
                for i, cor in enumerate(cores, 1):
                    print(f"   {i:2d}. {cor.upper()}")
            
            elif opcao == "4":
                break
            
            else:
                print("❌ Opção inválida!")
        
        print("\n🎉 Teste concluído!")
        print("✅ Agora você pode usar qualquer uma das cores disponíveis!")
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("💡 Certifique-se de que o bot_vision está instalado")
    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main()
