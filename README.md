# Media Organizer

Media Organizer é uma aplicação desktop portátil para Windows, de uso pessoal, criada para organizar automaticamente bibliotecas locais de filmes, séries, animes e legendas.

O projeto é deliberadamente simples: selecionar uma pasta ou unidade, analisar recursivamente os arquivos, propor uma organização segura, revisar conflitos e aplicar as alterações.

## Objetivo

Transformar estruturas de release desorganizadas em nomes limpos e previsíveis.

Exemplo:

```text
John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv
```

em:

```text
John Wick Chapter 4/
└── John Wick Chapter 4.mkv
```

Séries:

```text
Jujutsu Kaisen/
└── 2ª - Temporada/
    ├── S02E04 - Jujutsu Kaisen.mkv
    └── S02E05 - Jujutsu Kaisen.mkv
```

Anime com numeração absoluta:

```text
One Piece/
├── 1121 - One Piece.mkv
├── 1122 - One Piece.mkv
└── 1123 - One Piece.mkv
```

## Escopo

O Alfa é o produto final pretendido para uso pessoal. Não há plano de evoluir o projeto para servidor, contas, login, banco de dados persistente ou arquitetura web.

A aplicação deve ser:

- local;
- portátil;
- stateless;
- segura contra sobrescrita;
- desenvolvida desde o início em ambiente Docker;
- distribuída preferencialmente como um único `.exe`, com `.zip` como fallback.

## Repositório

- GitHub: `https://github.com/RomeuCarvalhoAntunes/media-organizer.git`
- Branch principal: `main`

## Documentação

Leia nesta ordem:

1. `docs/REQUIREMENTS.md`
2. `docs/NAMING.md`
3. `docs/SAFETY.md`
4. `docs/ARCHITECTURE.md`
5. `docs/TESTING.md`
6. `plans/IMPLEMENTATION_PLAN.md`
7. `plans/BOOTSTRAP_PLAN.md`
8. `AGENTS.md`

## Desenvolvimento

O ambiente de desenvolvimento usa Docker desde o início. A partir da raiz do
repositório, execute:

```bash
docker compose build
docker compose run --rm app pytest
docker compose run --rm app ruff check src tests
docker compose run --rm app mypy src tests
```

Cada container deve encerrar com código `0`. O pacote Python mínimo fica em
`src/media_organizer` e ainda não implementa regras de organização de mídia.

### Execução nativa no Windows

Com Python 3.11 ou superior instalado, a partir da raiz do repositório:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --editable ".[dev]"
.\.venv\Scripts\pytest.exe
.\.venv\Scripts\ruff.exe check src tests
.\.venv\Scripts\mypy.exe src tests
```

Esses comandos executam apenas a infraestrutura mínima do projeto e não
alteram nenhuma biblioteca de mídia.

Para demonstrar as regras de naming sem acessar ou modificar o filesystem,
execute:

```bash
docker compose run --rm app python scripts/naming_demo.py
```

Para demonstrar o parser de filmes com nomes próprios, execute:

```bash
docker compose run --rm app python scripts/movie_parser_demo.py \
  "John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv" \
  "Mickey.17.2025.1080p.AMZN.WEB-DL.DDP5.1.H264.DUAL-C76.mkv"
```
