# Requirements

## 1. Visão geral

Media Organizer é uma aplicação desktop portátil para Windows destinada ao uso pessoal do proprietário do projeto.

O programa organiza filmes, séries, animes e legendas em uma pasta ou unidade local.

O Alfa é o produto final pretendido. O projeto não precisa ser preparado para uma plataforma maior.

## 2. Requisitos principais

A aplicação deve:

- permitir selecionar uma pasta ou unidade;
- fazer varredura recursiva;
- detectar arquivos de vídeo;
- detectar legendas;
- interpretar nomes comuns de releases;
- distinguir filmes, séries, especiais e anime com numeração absoluta;
- associar legendas aos respectivos vídeos;
- gerar uma estrutura de diretórios limpa;
- criar diretórios quando necessário;
- mover arquivos;
- renomear arquivos;
- detectar possíveis duplicidades;
- detectar conflitos;
- listar ignorados;
- listar itens que exigem revisão;
- mostrar preview antes de qualquer alteração;
- aplicar somente operações aprovadas;
- remover diretórios que ficarem realmente vazios;
- gerar log da execução;
- gerar relatório final.

## 3. Aplicação stateless

Não usar banco de dados.

Não manter catálogo persistente.

Cada execução analisa o filesystem atual novamente.

Persistência permitida:

- logs de execução;
- arquivos normais do projeto/configuração estritamente necessários ao funcionamento.

## 4. Filmes

Todo filme deve ficar dentro de pasta própria.

Formato:

```text
Nome do Filme/
└── Nome do Filme.ext
```

Exemplo:

```text
Mickey 17/
└── Mickey 17.mkv
```

O ano não aparece no nome final.

## 5. Séries

Formato:

```text
Nome da Série/
└── Nª - Temporada/
    ├── SxxExx - Nome da Série.ext
    └── ...
```

Exemplo:

```text
Jujutsu Kaisen/
└── 2ª - Temporada/
    ├── S02E04 - Jujutsu Kaisen.mkv
    └── S02E05 - Jujutsu Kaisen.mkv
```

O nome individual do episódio não aparece no nome final.

## 6. Episódios múltiplos

Exemplo de entrada:

```text
Show.S01E01E02.1080p.mkv
```

Saída:

```text
S01E01-E02 - Nome da Série.mkv
```

## 7. Especiais

`S00` deve usar a pasta:

```text
Nome da Série/
└── Especiais/
    ├── S00E01 - Nome da Série.mkv
    └── S00E02 - Nome da Série.mkv
```

Não usar `0ª - Temporada`.

## 8. Anime com numeração absoluta

Formato:

```text
Nome do Anime/
├── 1121 - Nome do Anime.mkv
├── 1122 - Nome do Anime.mkv
└── 1123 - Nome do Anime.mkv
```

Não criar pasta intermediária `Episódios`.

Não converter automaticamente numeração absoluta para `SxxExx`.

## 9. Legendas

Formatos inicialmente reconhecidos:

- `.srt`
- `.ass`
- `.ssa`
- `.sub`
- `.idx`
- `.sup`

Uma legenda:

```text
A Favorita.mkv
A Favorita.srt
```

Múltiplas:

```text
A Favorita.mkv
A Favorita.pt-BR.srt
A Favorita.en.srt
A Favorita.pt-BR.forced.srt
```

Para série:

```text
S02E04 - Jujutsu Kaisen.mkv
S02E04 - Jujutsu Kaisen.pt-BR.srt
```

## 10. Parsing

Exemplo:

```text
John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv
```

O parser deve conseguir separar, quando possível:

- título;
- ano;
- resolução;
- fonte;
- codec de vídeo;
- codec de áudio;
- canais;
- Atmos;
- HDR/Dolby Vision;
- idioma;
- release group;
- container.

Esses metadados servem apenas para análise, parsing, preview e diagnóstico. Não precisam ser persistidos.

## 11. Tags técnicas

A lista de tags deve ser extensível.

Exemplos:

- `720p`
- `1080p`
- `2160p`
- `4K`
- `BluRay`
- `WEB-DL`
- `WEBRip`
- `REMUX`
- `AMZN`
- `NF`
- `MAX`
- `x264`
- `x265`
- `H264`
- `H265`
- `HEVC`
- `AV1`
- `AAC`
- `AC3`
- `EAC3`
- `DDP`
- `DTS`
- `TrueHD`
- `Opus`
- `Atmos`
- `HDR`
- `HDR10`
- `DV`
- `DUAL`
- `MULTI`
- `PT-BR`
- `ENG`
- `10bit`
- `8bit`

## 12. Consulta externa

Nenhuma consulta externa é requisito do Alfa.

Não depender de IMDb, Google, TMDB ou qualquer API para o fluxo principal funcionar.

O programa deve organizar com base no nome local e nas regras definidas.

## 13. Scanner

A varredura é recursiva em toda a árvore abaixo da raiz selecionada.

Arquivos podem estar em qualquer profundidade.

Scanner é read-only.

## 14. Agrupamento

Antes de planejar operações, construir representação lógica de filmes, séries, temporadas, episódios e legendas.

Não tratar arquivos relacionados como itens independentes quando houver evidência suficiente para agrupá-los.

## 15. Extras, trailers e samples

Quando identificados como `sample`, `trailer`, `extra`, `extras`, `featurette`, `behind the scenes` ou equivalentes:

- preservar;
- não tratar como filme principal;
- não excluir;
- listar em revisão/ignorados quando necessário.

## 16. Outros arquivos

Arquivos como `.jpg`, `.jpeg`, `.png`, `.nfo` e `.txt` não devem ser apagados automaticamente.

Se não houver regra específica, deixar no local e registrar como ignorado.

## 17. Pastas vazias

Remover apenas pastas realmente vazias após as operações.

Nunca remover diretório que ainda contenha qualquer arquivo.

## 18. Duplicidades

Não implementar gerenciamento sofisticado de versões duplicadas.

Quando dois itens aparentarem representar a mesma obra ou convergirem para o mesmo destino, marcar como `POSSIBLE_DUPLICATE`.

Mostrar lista completa ao usuário.

Não sobrescrever.

## 19. Conflitos

Se o destino já existir, bloquear a operação.

Estado:

`CONFLICT`

O usuário deve conseguir ver a lista completa.

## 20. Revisão necessária

Usar `REVIEW_REQUIRED` quando a interpretação não for segura.

Exemplos:

- título ambíguo;
- ano ambíguo;
- série versus filme inconclusivo;
- legenda sem vídeo correspondente;
- vários vídeos candidatos;
- numeração absoluta incerta;
- operação estrutural arriscada.

Itens em revisão não são alterados automaticamente.

## 21. Estados mínimos

- `READY`
- `UNCHANGED`
- `POSSIBLE_DUPLICATE`
- `CONFLICT`
- `IGNORED`
- `REVIEW_REQUIRED`
- `ERROR`

Nenhum item deve desaparecer do relatório.

## 22. Preview

Antes de executar, mostrar claramente origem e destino propostos.

Nada deve ser alterado antes da aprovação.

## 23. Executor

Operações permitidas:

- `CREATE_DIRECTORY`
- `MOVE`
- `RENAME`
- `REMOVE_EMPTY_DIRECTORY`

Somente o executor pode modificar o filesystem.

## 24. Revalidação

Antes de cada alteração, revalidar o estado do destino.

Uma operação planejada pode deixar de ser segura entre planning e apply.

## 25. Rollback best-effort

Durante a execução, manter em memória as operações já aplicadas.

Em caso de erro, tentar reverter quando for seguro.

Falhas de rollback devem ser registradas no log.

## 26. Log

Cada execução que aplicar alterações deve produzir log com:

- raiz analisada;
- itens identificados;
- diretórios criados;
- moves;
- renames;
- pastas vazias removidas;
- duplicidades;
- conflitos;
- ignorados;
- itens em revisão;
- erros.

## 27. Relatório final

Mostrar contagens e listas para:

- organizados;
- sem alteração;
- possíveis duplicados;
- conflitos;
- ignorados;
- revisão necessária;
- erros.

## 28. Interface

Desktop Windows simples.

Fluxo:

```text
Selecionar pasta/unidade
→ Analisar
→ Ver resumo
→ Ver alterações
→ Aplicar
→ Ver resultado
→ Abrir log
```

Funcionalidade e clareza são mais importantes que aparência sofisticada.

## 29. Distribuição

Preferência:

```text
Media Organizer.exe
```

Se não for viável:

```text
Media Organizer.zip
├── Media Organizer.exe
└── dependências necessárias
```

O usuário final não deve precisar instalar Python ou Docker.

## 30. Desenvolvimento

Docker é obrigatório desde o bootstrap do projeto.

O ambiente Docker deve suportar:

- testes;
- lint;
- type checking;
- parser;
- planner;
- domínio;
- demais componentes que não dependam diretamente da GUI Windows.

Também deve existir forma documentada de executar a GUI nativamente no Windows.

## 31. Critério de conclusão

O Alfa está concluído quando todos os requisitos acima funcionarem de forma segura em um cenário real de teste e os testes automatizados passarem.
