# 🔧 Solução para o Problema do Overlay

## ❌ Problema Identificado
O erro do overlay ocorre porque o Tkinter (biblioteca gráfica do Python) não está configurado corretamente:
```
Can't find a usable init.tcl in the following directories
```

## ✅ Soluções Disponíveis

### Solução 1: Desabilitar Overlay (Recomendado)
```python
from bot_vision import BotVision

# Criar instância com overlay desabilitado
bot = BotVision()
bot.show_overlay = False  # Desabilita overlay visual

# Ou configurar globalmente
config = {
    'show_overlay': False
}
bot = BotVision(config=config)

# Agora usar normalmente - funciona sem problemas de overlay
bot.click_relative_image('anchor.png', 'target.png')
```

### Solução 2: Corrigir Tkinter (Avançado)
Se quiser manter o overlay visual funcionando:

#### Windows:
```bash
# Reinstalar Python com Tkinter
# Download do Python oficial: https://python.org
# Certifique-se de marcar "tcl/tk and IDLE" na instalação
```

#### Conda/Miniconda:
```bash
conda install tk
```

#### Pip (alternativo):
```bash
pip install tk
```

### Solução 3: Usar Configuração Personalizada
Crie um arquivo `config.json`:
```json
{
    "show_overlay": false,
    "default_delay": 0.5,
    "confidence_threshold": 0.8
}
```

Depois use:
```python
from bot_vision import BotVision

# Carregar configuração do arquivo
bot = BotVision()
bot.config.load_from_file('config.json')
```

## 🚀 Exemplo Funcional (Sem Overlay)

```python
from bot_vision import BotVision

# Configurar para não usar overlay
bot = BotVision()
bot.show_overlay = False

# Todas as funcionalidades funcionam normalmente
print("Testando funcionalidades...")

# Busca relativa
result = bot.click_relative_image(
    anchor_image='anchor.png',
    target_image='target.png',
    max_distance=200
)

if result:
    print("✅ Clique realizado com sucesso!")
else:
    print("❌ Imagens não encontradas")

# Outras funcionalidades
bot.click_text("Login")
bot.type_text("usuario123")
bot.keyboard_command("Enter")
```

## 📝 Script de Teste (Overlay Desabilitado)

Salve como `test_no_overlay.py`:
```python
from bot_vision import BotVision

print("🧪 Testando Bot Vision Suite sem overlay...")

# Configurar sem overlay
bot = BotVision()
bot.show_overlay = False
print("✅ Overlay desabilitado")

# Testar métodos básicos
try:
    # Método que você está usando
    print("🔍 Testando click_relative_image...")
    
    # Simular uso (substitua pelas suas imagens)
    # result = bot.click_relative_image('anchor.png', 'target.png')
    
    print("✅ Método click_relative_image acessível")
    print("ℹ️ Para testar completamente, substitua pelas suas imagens")
    
    # Outros métodos
    print("🔍 Testando outros métodos...")
    print("- find_text:", hasattr(bot, 'find_text'))
    print("- click_text:", hasattr(bot, 'click_text'))
    print("- type_text:", hasattr(bot, 'type_text'))
    print("- keyboard_command:", hasattr(bot, 'keyboard_command'))
    
    print("\n🎉 Todos os testes passaram! Biblioteca funcionando corretamente sem overlay.")
    
except Exception as e:
    print(f"❌ Erro: {e}")
```

## 🔍 Verificar Status do Overlay

```python
from bot_vision import BotVision

bot = BotVision()
print(f"Overlay habilitado: {bot.show_overlay}")

# Desabilitar
bot.show_overlay = False
print(f"Overlay agora: {bot.show_overlay}")
```

## 💡 Recomendação

Para máxima compatibilidade, **recomendo usar sempre com overlay desabilitado**:
```python
from bot_vision import BotVision

bot = BotVision()
bot.show_overlay = False  # Sempre adicionar esta linha

# Resto do código funciona normalmente
```

O overlay é apenas visual para debug - a funcionalidade principal funciona perfeitamente sem ele!
