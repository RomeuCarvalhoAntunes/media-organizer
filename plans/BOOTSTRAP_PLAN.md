# Bootstrap Plan

## Objetivo

Preparar o repositório oficial do Media Organizer, inserir a documentação aprovada e criar a estrutura inicial de desenvolvimento.

Este plano é o primeiro trabalho a ser executado pelo Codex.

## Repositório oficial

```text
https://github.com/RomeuCarvalhoAntunes/media-organizer.git
```

Repository full name:

```text
RomeuCarvalhoAntunes/media-organizer
```

Branch principal:

```text
main
```

O repositório foi criado vazio, sem README, `.gitignore`, licença ou template.

## Passo 1 — Clonar

Clonar no diretório de trabalho atual:

```bash
git clone https://github.com/RomeuCarvalhoAntunes/media-organizer.git
cd media-organizer
```

Não criar outro repositório Git local.

Não alterar o remote `origin`.

Confirmar:

```bash
git remote -v
git branch --show-current
```

A branch deve ser `main`.

## Passo 2 — Inserir documentação fornecida

Colocar os arquivos fornecidos exatamente nestes caminhos:

```text
media-organizer/
├── README.md
├── AGENTS.md
├── docs/
│   ├── REQUIREMENTS.md
│   ├── NAMING.md
│   ├── SAFETY.md
│   ├── ARCHITECTURE.md
│   └── TESTING.md
└── plans/
    ├── BOOTSTRAP_PLAN.md
    └── IMPLEMENTATION_PLAN.md
```

Não reescrever o conteúdo sem necessidade.

## Passo 3 — Criar estrutura inicial

Criar:

```text
media-organizer/
├── src/
│   └── media_organizer/
│       ├── domain/
│       ├── scanner/
│       ├── parser/
│       ├── matcher/
│       ├── naming/
│       ├── planner/
│       ├── executor/
│       ├── logging/
│       └── ui/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── scripts/
├── docker/
└── .github/
    └── workflows/
```

Como Git não rastreia diretórios vazios, usar `.gitkeep` apenas onde necessário para preservar a estrutura inicial.

## Passo 4 — Docker desde o início

O desenvolvimento deve começar dockerizado.

Ainda no bootstrap, preparar a base necessária para que o próximo marco possa criar:

- `Dockerfile`;
- `compose.yaml`;
- `pyproject.toml`;
- testes;
- lint;
- type checking.

Se este bootstrap estiver sendo executado como parte do início efetivo do desenvolvimento, pode criar esses arquivos mínimos imediatamente, desde que sigam `IMPLEMENTATION_PLAN.md`.

Docker não deve ser tratado como uma etapa posterior.

## Passo 5 — Ler documentação antes de implementar

Antes de escrever funcionalidade, ler:

1. `README.md`
2. `docs/REQUIREMENTS.md`
3. `docs/NAMING.md`
4. `docs/SAFETY.md`
5. `docs/ARCHITECTURE.md`
6. `docs/TESTING.md`
7. `plans/IMPLEMENTATION_PLAN.md`
8. `AGENTS.md`

Se houver contradição, parar e apontar o conflito antes de implementar.

## Passo 6 — Commit inicial de documentação e estrutura

Após validar os arquivos:

```bash
git status
```

Criar commit inicial do conteúdo adicionado.

Mensagem sugerida:

```text
chore: bootstrap media organizer repository
```

Push para:

```text
origin/main
```

## Passo 7 — Não antecipar escopo

No bootstrap, não implementar funcionalidades completas de organização antes da documentação estar colocada e lida.

Não adicionar arquitetura de:

- banco;
- servidor;
- login;
- conta;
- API externa obrigatória;
- serviços em background.

## Resultado esperado

Ao final do bootstrap:

- repositório correto clonado;
- `origin` apontando para o GitHub oficial;
- branch `main`;
- documentação nos caminhos corretos;
- estrutura inicial criada;
- Docker tratado como premissa do projeto;
- commit inicial enviado ao repositório;
- projeto pronto para iniciar o Marco 0/1 do `IMPLEMENTATION_PLAN.md`.
