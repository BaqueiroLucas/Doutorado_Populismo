# Doutorado_Populismo

Repositório de desenvolvimento computacional da pesquisa de doutorado **"Populismo na Era de Narciso: Carisma, Identificação e Organização Política na América Contemporânea"**, desenvolvida no âmbito Programa de Pós-Graduação em Ciência Política da Universidade Federal de São Carlos (UFSCar).

Este repositório reúne notebooks, scripts, bases analíticas, documentação e produtos intermediários utilizados na construção da infraestrutura empírica e nas análises quantitativas da tese.

---

# Objetivo

O projeto tem como objetivo construir uma infraestrutura analítica reproduzível para investigar as relações entre:

* atitudes políticas individuais;
* perfis afetivos;
* contexto institucional;
* sistemas partidários;
* populismo contemporâneo;
* narcisismo coletivo.

Toda a arquitetura foi desenvolvida para privilegiar modularidade, rastreabilidade, reprodutibilidade e documentação permanente das decisões metodológicas.

---

# Bases de dados utilizadas

A pesquisa integra informações provenientes de três grandes bases internacionais:

* **World Values Survey (WVS)** — atitudes e valores individuais;
* **Varieties of Democracy (V-Dem)** — contexto institucional;
* **V-Dem CPD Party Dataset (V-Party)** — características dos sistemas partidários.

Essas bases foram harmonizadas em uma estrutura multinível que preserva a unidade de análise no nível do indivíduo.

---

# Estrutura do repositório

```text
notebooks/          Pipeline analítico da pesquisa
scripts/            Biblioteca de funções reutilizáveis
dados/
    brutos/         Bases originais
    integrados/     Produtos persistidos do pipeline
resultados/         Tabelas, figuras e produtos analíticos

PROJECT.md          Documento mestre do projeto
CHANGELOG.md        Histórico de versões
README.md           Documentação geral do repositório
```

---

# Pipeline analítico

A infraestrutura foi construída de forma incremental.

Até a versão atual foram concluídas as seguintes etapas:

* preparação da base WVS;
* construção de indicadores individuais;
* Análise Fatorial Exploratória (AFE);
* construção de fatores de segunda ordem;
* identificação dos perfis afetivos;
* integração multinível WVS + V-Dem;
* integração do V-Party;
* construção da base analítica definitiva.

O principal produto do pipeline é:

```text
dados/integrados/base_analitica.parquet
```

Essa base constitui a entrada oficial para todas as análises empíricas subsequentes da tese.

---

# Estado atual

**Versão atual:** v0.6.0

A infraestrutura analítica da pesquisa encontra-se concluída, validada e documentada.

O projeto entra agora na fase de produção dos resultados científicos, dedicada às análises relacionais e aos modelos explicativos previstos na tese.

As próximas etapas incluem:

* Multiple Correspondence Analysis (MCA);
* Multiple Factor Analysis (MFA);
* Correspondence Analysis (CA);
* modelos multinível;
* interpretação substantiva dos resultados.

---

# Reprodutibilidade

O projeto foi concebido segundo princípios de pesquisa reproduzível.

Todas as etapas são:

* documentadas;
* versionadas;
* auditáveis;
* executadas por notebooks independentes;
* organizadas em pipeline modular.

Produtos intermediários são preservados sempre que contribuem para auditoria ou reutilização em etapas posteriores.

---

# Observações sobre os dados

As bases originais internacionais não são mantidas sob controle de versão neste repositório.

São versionados apenas:

* scripts;
* notebooks;
* documentação;
* produtos intermediários;
* bases analíticas necessárias à continuidade do projeto.

Essa estratégia reduz o tamanho do repositório sem comprometer a reprodutibilidade da pesquisa.

---

# Autor

**Pe. Lucas Mariano Maciel-Baqueiro**, M.Sc., Cand. Ph.D.

Programa de Pós-Graduação em Ciência Política - Universidade Federal de São Carlos — UFSCar
