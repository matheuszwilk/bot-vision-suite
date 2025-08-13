# Changelog - Bot Vision Suite

## [1.0.4] - 2025-08-13

### 🚀 Melhorias Importantes

#### Overlay System - Correção Crítica
- **✅ Detecção Dinâmica de TCL/TK**: Substituída busca por caminhos hardcoded por detecção automática
- **🌍 Compatibilidade Universal**: Agora funciona em qualquer versão do Python e tipo de ambiente
- **🔧 Suporte a Ambientes Virtuais**: Detecta automaticamente venv, conda, virtualenv
- **📦 Busca Inteligente**: Usa glob patterns para encontrar TCL/TK dinamicamente
- **🛡️ Fallback Robusto**: Múltiplos métodos de fallback para garantir funcionamento

#### Problemas Resolvidos
- ❌ **ANTES**: Caminhos fixos como `C:\Program Files\Python313\tcl` não funcionavam em venv
- ✅ **AGORA**: Detecta automaticamente qualquer instalação Python e versão TCL/TK
- ❌ **ANTES**: Falhava em instalações customizadas ou versões diferentes do Python  
- ✅ **AGORA**: Funciona universalmente em qualquer ambiente Python

#### Detalhes Técnicos
```python
# ANTES (problemático)
tcl_paths = [
    r'C:\Program Files\Python313\tcl',  # Muito específico
    r'C:\Program Files\Python312\tcl',  # Só versões específicas
]

# AGORA (dinâmico)
python_installs = glob.glob(os.path.join(pf, 'Python*'))
tcl_patterns = [
    os.path.join(base_dir, 'tcl*'),     # Qualquer versão TCL
    os.path.join(base_dir, 'Library', 'lib', 'tcl*'),  # Conda
]
```

### 🎯 Impacto
- **Usuários de venv/conda**: Overlay agora funciona corretamente
- **Diferentes versões Python**: Suporte automático para 3.8, 3.9, 3.10, 3.11, 3.12, 3.13+
- **Instalações customizadas**: Detecta automaticamente qualquer local de instalação

---

## [1.0.3] - 2025-08-13

### Correções
- Corrigido erro de sintaxe em overlay.py
- Melhorada estabilidade do sistema de overlay

## [1.0.2] - 2025-08-13

### Correções  
- Corrigida função `click_relative_image` para retornar coordenadas corretas
- Melhorada documentação de uso

## [1.0.1] - 2025-08-13

### Correções
- Corrigido problema de importação de submódulos
- Adicionado `[tool.setuptools.packages.find]` ao pyproject.toml

## [1.0.0] - 2025-08-13

### 🎉 Primeira Versão
- Lançamento inicial da biblioteca Bot Vision Suite
- Automação visual com OCR
- Sistema de overlay para feedback visual
- Detecção de texto e imagens na tela
- Simulação de cliques e comandos de teclado
