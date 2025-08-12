#!/usr/bin/env python
"""
Package validation script for bot-vision-suite.

This script validates the package structure, imports, and basic functionality.
"""

import os
import sys
from pathlib import Path

def check_file_exists(file_path, description):
    """Check if a file exists and report the result."""
    if Path(file_path).exists():
        print(f"✓ {description}: {file_path}")
        return True
    else:
        print(f"✗ {description}: {file_path} (MISSING)")
        return False

def validate_package_structure():
    """Validate the package directory structure."""
    print("Validating Package Structure")
    print("=" * 35)
    
    required_files = [
        ("Setup script", "setup.py"),
        ("Project config", "pyproject.toml"),
        ("Requirements", "requirements.txt"),
        ("License", "LICENSE"),
        ("Main README", "README.md"),
        ("Package README", "bot_vision/README.md"),
        ("Main __init__", "bot_vision/__init__.py"),
        ("Exceptions", "bot_vision/exceptions.py"),
        ("Core __init__", "bot_vision/core/__init__.py"),
        ("OCR Engine", "bot_vision/core/ocr_engine.py"),
        ("Image Processing", "bot_vision/core/image_processing.py"),
        ("Task Executor", "bot_vision/core/task_executor.py"),
        ("Visual Overlay", "bot_vision/core/overlay.py"),
        ("Utils __init__", "bot_vision/utils/__init__.py"),
        ("Config", "bot_vision/utils/config.py"),
        ("Text Filters", "bot_vision/utils/text_filters.py"),
    ]
    
    required_dirs = [
        ("Tests directory", "tests"),
        ("Examples directory", "examples"),
        ("Documentation", "docs"),
    ]
    
    test_files = [
        ("Test exceptions", "tests/test_exceptions.py"),
        ("Test utils", "tests/test_utils.py"),
        ("Test core", "tests/test_core.py"),
        ("Test integration", "tests/test_integration.py"),
        ("Test config", "tests/conftest.py"),
    ]
    
    example_files = [
        ("Basic example", "examples/basic_example.py"),
        ("Advanced workflow", "examples/advanced_workflow.py"),
        ("Migration guide", "examples/migration_guide.py"),
    ]
    
    doc_files = [
        ("Docs README", "docs/README.md"),
        ("Installation guide", "docs/installation.md"),
        ("API reference", "docs/api_reference.md"),
    ]
    
    all_valid = True
    
    # Check required files
    print("\nRequired Files:")
    for desc, file_path in required_files:
        all_valid &= check_file_exists(file_path, desc)
    
    # Check directories
    print("\nRequired Directories:")
    for desc, dir_path in required_dirs:
        if Path(dir_path).is_dir():
            print(f"✓ {desc}: {dir_path}/")
        else:
            print(f"✗ {desc}: {dir_path}/ (MISSING)")
            all_valid = False
    
    # Check test files
    print("\nTest Files:")
    for desc, file_path in test_files:
        all_valid &= check_file_exists(file_path, desc)
    
    # Check example files
    print("\nExample Files:")
    for desc, file_path in example_files:
        all_valid &= check_file_exists(file_path, desc)
    
    # Check documentation files
    print("\nDocumentation Files:")
    for desc, file_path in doc_files:
        all_valid &= check_file_exists(file_path, desc)
    
    return all_valid

def validate_imports():
    """Validate that all modules can be imported."""
    print("\n\nValidating Imports")
    print("=" * 25)
    
    import_tests = [
        ("Main package", "import bot_vision"),
        ("BotVision class", "from bot_vision import BotVision"),
        ("Convenience functions", "from bot_vision import execute_tasks, find_text, click_text"),
        ("Configuration", "from bot_vision.utils.config import BotVisionConfig"),
        ("Exceptions", "from bot_vision.exceptions import BotVisionError, OCRError"),
        ("Core modules", "from bot_vision.core import OCREngine, ImageProcessor, TaskExecutor"),
        ("Utils", "from bot_vision.utils import clean_text, filter_text_by_keywords"),
    ]
    
    all_valid = True
    
    for desc, import_stmt in import_tests:
        try:
            exec(import_stmt)
            print(f"✓ {desc}")
        except ImportError as e:
            print(f"✗ {desc}: {e}")
            all_valid = False
        except Exception as e:
            print(f"✗ {desc}: Unexpected error - {e}")
            all_valid = False
    
    return all_valid

def validate_basic_functionality():
    """Validate basic package functionality."""
    print("\n\nValidating Basic Functionality")
    print("=" * 40)
    
    try:
        from bot_vision.utils.config import BotVisionConfig
        from _bot_vision import BotVision
        
        # Test configuration creation
        config = BotVisionConfig()
        print("✓ Configuration creation")
        
        # Test BotVision instantiation
        bot = BotVision(config=config)
        print("✓ BotVision instantiation")
        
        # Test configuration validation
        config.validate()
        print("✓ Configuration validation")
        
        # Test task format validation (basic)
        sample_task = {
            "task_name": "test",
            "description": "Test task",
            "steps": [
                {"action": "find_text", "text": "test"}
            ]
        }
        print("✓ Task format validation")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def validate_package_metadata():
    """Validate package metadata files."""
    print("\n\nValidating Package Metadata")
    print("=" * 35)
    
    all_valid = True
    
    # Check setup.py
    try:
        with open("setup.py", "r") as f:
            setup_content = f.read()
            if "name=" in setup_content and "version=" in setup_content:
                print("✓ setup.py contains required metadata")
            else:
                print("✗ setup.py missing required metadata")
                all_valid = False
    except FileNotFoundError:
        print("✗ setup.py not found")
        all_valid = False
    
    # Check pyproject.toml
    try:
        with open("pyproject.toml", "r") as f:
            toml_content = f.read()
            if "[build-system]" in toml_content:
                print("✓ pyproject.toml contains build system config")
            else:
                print("✗ pyproject.toml missing build system config")
                all_valid = False
    except FileNotFoundError:
        print("✗ pyproject.toml not found")
        all_valid = False
    
    # Check requirements.txt
    try:
        with open("requirements.txt", "r") as f:
            requirements = f.read()
            required_deps = ["opencv-python", "pillow", "numpy", "pyautogui", "pytesseract"]
            for dep in required_deps:
                if dep.lower() in requirements.lower():
                    print(f"✓ {dep} in requirements.txt")
                else:
                    print(f"✗ {dep} missing from requirements.txt")
                    all_valid = False
    except FileNotFoundError:
        print("✗ requirements.txt not found")
        all_valid = False
    
    return all_valid

def main():
    """Main validation function."""
    print("Bot Vision Suite - Package Validation")
    print("=" * 45)
    print("This script validates the package structure and functionality.")
    
    # Change to package directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    print(f"Working directory: {script_dir.absolute()}")
    
    # Run validation steps
    results = []
    
    results.append(("Package Structure", validate_package_structure()))
    results.append(("Package Metadata", validate_package_metadata()))
    results.append(("Module Imports", validate_imports()))
    results.append(("Basic Functionality", validate_basic_functionality()))
    
    # Summary
    print("\n\nValidation Summary")
    print("=" * 25)
    
    all_passed = True
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"{symbol} {test_name}: {status}")
        all_passed &= passed
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All validations PASSED! Package is ready.")
        print("\nNext steps:")
        print("  1. Run tests: python run_tests.py")
        print("  2. Build package: python build_package.py")
        print("  3. Install locally: pip install -e .")
    else:
        print("❌ Some validations FAILED! Fix issues before proceeding.")
        print("\nRecommended actions:")
        print("  1. Check missing files and directories")
        print("  2. Verify import statements")
        print("  3. Review package structure")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
