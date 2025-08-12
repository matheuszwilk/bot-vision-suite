#!/usr/bin/env python
"""
Build and package script for bot-vision-suite.

This script handles building, testing, and packaging the bot-vision-suite package.
"""

import os
import sys
import subprocess
import argparse
import shutil
from pathlib import Path

def run_command(cmd, description, check=True):
    """Run a command with error handling."""
    print(f"\n{description}")
    print("=" * len(description))
    
    try:
        result = subprocess.run(cmd, shell=True, check=check, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        return False

def clean_build_artifacts():
    """Clean build artifacts and cache files."""
    print("Cleaning build artifacts...")
    
    # Directories to clean
    clean_dirs = [
        'build',
        'dist', 
        'bot_vision.egg-info',
        'bot_vision_suite.egg-info',
        '.pytest_cache',
        'htmlcov',
        '__pycache__'
    ]
    
    # File patterns to clean
    clean_patterns = [
        '**/*.pyc',
        '**/*.pyo',
        '**/__pycache__'
    ]
    
    for dir_name in clean_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  Removed {dir_name}/")
    
    # Clean Python cache files
    for pattern in clean_patterns:
        for path in Path('.').rglob(pattern):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)

def install_dev_dependencies():
    """Install development dependencies."""
    dev_deps = [
        'pytest>=6.0.0',
        'pytest-cov>=2.10.0',
        'build>=0.7.0',
        'twine>=3.4.0',
        'wheel>=0.37.0'
    ]
    
    cmd = f"pip install {' '.join(dev_deps)}"
    return run_command(cmd, "Installing development dependencies")

def run_tests(test_type="all"):
    """Run tests."""
    if test_type == "unit":
        cmd = "python -m pytest tests/test_exceptions.py tests/test_utils.py tests/test_core.py -v"
    elif test_type == "integration":
        cmd = "python -m pytest tests/test_integration.py -v"
    elif test_type == "coverage":
        cmd = "python -m pytest tests/ --cov=bot_vision --cov-report=html --cov-report=term-missing -v"
    else:
        cmd = "python -m pytest tests/ -v"
    
    return run_command(cmd, f"Running {test_type} tests")

def build_package():
    """Build the package."""
    success = True
    
    # Build source distribution
    success &= run_command("python -m build --sdist", "Building source distribution")
    
    # Build wheel distribution
    success &= run_command("python -m build --wheel", "Building wheel distribution")
    
    return success

def check_package():
    """Check package with twine."""
    return run_command("python -m twine check dist/*", "Checking package with twine")

def install_local():
    """Install package locally for testing."""
    return run_command("pip install -e .", "Installing package locally in development mode")

def verify_installation():
    """Verify the package installation."""
    test_script = '''
import sys
try:
    from bot_vision import BotVision, find_text, click_text
    from bot_vision.utils.config import BotVisionConfig
    print("✓ Package import successful")
    
    config = BotVisionConfig()
    bot = BotVision(config=config)
    print("✓ BotVision instance created")
    
    print("✓ Installation verification passed")
    sys.exit(0)
except Exception as e:
    print(f"✗ Installation verification failed: {e}")
    sys.exit(1)
'''
    
    return run_command(f'python -c "{test_script}"', "Verifying installation")

def main():
    parser = argparse.ArgumentParser(description="Build and package bot-vision-suite")
    parser.add_argument('--clean', action='store_true', help='Clean build artifacts')
    parser.add_argument('--test-only', action='store_true', help='Run tests only')
    parser.add_argument('--build-only', action='store_true', help='Build package only')
    parser.add_argument('--install-deps', action='store_true', help='Install development dependencies')
    parser.add_argument('--coverage', action='store_true', help='Run tests with coverage')
    parser.add_argument('--verify', action='store_true', help='Verify installation only')
    
    args = parser.parse_args()
    
    success = True
    
    if args.clean:
        clean_build_artifacts()
        return 0
    
    if args.install_deps:
        success &= install_dev_dependencies()
        if not args.test_only and not args.build_only:
            return 0 if success else 1
    
    if args.verify:
        success &= verify_installation()
        return 0 if success else 1
    
    if args.test_only:
        test_type = "coverage" if args.coverage else "all"
        success &= run_tests(test_type)
        return 0 if success else 1
    
    if args.build_only:
        clean_build_artifacts()
        success &= build_package()
        success &= check_package()
        return 0 if success else 1
    
    # Full build process
    print("Starting full build process for bot-vision-suite")
    print("=" * 55)
    
    # Step 1: Clean
    clean_build_artifacts()
    
    # Step 2: Install development dependencies
    success &= install_dev_dependencies()
    
    # Step 3: Install package in development mode
    success &= install_local()
    
    # Step 4: Run tests
    test_type = "coverage" if args.coverage else "all"
    success &= run_tests(test_type)
    
    if not success:
        print("\n❌ Tests failed! Fix issues before building package.")
        return 1
    
    # Step 5: Build package
    success &= build_package()
    
    # Step 6: Check package
    success &= check_package()
    
    # Step 7: Verify installation
    success &= verify_installation()
    
    if success:
        print("\n🎉 Build completed successfully!")
        print("\nGenerated files:")
        dist_dir = Path("dist")
        if dist_dir.exists():
            for file in dist_dir.iterdir():
                print(f"  - {file}")
        
        print("\nNext steps:")
        print("  1. Test the package: pip install dist/*.whl")
        print("  2. Upload to PyPI: python -m twine upload dist/*")
        
    else:
        print("\n❌ Build failed! Check the errors above.")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
