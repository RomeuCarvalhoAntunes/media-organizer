# Architecture

## 1. Princípio

A arquitetura deve ser simples, local e adequada a uma aplicação pessoal.

Não projetar para servidor, SaaS, contas, banco ou múltiplos usuários.

## 2. Fluxo

```text
Filesystem
   ↓
Scanner
   ↓
Parser
   ↓
Grouping
   ↓
Naming
   ↓
Planner
   ↓
Validation
   ↓
Preview
   ↓
Executor
   ↓
Log / Report
```

Somente o Executor pode modificar o filesystem.

## 3. Componentes

### Scanner

Responsável por:

- percorrer a raiz recursivamente;
- identificar extensões relevantes;
- retornar entradas do filesystem.

Read-only.

### Parser

Responsável por:

- interpretar nomes;
- extrair título;
- extrair ano;
- detectar série/temporada/episódio;
- detectar numeração absoluta;
- reconhecer tags técnicas.

Read-only.

### Grouping

Responsável por agrupar:

- vídeo + legenda;
- episódios da mesma série;
- temporadas;
- arquivos que aparentemente pertencem à mesma obra.

### Naming

Responsável apenas por transformar uma identidade em nomes finais válidos.

Inclui sanitização Windows.

### Planner

Produz operações propostas, sem executá-las.

Exemplo:

```text
CREATE_DIRECTORY
MOVE
RENAME
REMOVE_EMPTY_DIRECTORY
```

### Validator

Detecta:

- conflitos;
- duplicidades;
- destinos inválidos;
- itens que exigem revisão.

### Executor

Executa somente operações aprovadas.

Antes de cada operação, revalida filesystem.

### Logger

Registra o que foi analisado e aplicado.

### UI

Interface desktop simples.

Não deve conter regras de domínio.

## 4. Estrutura sugerida

```text
src/
└── media_organizer/
    ├── domain/
    ├── scanner/
    ├── parser/
    ├── matcher/
    ├── naming/
    ├── planner/
    ├── executor/
    ├── logging/
    └── ui/
```

Não criar módulos para funcionalidades fora do Alfa.

## 5. Dependências

Preferir biblioteca padrão e dependências pequenas.

Evitar frameworks de backend web.

## 6. Docker

Docker faz parte da arquitetura de desenvolvimento desde o início.

O container deve executar, no mínimo:

- testes;
- lint;
- type checking;
- código de domínio;
- parser;
- planner.

A GUI Windows poderá ser validada nativamente.

## 7. Distribuição

Build portátil para Windows.

Prioridade:

1. single executable;
2. ZIP portátil como fallback.
