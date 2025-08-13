# 🚀 Quick Reference - PyPI Updates

## Comandos Rápidos

### Update Simples
```powershell
.\update_pypi.ps1 -NewVersion "1.0.1"
```

### Update com Changelog
```powershell
.\update_pypi.ps1 -NewVersion "1.0.1" -ChangelogMessage "Correção de bug na função OCR"
```

### Testar no TestPyPI primeiro
```powershell
.\update_pypi.ps1 -NewVersion "1.0.1" -TestOnly
```

## Manual Steps (se preferir fazer manualmente)

### 1. Atualizar versão
```toml
# pyproject.toml
version = "1.0.1"  # Altere aqui
```

### 2. Build e Upload
```powershell
cd 'd:\bot_vision\bot_vision_suite'
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
python -m build
twine check dist/*
twine upload dist/*
```

## Versionamento

- **1.0.1** → Patch (bug fixes)
- **1.1.0** → Minor (new features)  
- **2.0.0** → Major (breaking changes)

## Links Úteis

- **PyPI Package**: https://pypi.org/project/bot-vision-suite/
- **Test PyPI**: https://test.pypi.org/project/bot-vision-suite/
- **GitHub Repo**: https://github.com/matheuszwilk/bot-vision-suite
- **PyPI Stats**: https://pypistats.org/packages/bot-vision-suite

## Troubleshooting

- **"File already exists"** → Versão já publicada, mude a versão
- **"Invalid credentials"** → Verifique token em `~\.pypirc`
- **Build fails** → Execute `pytest` para ver erros
