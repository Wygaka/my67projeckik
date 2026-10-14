$ErrorActionPreference = "Stop"

$hookPath = Join-Path (Get-Location) ".git/hooks/pre-commit"
@'
#!/bin/sh
python -m unittest discover -s tests
'@ | Set-Content -LiteralPath $hookPath -Encoding ASCII

Write-Host "Installed pre-commit hook: $hookPath"

