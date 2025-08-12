from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bot-vision-suite",
    version="1.0.0",
    author="Automation Suite Developer",
    author_email="matheuszwilkdev@gmail.com",
    description="Advanced GUI automation with OCR and image recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/automation-suite/bot-vision-suite",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Desktop Environment",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyAutoGUI==0.9.54",
        "pytesseract",
        "opencv-python==4.9.0.80",
        "Pillow>=10.0.0",
        "numpy==1.26.4",
        "pyperclip>=1.8.2"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ],
        "automation": [
            "keyboard==0.13.5",
            "MouseInfo==0.1.3",
            "setuptools",
            "pandas"
        ],
        "ai": [
            "openai>=1.0.0"
        ],
        "web": [
            "webdriver-manager>=4.0.0"
        ],
    },
    keywords="automation, gui, ocr, image-recognition, rpa, bot, desktop-automation",
    project_urls={
        "Bug Reports": "https://github.com/automation-suite/bot-vision-suite/issues",
        "Source": "https://github.com/automation-suite/bot-vision-suite",
        "Documentation": "https://bot-vision-suite.readthedocs.io/",
    },
)
