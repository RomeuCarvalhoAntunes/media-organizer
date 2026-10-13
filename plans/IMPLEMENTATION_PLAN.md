# Implementation Plan

## Premissa

Docker não é etapa final. O projeto começa dockerizado.

A cada marco, os comandos de testes, lint e type checking devem continuar funcionando dentro do ambiente Docker.

## Marco 0 — Bootstrap + Docker

Objetivo: preparar o repositório para desenvolvimento antes da lógica funcional.

Entregar:

- estrutura de diretórios;
- documentação;
- `pyproject.toml`;
- `.gitignore`;
- `Dockerfile`;
- `compose.yaml`;
- configuração inicial de testes;
- lint;
- type checking;
- comando documentado para rodar tudo via Docker;
- execução mínima nativa documentada para Windows.

Critério:

```text
docker compose build
docker compose run --rm app pytest
```

ou comandos equivalentes devem funcionar desde o início.

Nenhuma funcionalidade de organização precisa existir ainda.

## Marco 1 — Domain + Naming + Parser

Entregar:

- modelos internos simples;
- enums de estados;
- reconhecimento de extensões;
- sanitização Windows;
- regras de naming;
- parser de filmes;
- parser de séries;
- episódios múltiplos;
- especiais;
- anime absoluto;
- tags técnicas;
- testes.

Ainda sem GUI e sem alterar arquivos reais.

## Marco 2 — Scanner + Matcher + Grouping

Entregar:

- scan recursivo;
- classificação de arquivos;
- associação de vídeo e legenda;
- agrupamento por obra/série/temporada;
- identificação de arquivos ignorados;
- testes com filesystem temporário.

## Marco 3 — Planner + Validation

Entregar transformação:

```text
filesystem atual
→
plano de operações
```

Implementar:

- diretórios a criar;
- moves;
- renames;
- diretórios potencialmente removíveis;
- conflitos;
- possíveis duplicidades;
- revisão necessária;
- unchanged;
- ignored.

Nenhuma operação real ainda.

## Marco 4 — Executor + Log

Implementar:

- create directory;
- move;
- rename;
- remove empty directory;
- revalidação imediatamente antes da operação;
- log;
- rollback best-effort;
- relatório de erros.

Cobrir regras de segurança com testes.

## Marco 5 — GUI Windows

Adicionar:

- seleção de pasta/unidade;
- analisar;
- progresso;
- resumo;
- preview;
- listas de:
  - duplicados;
  - conflitos;
  - ignorados;
  - revisão;
  - erros;
- aplicar;
- resultado;
- abrir log.

GUI não deve duplicar regra de negócio.

## Marco 6 — Build portátil

Configurar build Windows.

Prioridade:

```text
Media Organizer.exe
```

Fallback:

```text
Media Organizer.zip
```

Documentar processo de build.

## Marco 7 — Validação final

Testar em cópia controlada de releases reais.

Validar:

- filmes soltos;
- filmes em pastas;
- legendas;
- múltiplas legendas;
- séries;
- especiais;
- episódio múltiplo;
- anime absoluto;
- conflitos;
- duplicidades;
- ignorados;
- pasta vazia;
- falha parcial;
- log.

## Regra de escopo

Não adicionar:

- banco de dados;
- servidor web;
- login;
- conta;
- API externa obrigatória;
- download;
- streaming;
- serviço em background.

Se não for necessário para cumprir o Alfa, não implementar.
