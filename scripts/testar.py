#!/usr/bin/env python3
"""Roda todos os testes automáticos do repositório e o empacotamento.

Uso, a partir da raiz do repositório:
    python3 scripts/testar.py

Etapas: scripts (contas e casos-limite), estrutura das skills, acionamento aproximado e empacotamento
(valida e gera os .zip em dist/). Sai com código diferente de zero se algo falhar.
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ETAPAS = (
    ("scripts", "tests/test_scripts.py"),
    ("estrutura", "tests/test_estrutura.py"),
    ("acionamento", "tests/test_gatilho.py"),
    ("empacotamento", "scripts/empacotar.py"),
)


def main():
    falhas = []
    for nome, caminho in ETAPAS:
        p = subprocess.run([sys.executable, str(RAIZ / caminho)], capture_output=True, text=True, cwd=RAIZ)
        saida = p.stdout.strip().splitlines()
        resumo = saida[0] if saida else ""
        print(f"{'OK   ' if p.returncode == 0 else 'FALHA'} {nome}: {resumo}")
        if p.returncode != 0:
            falhas.append(nome)
            print(p.stdout)
            print(p.stderr, file=sys.stderr)
    if falhas:
        print(f"\nFalharam: {', '.join(falhas)}", file=sys.stderr)
        sys.exit(1)
    print("\nTudo certo.")


if __name__ == "__main__":
    main()
