#!/usr/bin/env bash
# Gera um .zip por skill em dist/, para quem usa o Claude.ai ou o Claude Desktop
# e instala skills enviando um arquivo (Configurações > Capacidades > Skills).
#
# Uso (a partir da raiz do repositório):
#   ./scripts/empacotar.sh              # empacota todas as skills
#   ./scripts/empacotar.sh user-story   # empacota só uma
set -euo pipefail

raiz="$(cd "$(dirname "$0")/.." && pwd)"
origem="$raiz/plugins/produto/skills"
destino="$raiz/dist"

mkdir -p "$destino"

if [ "$#" -gt 0 ]; then
  skills=("$@")
else
  skills=()
  for pasta in "$origem"/*/; do
    skills+=("$(basename "$pasta")")
  done
fi

for skill in "${skills[@]}"; do
  if [ ! -f "$origem/$skill/SKILL.md" ]; then
    echo "Skill não encontrada: $skill" >&2
    exit 1
  fi
  rm -f "$destino/$skill.zip"
  (cd "$origem" && zip -r -q "$destino/$skill.zip" "$skill" -x "*.DS_Store" -x "*__pycache__*" -x "*.pyc")
  echo "Gerado: dist/$skill.zip"
done
