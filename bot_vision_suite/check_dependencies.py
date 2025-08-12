#!/usr/bin/env python3
"""
Script de verificação das dependências do Bot Vision Suite.

Este script verifica se todas as dependências necessárias estão instaladas
com as versões corretas.
"""

import sys
import importlib
import pkg_resources

# Dependências obrigatórias com versões específicas
REQUIRED_PACKAGES = {
    "PyAutoGUI": "0.9.54",
    "numpy": "1.26.4", 
    "opencv-python": "4.9.0.80",
    "pytesseract": None,  # Sem versão específica
    "pyperclip": None,    # >= 1.8.2
    "Pillow": None,       # >= 10.0.0
}

# Dependências opcionais
OPTIONAL_PACKAGES = {
    "keyboard": "0.13.5",
    "MouseInfo": "0.1.3",
    "pandas": None,
    "openai": None,
    "webdriver-manager": None,
}

def check_package(package_name, expected_version=None):
    """
    Verifica se um package está instalado e opcionalmente sua versão.
    
    Args:
        package_name (str): Nome do package
        expected_version (str, optional): Versão esperada
        
    Returns:
        tuple: (is_installed, current_version, version_match)
    """
    try:
        # Tenta importar o package
        if package_name == "opencv-python":
            import cv2
            installed_version = cv2.__version__
        elif package_name == "PyAutoGUI":
            import pyautogui
            installed_version = pyautogui.__version__
        elif package_name == "Pillow":
            import PIL
            installed_version = PIL.__version__
        else:
            module = importlib.import_module(package_name.lower().replace("-", "_"))
            installed_version = getattr(module, '__version__', 'unknown')
        
        # Verifica versão se especificada
        if expected_version:
            version_match = installed_version == expected_version
        else:
            version_match = True
            
        return True, installed_version, version_match
        
    except ImportError:
        return False, None, False
    except Exception as e:
        return False, str(e), False

def main():
    """Função principal de verificação."""
    print("=" * 60)
    print("BOT VISION SUITE - VERIFICAÇÃO DE DEPENDÊNCIAS")
    print("=" * 60)
    
    all_good = True
    
    # Verifica dependências obrigatórias
    print("\n📦 DEPENDÊNCIAS OBRIGATÓRIAS:")
    print("-" * 40)
    
    for package, expected_version in REQUIRED_PACKAGES.items():
        is_installed, current_version, version_match = check_package(package, expected_version)
        
        if is_installed:
            if expected_version and version_match:
                status = "✅ OK"
                print(f"{package:15} | {current_version:10} | {status}")
            elif expected_version and not version_match:
                status = f"⚠️  Versão incorreta (esperada: {expected_version})"
                print(f"{package:15} | {current_version:10} | {status}")
                all_good = False
            else:
                status = "✅ OK"
                print(f"{package:15} | {current_version:10} | {status}")
        else:
            status = "❌ NÃO INSTALADO"
            print(f"{package:15} | {'N/A':10} | {status}")
            all_good = False
    
    # Verifica dependências opcionais
    print("\n📦 DEPENDÊNCIAS OPCIONAIS:")
    print("-" * 40)
    
    for package, expected_version in OPTIONAL_PACKAGES.items():
        is_installed, current_version, version_match = check_package(package, expected_version)
        
        if is_installed:
            if expected_version and version_match:
                status = "✅ OK"
            elif expected_version and not version_match:
                status = f"⚠️  Versão incorreta (esperada: {expected_version})"
            else:
                status = "✅ OK"
            print(f"{package:15} | {current_version:10} | {status}")
        else:
            status = "⚪ Opcional - não instalado"
            print(f"{package:15} | {'N/A':10} | {status}")
    
    # Verifica se o Bot Vision Suite pode ser importado
    print("\n🤖 BOT VISION SUITE:")
    print("-" * 40)
    
    try:
        from _bot_vision import BotVision, execute_tasks, click_images
        print("bot_vision       | Importado  | ✅ OK")
        
        # Testa inicialização básica
        bot = BotVision()
        print("BotVision()      | Instancia  | ✅ OK")
        
    except ImportError as e:
        print(f"bot_vision       | Error      | ❌ ERRO: {e}")
        all_good = False
    except Exception as e:
        print(f"bot_vision       | Error      | ❌ ERRO: {e}")
        all_good = False
    
    # Resultado final
    print("\n" + "=" * 60)
    if all_good:
        print("🎉 TODAS AS DEPENDÊNCIAS OBRIGATÓRIAS ESTÃO OK!")
        print("✅ Bot Vision Suite está pronto para uso.")
    else:
        print("❌ ALGUMAS DEPENDÊNCIAS OBRIGATÓRIAS ESTÃO FALTANDO OU INCORRETAS!")
        print("\nPara instalar as dependências corretas, execute:")
        print("pip install PyAutoGUI==0.9.54 numpy==1.26.4 opencv-python==4.9.0.80")
        print("pip install pytesseract pyperclip Pillow")
    
    print("=" * 60)
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
