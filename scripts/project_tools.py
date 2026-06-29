"""
project_tools.py

Ferramentas para organização e documentação de projetos científicos.

Projeto:
Doutorado_Populismo
"""

from pathlib import Path


def criar_documentacao_projeto(
    base,
    nome,
    autor,
    universidade,
    versao="0.1.0"
):
    """
    Cria automaticamente os arquivos básicos de documentação
    de um projeto científico.

    Parâmetros
    ----------
    base : str ou Path
        Pasta raiz do projeto.

    nome : str
        Nome do projeto.

    autor : str
        Nome do pesquisador.

    universidade : str
        Instituição.

    versao : str
        Versão inicial.
    """

    base = Path(base)

    arquivos = {

        "README.md": f"""# {nome}

Projeto de pesquisa científica.

Este repositório contém notebooks, bases processadas,
resultados e documentação.

Para informações completas consulte:

- PROJECT.md
- CHANGELOG.md

Autor: {autor}

Versão: {versao}
""",

        "PROJECT.md": f"""# {nome}

## Autor

{autor}

## Universidade

{universidade}

## Versão

{versao}

## Objetivo

Documentar toda a arquitetura do projeto, pipeline analítico,
bases utilizadas, notebooks e decisões metodológicas.

Este arquivo deverá ser atualizado durante toda a pesquisa.
""",

        "CHANGELOG.md": f"""# CHANGELOG

## v{versao}

- Estrutura inicial do projeto criada.
""",

        ".gitignore": """__pycache__/
.ipynb_checkpoints/
*.pyc
*.pyo
.DS_Store
Thumbs.db
""",

        "requirements.txt": """pandas
numpy
scipy
scikit-learn
factor-analyzer
duckdb
pyarrow
matplotlib
openpyxl
jupyterlab
"""
    }

    for nome_arquivo, conteudo in arquivos.items():

        caminho = base / nome_arquivo

        if caminho.exists():
            print(f"✔ {nome_arquivo} já existe.")
            continue

        caminho.write_text(
            conteudo,
            encoding="utf-8"
        )

        print(f"✔ Criado: {nome_arquivo}")

    print("\nDocumentação inicial concluída.")