# CHANGELOG

\## \[v0.5.0] - 2026-06-28



\### Adicionado

\- Notebook `06\_integracao\_VDEM.ipynb`.

\- Integração entre a base analítica do WVS e a base institucional do V-Dem.

\- Recuperação das chaves `country\_text\_id` e `year` a partir da base original do WVS.

\- Construção da base multinível contendo indicadores individuais e institucionais.

\- Validação da unicidade da chave país-ano no V-Dem.

\- Validação da integridade do processo de integração.



\### Resultados

\- Base multinível criada com 39.720 respondentes.

\- Integração bem-sucedida para aproximadamente 97,16% das observações.

\- Casos sem correspondência restritos a Porto Rico (PRI), ausente da cobertura territorial do V-Dem.



\### Decisões metodológicas

\- A integração foi realizada exclusivamente pelas variáveis `country\_text\_id` e `year`.

\- Não foram efetuadas imputações para unidades territoriais ausentes no V-Dem.

\- As dimensões institucionais produzidas anteriormente permanecem consolidadas e não serão recalculadas.



## v0.4.0 — Perfis Afetivos

### Concluído

* Organização da estrutura do projeto.
* Preparação do WVS.
* Construção dos indicadores derivados.
* Experimento 3: Análise Fatorial Exploratória.
* Construção dos fatores de segunda ordem.
* Experimento 4: identificação de três perfis afetivos.
* Validação dos perfis por centroides, coesão, PCA, qui-quadrado, V de Cramér e resíduos padronizados.
* Exportação das bases, tabelas e figuras.
* Criação do PROJECT.md.

### Próxima etapa

* 06\_integracao\_VDEM.ipynb

### Objetivo da próxima etapa

Construir a base integrada WVS + V-Dem:

dados/integrados/wvs\_vdem.parquet

