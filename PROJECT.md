# Documento Mestre do Projeto

# 1. A Pesquisa

## Identificação

**Populismo na Era de Narciso: Carisma, Identificação e Organização Política na América Contemporânea**

Programa de Pós-Graduação em Ciência Política

Universidade Federal de São Carlos (UFSCar)

Projeto de doutorado.

---

## Apresentação

Este documento constitui o registro mestre do projeto de pesquisa.

Seu objetivo é documentar, simultaneamente, a fundamentação científica, a arquitetura computacional e o estado de desenvolvimento da investigação, permitindo que qualquer pesquisador possa compreender a lógica do projeto e reproduzir integralmente todas as etapas analíticas.

Embora elaborado para fins de documentação científica e reprodutibilidade, este documento também serve como referência operacional para a continuidade do desenvolvimento computacional da pesquisa, registrando decisões metodológicas já consolidadas, arquivos produzidos, convenções adotadas e etapas futuras.

Diferentemente do texto da tese, este documento possui natureza operacional. Seu propósito não é substituir a fundamentação teórica ou metodológica desenvolvida no manuscrito, mas registrar como essa fundamentação vem sendo implementada empiricamente ao longo do projeto.

---

## Objeto da pesquisa

Esta pesquisa investiga o populismo contemporâneo como uma lógica política relacional capaz de produzir identificação entre líderes e massas mediante a articulação entre dimensões discursivas, afetivas e organizacionais.

Parte-se da hipótese de que o populismo não constitui uma ideologia específica nem pode ser reduzido exclusivamente a estratégias eleitorais ou estilos discursivos. Ao contrário, compreende-se o populismo como um processo relacional de construção política, no qual antagonismos entre "povo" e "elite" são produzidos e estabilizados por mecanismos de identificação coletiva, liderança carismática e formas específicas de organização política. 

O foco empírico da pesquisa recai sobre a América contemporânea, especialmente no período compreendido entre a crise financeira internacional de 2008 e os processos políticos observados até 2027, contexto caracterizado pela intensificação da personalização da liderança política, pela desintermediação comunicacional e pela reorganização das formas tradicionais de representação política. 

---

## Perspectiva analítica

A pesquisa organiza-se em torno de três grandes planos analíticos, permanentemente articulados entre si:

- o plano discursivo, responsável pela construção simbólica das fronteiras entre povo e elite;

- o plano afetivo, responsável pelos mecanismos de identificação política, pertencimento coletivo e mobilização emocional;

- o plano organizacional, responsável pelas formas institucionais através das quais lideranças e organizações políticas estruturam e estabilizam essas relações.

Esses planos não são tratados como dimensões independentes, mas como componentes complementares de uma mesma lógica política.

---

## Estratégia geral de investigação

A pesquisa combina fundamentação teórica e análise empírica comparada.

No plano empírico, utiliza bases internacionais amplamente consolidadas — World Values Survey (WVS), Varieties of Democracy (V-Dem) e V-Party — para reconstruir empiricamente as estruturas relacionais associadas ao populismo contemporâneo.

A estratégia metodológica adota técnicas de redução dimensional e análise geométrica de dados para identificar estruturas latentes, construir tipologias e integrar informações provenientes de diferentes níveis analíticos (indivíduos, países e partidos políticos).

---

## Objetivo deste documento

Este PROJECT.md acompanha toda a evolução computacional da pesquisa.

Sempre que um notebook for concluído, este documento deverá ser atualizado para registrar:

- novas decisões metodológicas;
- arquivos produzidos;
- alterações na arquitetura do projeto;
- mudanças no pipeline analítico;
- novas etapas concluídas.

Dessa forma, este documento constitui a principal referência para a continuidade da pesquisa, tanto por pesquisadores quanto por sistemas de inteligência artificial utilizados como apoio ao desenvolvimento do projeto.

# 2. Problema de Pesquisa, Hipótese e Objetivos

## Problema de pesquisa

Nas últimas décadas, o populismo consolidou-se como um dos principais objetos da Ciência Política comparada. Apesar da ampla produção acadêmica, permanece um desacordo substantivo acerca de sua natureza, de seus mecanismos constitutivos e de suas formas de manifestação empírica.

Parte importante dessa literatura compreende o populismo como uma ideologia de baixa densidade, um estilo discursivo, uma estratégia política ou uma lógica de articulação entre demandas sociais. Essas abordagens, embora fundamentais, tendem a privilegiar dimensões específicas do fenômeno, frequentemente analisadas de maneira isolada.

O presente projeto parte da premissa de que essa fragmentação dificulta a compreensão do populismo como fenômeno complexo. A investigação propõe que sua explicação exige a articulação simultânea entre dimensões discursivas, afetivas, organizacionais e institucionais, compreendidas como componentes de um mesmo processo político.

Nesse sentido, o problema central da pesquisa consiste em compreender como mecanismos de identificação coletiva, lideranças carismáticas, orientações afetivas e contextos institucionais interagem na constituição e na reprodução do populismo contemporâneo nas democracias americanas.

---

## Hipótese Geral

A hipótese central da pesquisa sustenta que o populismo pode ser compreendido como uma lógica relacional de organização política, cuja estabilidade depende da interação entre três dimensões complementares:

- uma dimensão discursiva, responsável pela construção simbólica do antagonismo entre "povo" e "elite";
- uma dimensão afetiva, responsável pela formação de identidades políticas, vínculos emocionais e mecanismos de pertencimento coletivo;
- uma dimensão organizacional, responsável pela institucionalização dessas relações em lideranças, partidos e formas de representação política.

Essas dimensões não atuam de forma independente. Ao contrário, reforçam-se mutuamente, produzindo configurações distintas conforme o contexto institucional e partidário em que se desenvolvem.

---

## Hipóteses Operacionais

A operacionalização empírica da pesquisa deriva dessa hipótese geral e orienta a construção dos experimentos computacionais.

Até o momento, foram adotadas as seguintes hipóteses operacionais:

**H1.** Atitudes políticas e valores individuais observados no World Values Survey organizam-se em dimensões latentes identificáveis por técnicas de redução dimensional.

**H2.** Essas dimensões podem ser sintetizadas em fatores de ordem superior, representando estruturas afetivas mais amplas relacionadas ao populismo.

**H3.** Os fatores de segunda ordem permitem identificar perfis relativamente homogêneos de indivíduos por meio de técnicas de clusterização.

**H4.** A distribuição desses perfis não ocorre aleatoriamente entre os países, estando associada a características contextuais dos regimes políticos.

**H5.** Indicadores institucionais (V-Dem) e características partidárias (V-Party) contribuirão para explicar diferenças observadas na distribuição desses perfis entre contextos nacionais.

Essas hipóteses orientam diretamente a sequência dos notebooks desenvolvidos neste projeto.

---

## Objetivo Geral

Investigar como mecanismos de identificação política, disposições afetivas e características institucionais articulam-se na constituição do populismo contemporâneo, utilizando uma estratégia comparada baseada em dados individuais, institucionais e partidários.

---

## Objetivos Específicos

Para atingir esse objetivo geral, a pesquisa foi organizada em etapas sucessivas.

### Objetivo 1

Construir indicadores individuais derivados do World Values Survey capazes de representar dimensões teoricamente relevantes para o estudo do populismo.

### Objetivo 2

Identificar estruturas latentes por meio de Análise Fatorial Exploratória, reduzindo a dimensionalidade do conjunto inicial de indicadores.

### Objetivo 3

Construir fatores de segunda ordem que sintetizem relações entre as dimensões identificadas na etapa anterior.

### Objetivo 4

Identificar tipologias de indivíduos por meio de técnicas de clusterização aplicadas aos fatores de segunda ordem.

### Objetivo 5

Validar empiricamente os perfis obtidos utilizando diferentes critérios estatísticos e gráficos, assegurando sua consistência interna e sua interpretabilidade substantiva.

### Objetivo 6

Integrar os perfis individuais a indicadores institucionais provenientes do V-Dem, preservando a unidade de análise no nível do indivíduo.

### Objetivo 7

Incorporar indicadores partidários do V-Party à base integrada, permitindo analisar conjuntamente fatores individuais, institucionais e partidários.

### Objetivo 8

Estimar modelos estatísticos capazes de avaliar em que medida contextos institucionais e sistemas partidários influenciam a distribuição dos perfis afetivos identificados.

---

## Relação entre teoria e implementação computacional

A arquitetura computacional do projeto foi concebida para refletir diretamente o desenho teórico da pesquisa.

Cada notebook corresponde a uma etapa analítica específica e operacionaliza um objetivo metodológico claramente definido. A separação entre preparação dos dados, construção dos indicadores, identificação de fatores, formação dos perfis e integração com bases contextuais busca assegurar transparência, reprodutibilidade e rastreabilidade de todas as decisões tomadas ao longo da investigação.

Essa correspondência entre objetivos científicos e organização computacional constitui um princípio estruturante do projeto e orientará todas as etapas subsequentes da pesquisa.

# 3. Fundamentação Teórica

## Perspectiva Geral

Esta pesquisa adota uma perspectiva relacional do populismo. Em vez de concebê-lo como uma ideologia específica, um estilo de comunicação ou uma estratégia eleitoral isolada, o projeto compreende o populismo como um processo político de construção de identidades coletivas, no qual discursos, afetos e formas organizacionais articulam-se na constituição de sujeitos políticos.

Essa perspectiva permite integrar diferentes tradições da literatura sem reduzir o fenômeno a uma única dimensão analítica.

Embora reconheça as contribuições das abordagens ideacional, estratégica e discursiva, o projeto parte da premissa de que nenhuma delas, isoladamente, é suficiente para explicar a emergência, a estabilidade e a transformação dos movimentos populistas contemporâneos.

---

# Principais Referências

A pesquisa dialoga principalmente com cinco tradições da literatura.

## 1. A tradição discursiva

A obra de Ernesto Laclau constitui o principal referencial para compreender o populismo como lógica política.

Nessa perspectiva, o populismo não corresponde a um conjunto fixo de ideias nem a uma ideologia determinada, mas a um modo específico de construção do político.

Demandas sociais inicialmente dispersas podem tornar-se equivalentes mediante processos de articulação discursiva, produzindo uma fronteira antagônica entre "o povo" e "a elite". A identidade popular emerge precisamente desse processo de construção simbólica.

Essa formulação oferece o ponto de partida teórico da presente investigação.

---

## 2. A dimensão agonística

A perspectiva agonística, especialmente desenvolvida por Chantal Mouffe, complementa a teoria laclauniana ao enfatizar o conflito como elemento constitutivo da democracia.

O antagonismo não representa uma patologia das sociedades democráticas, mas uma característica inerente da política.

A pesquisa incorpora essa perspectiva ao considerar que diferentes formas de populismo expressam maneiras distintas de organizar conflitos sociais e construir pertencimentos coletivos.

---

## 3. A dimensão sociocultural

A literatura de Pierre Ostiguy amplia a compreensão do populismo ao destacar sua dimensão sociocultural.

O populismo envolve estilos de liderança, formas de comunicação, códigos simbólicos e relações específicas entre representantes e representados.

Essa perspectiva contribui para compreender como diferentes lideranças mobilizam identidades populares para além das disputas estritamente programáticas.

---

## 4. Carisma e identificação

O projeto também dialoga com a tradição inaugurada por Max Weber sobre autoridade carismática.

O carisma é compreendido não como atributo psicológico do líder, mas como uma relação social de reconhecimento.

Essa interpretação aproxima-se das formulações contemporâneas sobre identificação política, nas quais a legitimidade das lideranças depende da produção contínua de vínculos afetivos entre líderes, seguidores e coletividades.

A relação entre carisma, identificação e populismo constitui um dos eixos centrais da tese.

---

## 5. Psicologia política e afetos

O projeto incorpora contribuições recentes da Psicologia Política para compreender a dimensão afetiva do comportamento político.

Atitudes relativas à identidade nacional, confiança institucional, autoritarismo, percepção de ameaça, exclusão social, pertencimento coletivo e engajamento político são tratadas como manifestações observáveis de estruturas latentes mais profundas.

Essas estruturas não são consideradas características individuais isoladas, mas componentes de processos coletivos de identificação política.

---

# Integração Teórica

A contribuição original da pesquisa consiste em integrar essas diferentes tradições analíticas.

Em vez de tratar discurso, afetos e organização como explicações concorrentes, o projeto parte da hipótese de que essas dimensões são mutuamente constitutivas.

A construção discursiva do povo produz identidades coletivas.

Essas identidades são sustentadas por mecanismos afetivos de pertencimento.

Por sua vez, esses mecanismos tornam-se relativamente estáveis quando institucionalizados por organizações políticas, partidos, movimentos e lideranças.

Consequentemente, compreender o populismo exige analisar simultaneamente indivíduos, organizações e contextos institucionais.

---

# Implicações Metodológicas

Essa perspectiva relacional possui consequências diretas para o desenho empírico da pesquisa.

Em vez de buscar uma medida única de populismo, a investigação procura identificar padrões multidimensionais de atitudes e orientações políticas presentes nos indivíduos.

Esses padrões são inicialmente sintetizados por técnicas de redução dimensional, posteriormente organizados em perfis de indivíduos e, por fim, relacionados a características institucionais e partidárias dos diferentes contextos nacionais.

A arquitetura computacional da pesquisa foi concebida para refletir exatamente essa sequência lógica.

Cada etapa do pipeline operacionaliza uma dimensão específica do modelo teórico, permitindo preservar a coerência entre fundamentação conceitual e implementação empírica.

---

# Escopo Analítico

O objetivo da pesquisa não é classificar indivíduos como "populistas" ou "não populistas".

O foco consiste em identificar configurações afetivas e relacionais que possam contribuir para compreender diferentes formas de identificação política presentes nas democracias contemporâneas.

Esses perfis constituem construções analíticas derivadas dos dados e deverão ser interpretados à luz da teoria desenvolvida ao longo da tese, sempre considerando as limitações inerentes às técnicas de redução dimensional e clusterização empregadas.

# 4. Desenho Metodológico

## Estratégia Geral

Esta pesquisa adota um desenho quantitativo comparado, combinando informações provenientes de diferentes níveis analíticos com o objetivo de compreender como disposições individuais, contextos institucionais e características dos sistemas partidários articulam-se na formação dos perfis afetivos associados ao populismo contemporâneo.

A estratégia metodológica foi concebida em etapas sucessivas, de modo que cada procedimento produza insumos para a etapa seguinte, preservando a rastreabilidade das decisões analíticas e a completa reprodutibilidade do projeto.

Em todas as etapas, a unidade fundamental de análise permanece sendo o indivíduo, ao qual são posteriormente incorporadas informações contextuais provenientes de bases externas.

---

# Bases de Dados

## World Values Survey (WVS)

O World Values Survey constitui a principal fonte de dados individuais da pesquisa.

A partir dessa base foram selecionadas variáveis relacionadas a:

- identidade nacional;
- confiança interpessoal;
- confiança institucional;
- participação política;
- interesse por política;
- valores democráticos;
- autoritarismo;
- atitudes frente à diversidade;
- pertencimento coletivo;
- religiosidade;
- orientações normativas.

Essas variáveis foram utilizadas para construir indicadores derivados capazes de representar diferentes dimensões teoricamente relevantes para o estudo do populismo.

---

## V-Dem

O Varieties of Democracy será utilizado para incorporar características institucionais dos regimes políticos.

A integração ocorrerá no nível país-ano, preservando a observação individual do World Values Survey.

Serão selecionados apenas os indicadores necessários para responder às hipóteses da pesquisa, evitando o uso indiscriminado do conjunto completo de variáveis disponibilizadas pelo projeto V-Dem.

---

## V-Party

O V-Dem CPD Party Dataset (V-Party) foi integrado à base multinível mediante a construção de indicadores agregados do sistema partidário no nível país-eleição.

A integração preserva a unidade de análise no nível do indivíduo, incorporando ao World Values Survey características estruturais dos sistemas partidários, incluindo organização, populismo, antipluralismo, posicionamento ideológico, clientelismo, polarização e indicadores de cobertura.

Em razão da natureza eleitoral da base, adotou-se procedimento de harmonização temporal que associa cada entrevista do World Values Survey à eleição imediatamente anterior ou coincidente, preservando a precedência temporal entre contexto político e atitudes individuais.

---

# Construção dos Indicadores

As variáveis originais do World Values Survey passaram por um processo sistemático de preparação.

Esse processo compreendeu:

- seleção das variáveis relevantes;
- harmonização das escalas;
- tratamento de valores ausentes;
- recodificações necessárias;
- construção de indicadores compostos;
- padronização das métricas utilizadas ao longo do projeto.

Os indicadores produzidos representam operacionalizações empíricas de conceitos desenvolvidos na fundamentação teórica da tese.

---

# Redução Dimensional

Considerando a elevada correlação existente entre diversos indicadores, optou-se pela utilização de Análise Fatorial Exploratória (AFE).

A escolha dessa técnica fundamenta-se na hipótese de que diferentes atitudes observáveis refletem estruturas latentes comuns.

A determinação do número de fatores foi baseada na combinação de diferentes critérios:

- análise paralela de Horn;
- scree plot;
- interpretabilidade substantiva;
- coerência teórica.

A solução final resultou em oito fatores de primeira ordem.

Posteriormente, esses fatores foram submetidos a uma segunda Análise Fatorial Exploratória, produzindo três fatores de ordem superior.

Esses fatores sintetizam estruturas latentes mais abrangentes relacionadas às orientações afetivas dos indivíduos.

---

# Construção dos Perfis

Os três fatores de segunda ordem constituíram a base para a identificação de tipologias de indivíduos.

Foi utilizada a técnica K-Means.

Diversas soluções foram comparadas utilizando critérios clássicos de validação:

- Inertia;
- Silhouette Score;
- Calinski-Harabasz;
- Davies-Bouldin.

Embora alguns critérios estatísticos favorecessem soluções com menor número de grupos, a solução contendo três clusters apresentou melhor interpretabilidade substantiva e foi adotada como solução final.

Essa decisão encontra-se integralmente documentada no notebook correspondente.

---

# Validação

A consistência da solução obtida foi avaliada mediante diferentes procedimentos.

Entre eles destacam-se:

- distribuição das frequências;
- análise dos centroides;
- matriz de distâncias entre clusters;
- coesão interna;
- projeção por PCA exclusivamente para visualização;
- associação entre perfis e países por meio do teste do qui-quadrado;
- cálculo do V de Cramér;
- análise dos resíduos padronizados.

Esses procedimentos permitiram avaliar simultaneamente separação, homogeneidade e interpretabilidade dos perfis identificados.

---

# Integração Multinível

A etapa de integração multinível foi concluída mediante a incorporação de indicadores institucionais do Varieties of Democracy (V-Dem) à base analítica derivada do World Values Survey (WVS).

A integração foi realizada utilizando as variáveis `country_text_id` e `year`, preservando a observação individual como unidade fundamental de análise. A inexistência de duplicidades na base institucional permitiu uma integração do tipo *many-to-one*, assegurando a correspondência unívoca entre indivíduos e seus respectivos contextos nacionais.

A validação do procedimento indicou taxa de correspondência superior a 97% dos respondentes. Os casos sem correspondência concentram-se exclusivamente em Porto Rico (PRI), unidade presente no WVS, mas não contemplada como Estado soberano na versão utilizada do V-Dem.

A base integrada passa a constituir a principal entrada para as etapas subsequentes da pesquisa.

Posteriormente, essa base foi ampliada mediante integração com o V-Party, produzindo a base analítica definitiva da pesquisa (`base_analitica.parquet`), na qual coexistem variáveis individuais, institucionais e partidárias.

---

# Filosofia Computacional

Toda a implementação computacional foi organizada segundo uma arquitetura modular.

Cada notebook possui responsabilidade única e produz arquivos persistentes utilizados pelas etapas subsequentes.

Nenhuma análise depende da permanência de objetos na memória do ambiente computacional.

Todos os resultados relevantes são exportados para disco em formatos abertos, permitindo completa reprodutibilidade das análises.

Essa organização busca garantir que qualquer pesquisador possa reproduzir integralmente os resultados da tese executando cada notebook de forma independente, respeitando apenas a sequência lógica do pipeline analítico.

# 5. Arquitetura Computacional do Projeto

## Princípios Gerais

A implementação computacional da pesquisa foi concebida para atender simultaneamente aos princípios de reprodutibilidade científica, modularidade, transparência metodológica e rastreabilidade analítica.

Toda a arquitetura do projeto foi organizada de forma que cada etapa produza artefatos persistentes, permitindo a reprodução integral dos resultados sem dependência da memória do ambiente computacional ou da execução contínua dos notebooks anteriores.

Consequentemente, cada notebook constitui um módulo independente dentro de um pipeline analítico maior.

---

# Estrutura do Projeto

A organização dos diretórios segue uma lógica funcional.

```
Doutorado_Populismo
│
├── dados
│   ├── brutos
│   │   ├── WVS
│   │   ├── VDEM
│   │   └── VPARTY
│   │
│   ├── processados
│   │
│   └── integrados
│
├── notebooks
│
├── resultados
│   ├── experimento3
│   └── experimento4
│
├── figuras
│   ├── experimento3
│   └── experimento4
│
├── scripts
│
├── README.md
├── PROJECT.md
└── CHANGELOG.md
```

Cada diretório possui responsabilidade única e não deve ser utilizado para armazenar arquivos pertencentes a outras etapas do projeto.

---

# Organização dos Notebooks

Os notebooks constituem a unidade principal de execução da pesquisa.

Cada notebook possui um único objetivo analítico claramente definido.

A comunicação entre notebooks ocorre exclusivamente por meio de arquivos gravados em disco.

Essa decisão elimina dependências ocultas entre sessões do Jupyter e garante completa reprodutibilidade.

Até o momento, a organização prevista é:

| Notebook | Objetivo |
|-----------|----------|
| 01_preparacao_WVS.ipynb | Preparação da base do World Values Survey |
| 02_experimento1.ipynb | Reprodução do Experimento 1 |
| 03_experimento2.ipynb | Reprodução do Experimento 2 |
| 04_experimento3_AFE.ipynb | Construção dos fatores latentes |
| 05_experimento4_Perfis.ipynb | Construção e validação dos perfis |
| 06_integracao_VDEM.ipynb | Integração com indicadores institucionais |
| 07_integracao_VPARTY.ipynb | Integração com indicadores partidários |
| 08_modelos.ipynb | Modelos estatísticos finais |

---

# Fluxo de Dados

O projeto segue uma sequência rígida de transformação dos dados.

```
Bases brutas
        │
        ▼
Preparação
        │
        ▼
Indicadores
        │
        ▼
Análise Fatorial
        │
        ▼
Fatores de Segunda Ordem
        │
        ▼
Perfis Afetivos
        │
        ▼
Integração V-Dem
        │
        ▼
Integração V-Party
        │
        ▼
Base Analítica
        │
        ▼
Análises Relacionais
        │
        ▼
Modelagem Estatística

Cada etapa produz novos arquivos sem modificar aqueles produzidos anteriormente.

---

# Persistência dos Dados

Uma decisão metodológica fundamental deste projeto consiste em persistir todos os resultados intermediários.

Não são recalculados resultados cuja validade metodológica já tenha sido estabelecida.

Essa estratégia reduz tempo computacional, melhora a rastreabilidade das análises e evita divergências decorrentes de sucessivas reexecuções de procedimentos exploratórios.

As bases intermediárias são armazenadas preferencialmente no formato Parquet devido à sua eficiência de leitura, escrita e preservação dos tipos de dados.

---

# Convenções

Foram adotadas as seguintes convenções ao longo do projeto.

## Bases de dados

- Bases originais permanecem imutáveis.
- Bases derivadas são gravadas em `dados/processados`.
- Bases integradas são gravadas em `dados/integrados`.

---

## Resultados

Tabelas analíticas são armazenadas em:

```
resultados/experimentoX
```

Figuras são armazenadas em:

```
figuras/experimentoX
```

---

## Código

Os notebooks concentram apenas a lógica analítica específica de cada experimento.

Funções reutilizáveis devem ser gradualmente transferidas para o diretório:

```
scripts/
```

Essa organização reduz duplicação de código e facilita manutenção futura.

---

# Documentação

A documentação do projeto encontra-se distribuída em três níveis.

## README.md

Documento introdutório destinado à apresentação geral do projeto.

---

## PROJECT.md

Documento mestre.

Descreve:

- objetivos científicos;
- fundamentação metodológica;
- arquitetura computacional;
- estado atual da pesquisa;
- pipeline analítico;
- convenções adotadas.

Este documento deve ser atualizado sempre que uma etapa importante da pesquisa for concluída.

---

## CHANGELOG.md

Registro cronológico das alterações realizadas no projeto.

Seu objetivo é documentar a evolução metodológica e computacional da pesquisa.

---

# Estado da Implementação

Até o momento, encontram-se implementadas e validadas as seguintes etapas computacionais:

- preparação do banco do World Values Survey;
- construção dos indicadores derivados;
- Análise Fatorial Exploratória;
- construção dos fatores de segunda ordem;
- identificação dos perfis afetivos;
- validação estatística dos perfis;
- exportação completa das tabelas e figuras;
- organização definitiva da estrutura do projeto;
- integração multinível entre WVS e V-Dem;
- integração do V-Party;
- harmonização temporal entre WVS e V-Party;
- construção da base analítica definitiva;
- validação completa da infraestrutura analítica.

A infraestrutura de dados da pesquisa encontra-se concluída.

As etapas subsequentes dedicar-se-ão exclusivamente às análises relacionais e aos modelos explicativos previstos na tese.

Nenhuma etapa posterior deverá modificar as bases consolidadas, salvo justificativa metodológica expressa.

# 6. Estado Atual da Pesquisa

## Visão Geral

Até o presente momento, a pesquisa concluiu integralmente a etapa de construção dos indicadores individuais e da estrutura latente dos dados provenientes do World Values Survey.

As etapas executadas produziram uma base analítica consistente, documentada e reprodutível, permitindo que as próximas fases concentrem-se exclusivamente na incorporação de informações contextuais e na estimação dos modelos explicativos.

A partir deste ponto, o projeto deixa de investigar a estrutura interna dos dados individuais e passa a analisar como essa estrutura relaciona-se aos contextos institucionais e partidários nos quais os indivíduos estão inseridos.

---

# Etapas Concluídas

## Organização da infraestrutura computacional

Foi construída uma estrutura permanente de diretórios destinada à execução de toda a pesquisa.

Essa estrutura separa claramente:

- bases brutas;
- bases processadas;
- bases integradas;
- notebooks;
- figuras;
- resultados;
- scripts reutilizáveis;
- documentação.

Essa organização constitui parte integrante da estratégia de reprodutibilidade adotada pelo projeto.

---

## Preparação do World Values Survey

Foi produzida uma versão analítica da base do World Values Survey.

Essa etapa compreendeu:

- seleção das variáveis relevantes;
- tratamento dos códigos de ausência;
- harmonização das escalas;
- construção dos indicadores derivados;
- exportação das bases processadas.

A partir desse momento, as análises posteriores passaram a utilizar exclusivamente as bases derivadas.

---

## Construção dos Indicadores

Foram operacionalizados indicadores correspondentes às principais dimensões discutidas na fundamentação teórica da pesquisa.

Entre elas destacam-se:

- nacionalismo;
- orgulho nacional;
- disposição para o conflito;
- hostilidade a grupos externos;
- autoritarismo;
- confiança institucional;
- religiosidade;
- participação política;
- interesse por política;
- percepção de ameaça;
- pertencimento coletivo;
- orientação normativa.

Esses indicadores constituíram a matéria-prima utilizada na análise fatorial.

---

## Experimento 3 — Estruturas Latentes

Foi realizada Análise Fatorial Exploratória utilizando os indicadores construídos anteriormente.

A adequação da matriz de correlações foi avaliada por meio de:

- índice KMO;
- teste de esfericidade de Bartlett;
- análise paralela de Horn;
- scree plot.

A solução final identificou oito fatores de primeira ordem.

Posteriormente foi conduzida nova análise fatorial produzindo três fatores de segunda ordem.

Esses fatores sintetizam estruturas afetivas mais amplas presentes na população analisada.

Os fatores de segunda ordem passaram a constituir a representação reduzida dos indivíduos para todas as análises subsequentes.

---

## Experimento 4 — Perfis Afetivos

Os três fatores de segunda ordem foram utilizados como entrada para a identificação de tipologias de indivíduos.

Foram comparadas diferentes soluções de clusterização.

A escolha do número de grupos baseou-se simultaneamente em critérios estatísticos e interpretabilidade substantiva.

A solução adotada foi composta por três perfis.

Esses perfis representam configurações distintas de orientação afetiva e política observadas nos dados.

Sua interpretação permanece provisória e poderá ser refinada após a incorporação das variáveis contextuais.

---

# Validação

Diversos procedimentos foram empregados para avaliar a consistência da solução obtida.

Entre eles:

- distribuição dos clusters;
- análise dos centroides;
- matriz de distâncias;
- coesão interna;
- projeção em componentes principais;
- teste do qui-quadrado;
- cálculo do V de Cramér;
- análise dos resíduos padronizados.

Os resultados indicaram que os perfis identificados apresentam consistência estatística e distinguem grupos empiricamente diferenciados.

Também foi observada associação estatisticamente significativa entre país e perfil, indicando que a distribuição dos grupos não ocorre aleatoriamente entre os diferentes contextos nacionais.

Esse resultado reforça a importância da etapa seguinte da pesquisa, dedicada à incorporação de variáveis institucionais.

---

# Arquivos Consolidados

Até esta etapa foram produzidos, entre outros, os seguintes arquivos permanentes:

## Bases processadas

- wvs_tese.parquet

- wvs_indicadores_w7.parquet

- afe8_scores.parquet

- afe_second_order_scores.parquet

- experimento4_perfis.parquet

- experimento4_coords_pca.parquet

## Bases integradas

- base_multinivel.parquet

- vparty_americas.parquet

- vparty_agregado.parquet

- vparty_contexto.parquet

- base_analitica.parquet

---

## Resultados

Foram exportadas todas as tabelas produzidas durante os Experimentos 3 e 4.

Essas tabelas encontram-se organizadas em seus respectivos diretórios e constituem a documentação quantitativa das análises realizadas.

---

## Figuras

Todas as figuras produzidas durante os experimentos encontram-se armazenadas em diretórios específicos, preservando uma correspondência direta entre notebook, resultados e documentação gráfica.

---

# Decisões Consolidadas

As seguintes decisões metodológicas passam a ser consideradas definitivas para o restante da pesquisa, salvo revisão explicitamente justificada.

- A unidade principal de análise permanece sendo o indivíduo.

- Os fatores de segunda ordem constituem a representação reduzida oficial dos indivíduos.

- A solução contendo três perfis foi adotada como solução analítica principal.

- Os experimentos concluídos não deverão ser recalculados durante as etapas subsequentes, exceto diante de necessidade metodológica claramente fundamentada.

- Todas as etapas futuras deverão utilizar exclusivamente os arquivos persistidos em disco, evitando dependências de objetos presentes apenas na memória do ambiente computacional.

- A integração temporal com o V-Party utiliza sempre a eleição imediatamente anterior ou coincidente ao ano da entrevista.

- As medidas partidárias permanecem contínuas e ponderadas pelo peso eleitoral dos partidos, evitando classificações dicotômicas baseadas em limiares arbitrários.

- Os indicadores de cobertura deverão permanecer na base analítica para utilização em análises de sensibilidade e robustez.

- A `base_analitica.parquet` constitui a base oficial para todas as análises subsequentes da tese.

---

# Situação Atual

A pesquisa concluiu a construção da base analítica definitiva, integrando dados individuais do World Values Survey, indicadores institucionais do Varieties of Democracy (V-Dem) e características dos sistemas partidários provenientes do V-Party.

A infraestrutura empírica da tese encontra-se consolidada, documentada e reproduzível.

As etapas futuras dedicar-se-ão exclusivamente à exploração analítica dessa base integrada.


---

# Próxima Etapa

O próximo notebook iniciará a fase de análises relacionais da pesquisa.

Essa etapa utilizará diretamente a `base_analitica.parquet` para explorar as relações entre dimensões individuais, contextos institucionais e sistemas partidários.

As principais técnicas previstas incluem:

- Multiple Correspondence Analysis (MCA);
- Multiple Factor Analysis (MFA);
- Correspondence Analysis (CA);
- modelos multinível;
- análises relacionais de perfis políticos.

# Política de Manutenção da Documentação

Este documento constitui o registro mestre da arquitetura científica e computacional do projeto. Sua função não é apenas descrever o estado inicial da pesquisa, mas acompanhar continuamente sua evolução metodológica e operacional.

Sempre que uma etapa relevante da pesquisa for concluída, recomenda-se revisar este documento para garantir que ele permaneça uma representação fiel do estado atual do projeto.

Em particular, deverão ser atualizados, quando pertinente:

- o estado atual da pesquisa;
- as etapas concluídas;
- os notebooks implementados;
- o pipeline analítico;
- as bases produzidas;
- os produtos exportados;
- as decisões metodológicas consolidadas;
- as convenções adotadas;
- as próximas etapas previstas.

Alterações metodológicas significativas, mudanças na arquitetura computacional, inclusão de novas bases de dados, substituição de procedimentos analíticos ou revisão de decisões previamente estabelecidas deverão ser registradas neste documento, acompanhadas de breve justificativa e, quando aplicável, da atualização correspondente no `CHANGELOG.md`.

A manutenção deste documento deve ocorrer preferencialmente ao término de cada notebook ou módulo analítico, de modo que o projeto permaneça permanentemente documentado, reproduzível e auditável.

Consequentemente, antes do início de qualquer nova etapa da pesquisa, recomenda-se a leitura integral deste documento, utilizando-o como referência principal para compreender o estado do projeto, evitar redundâncias analíticas, preservar decisões já consolidadas e assegurar a continuidade metodológica entre as diferentes fases da investigação.

Este documento deve ser tratado como a fonte de referência mais atualizada sobre a arquitetura do projeto, complementando a documentação existente nos notebooks, nos arquivos exportados e no manuscrito da tese.

# Apêndice A — Convenções para Continuidade do Projeto

Este projeto foi concebido para evoluir durante todo o desenvolvimento da tese.

Ao implementar uma nova etapa, recomenda-se observar as seguintes convenções:

- Não modificar bases brutas.

- Não recalcular resultados já consolidados sem justificativa metodológica.

- Toda nova etapa deve produzir arquivos persistentes.

- Cada notebook deve possuir objetivo único.

- Todo notebook deve iniciar carregando apenas arquivos gravados em disco.

- Ao término de cada notebook:

    • atualizar PROJECT.md;

    • atualizar CHANGELOG.md;

    • exportar tabelas;

    • exportar figuras;

    • registrar novos produtos gerados.

Antes de iniciar qualquer novo notebook, recomenda-se consultar este documento para compreender o estado atual da pesquisa e preservar a continuidade metodológica do projeto.
