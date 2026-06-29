# CHANGELOG

## [v0.6.0] - 2026-06-29

### Adicionado

- Notebook `07_integracao_VPARTY.ipynb`.
- Integração da base multinível WVS + V-Dem com indicadores partidários do V-Party.
- Construção do recorte `vparty_americas.parquet`.
- Construção da base agregada `vparty_agregado.parquet`.
- Construção da base harmonizada `vparty_contexto.parquet`.
- Construção da base analítica final `base_analitica.parquet`.

### Decisões metodológicas

- A integração com o V-Party não foi realizada diretamente por igualdade de ano.
- Como o V-Party é organizado por eleições, foi adotado o critério da eleição imediatamente anterior ou coincidente ao ano da entrevista do WVS.
- Os indicadores partidários foram agregados no nível país-eleição.
- Não foi adotado limiar binário para classificação de partidos populistas.
- O populismo partidário foi tratado como medida contínua.
- Foram preservados indicadores de cobertura para análises de sensibilidade e robustez.

### Resultados

- A base analítica final preserva a unidade de análise no nível do indivíduo.
- A base final integra variáveis individuais, fatores latentes, perfis afetivos, indicadores institucionais e indicadores partidários.
- Porto Rico permanece sem correspondência nas integrações contextuais.
- Os produtos intermediários foram preservados para reutilização em experimentos futuros.

### Melhorias futuras

- Refatorar `scripts/project_tools.py` em pacote modular.
- Priorizar essa refatoração antes do início das análises relacionais do Notebook 08.

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

