# 📋 Checklist para Publicação no PyPI

## ✅ Preparação (Concluído)
- [x] Build gerado com sucesso
- [x] Biblioteca testada localmente
- [x] Funcionalidade "move_to" adicionada
- [x] Documentação atualizada
- [x] README.md completo
- [x] Licença MIT incluída
- [x] pyproject.toml configurado
- [x] URLs corrigidas para github.com/matheuszwilk/bot-vision-suite
- [x] Formato de licença atualizado para SPDX
- [x] setup.py removido (usando apenas pyproject.toml)

## 🔑 Configuração Inicial (Fazer uma vez)
- [ ] Conta criada no https://pypi.org/
- [ ] API Token gerado no PyPI
- [ ] Arquivo ~/.pypirc configurado com o token
- [ ] Ferramentas instaladas: `pip install twine build`

## 🧪 Para Atualizações Futuras

### Método Automático (Recomendado)
```powershell
.\update_pypi.ps1 -NewVersion "1.0.1" -ChangelogMessage "Descrição das mudanças"
```

### Método Manual
1. [ ] Atualizar versão no `pyproject.toml`
2. [ ] Atualizar changelog no `README.md`
3. [ ] Executar testes: `pytest`
4. [ ] Limpar builds: `Remove-Item -Recurse -Force dist, build, *.egg-info`
5. [ ] Build: `python -m build`
6. [ ] Validar: `twine check dist/*`
7. [ ] Upload: `twine upload dist/*`

## 🚀 Primeira Publicação
```powershell
cd 'd:\bot_vision\bot_vision_suite'
python -m build
twine check dist/*
twine upload dist/*
```

## ✅ Verificação Pós-Upload
- [ ] Verificar em: https://pypi.org/project/bot-vision-suite/
- [ ] Testar instalação: `pip install bot-vision-suite`
- [ ] Testar importação: `python -c "import bot_vision; print('OK')"`

## 📁 Arquivos Criados para Updates Futuros
- `PYPI_UPDATE_GUIDE.md` - Guia completo
- `update_pypi.ps1` - Script automatizado
- `QUICK_REFERENCE.md` - Referência rápida
twine upload dist/*
```

- [ ] Upload para PyPI oficial bem-sucedido
- [ ] Testar instalação: `pip install bot-vision-suite`
- [ ] Verificar página do projeto: https://pypi.org/project/bot-vision-suite/

## 📈 Pós-Publicação
- [ ] Atualizar README com instruções de instalação via pip
- [ ] Criar tags no Git com a versão
- [ ] Documentar próximas versões

## 🔧 Para Futuras Atualizações
1. Atualizar versão no `pyproject.toml`
2. Rebuild: `python -m build`
3. Upload: `twine upload dist/*`

## 🆘 Comandos de Emergência
- Remover arquivos dist antigos: `rmdir /s dist`
- Rebuild completo: `python -m build --clean`
- Verificar conteúdo do pacote: `twine check dist/*`

## 📞 Links Úteis
- PyPI Test: https://test.pypi.org/
- PyPI Oficial: https://pypi.org/
- Documentação Twine: https://twine.readthedocs.io/
- Guia PyPI: https://packaging.python.org/
