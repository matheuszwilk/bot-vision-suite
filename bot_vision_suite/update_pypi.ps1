param(
    [Parameter(Mandatory=$true)]
    [string]$NewVersion,
    
    [Parameter(Mandatory=$false)]
    [string]$ChangelogMessage = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$TestOnly = $false,
    
    [Parameter(Mandatory=$false)]
    [switch]$BugFix = $false
)

Write-Host "🚀 Bot Vision Suite - Update Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# Se for bug fix, adicionar nota especial
if ($BugFix) {
    Write-Host "🚨 BUG FIX RELEASE - Correção crítica" -ForegroundColor Red
    if (!$ChangelogMessage) {
        $ChangelogMessage = "Correção de bug crítico"
    }
}

# Verificar se estamos no diretório correto
if (!(Test-Path "pyproject.toml")) {
    Write-Error "❌ Execute este script na pasta bot_vision_suite que contém pyproject.toml"
    exit 1
}

# 1. Atualizar versão no pyproject.toml
Write-Host "📝 Atualizando versão para $NewVersion..." -ForegroundColor Yellow
$content = Get-Content pyproject.toml
$newContent = $content -replace 'version = ".*"', "version = `"$NewVersion`""
$newContent | Set-Content pyproject.toml

# 2. Atualizar changelog se fornecido
if ($ChangelogMessage) {
    Write-Host "📋 Adicionando entrada no changelog..." -ForegroundColor Yellow
    $date = Get-Date -Format "yyyy-MM-dd"
    $changelogEntry = "`n## [$NewVersion] - $date`n- $ChangelogMessage`n"
    
    # Adicionar no README.md após o título principal
    $readme = Get-Content README.md -Raw
    $readme = $readme -replace "(# Bot Vision Suite.*?\n)", "`$1$changelogEntry"
    $readme | Set-Content README.md
}

# 3. Limpar builds anteriores
Write-Host "🧹 Limpando builds anteriores..." -ForegroundColor Yellow
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# 4. Executar testes
Write-Host "🧪 Executando testes..." -ForegroundColor Yellow
$testResult = pytest --tb=short
if ($LASTEXITCODE -ne 0) {
    Write-Warning "⚠️ Alguns testes falharam. Continuar mesmo assim? (y/N)"
    $response = Read-Host
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "❌ Abortado pelo usuário" -ForegroundColor Red
        exit 1
    }
}

# 5. Fazer build
Write-Host "🔨 Fazendo build do pacote..." -ForegroundColor Yellow
python -m build
if ($LASTEXITCODE -ne 0) {
    Write-Error "❌ Build falhou!"
    exit 1
}

# 6. Validar pacote
Write-Host "✅ Validando pacote..." -ForegroundColor Yellow
twine check dist/*
if ($LASTEXITCODE -ne 0) {
    Write-Error "❌ Validação falhou!"
    exit 1
}

# 7. Upload
if ($TestOnly) {
    Write-Host "🧪 Fazendo upload para TestPyPI..." -ForegroundColor Magenta
    twine upload --repository testpypi dist/*
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Upload para TestPyPI concluído!" -ForegroundColor Green
        Write-Host "🔗 Teste em: https://test.pypi.org/project/bot-vision-suite/" -ForegroundColor Cyan
        Write-Host "📦 Instalar: pip install -i https://test.pypi.org/simple/ bot-vision-suite==$NewVersion" -ForegroundColor Cyan
    }
} else {
    Write-Host "📦 Fazendo upload para PyPI oficial..." -ForegroundColor Magenta
    Write-Host "⚠️ Isso irá publicar a versão $NewVersion permanentemente!" -ForegroundColor Yellow
    Write-Host "Continuar? (y/N): " -NoNewline -ForegroundColor Yellow
    $response = Read-Host
    
    if ($response -eq "y" -or $response -eq "Y") {
        twine upload dist/*
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "🎉 Sucesso! Versão $NewVersion publicada no PyPI!" -ForegroundColor Green
            Write-Host "🔗 Verifique em: https://pypi.org/project/bot-vision-suite/" -ForegroundColor Cyan
            Write-Host "📦 Instalar: pip install bot-vision-suite==$NewVersion" -ForegroundColor Cyan
            
            # Commit das mudanças
            Write-Host "📝 Fazendo commit das mudanças..." -ForegroundColor Yellow
            git add pyproject.toml README.md
            git commit -m "🔖 Release version $NewVersion"
            git tag "v$NewVersion"
            
            Write-Host "💡 Execute 'git push && git push --tags' para enviar ao GitHub" -ForegroundColor Cyan
        } else {
            Write-Error "❌ Falha no upload!"
        }
    } else {
        Write-Host "❌ Upload cancelado pelo usuário" -ForegroundColor Red
    }
}

Write-Host "`n================================================" -ForegroundColor Cyan
Write-Host "Script concluído!" -ForegroundColor Cyan
