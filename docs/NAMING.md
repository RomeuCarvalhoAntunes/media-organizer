# Naming Rules

## 1. Objetivo

Definir regras únicas e previsíveis para nomes de pastas e arquivos gerados pelo Media Organizer.

## 2. Filmes

Pasta:

```text
Nome do Filme
```

Vídeo:

```text
Nome do Filme.ext
```

Exemplo:

```text
John Wick Chapter 4/
└── John Wick Chapter 4.mkv
```

O ano não aparece no nome final.

## 3. Séries

Pasta principal:

```text
Nome da Série
```

Temporada:

```text
Nª - Temporada
```

Episódio:

```text
SxxExx - Nome da Série.ext
```

Exemplo:

```text
Jujutsu Kaisen/
└── 2ª - Temporada/
    ├── S02E04 - Jujutsu Kaisen.mkv
    └── S02E05 - Jujutsu Kaisen.mkv
```

O título individual do episódio não é incluído.

## 4. Episódios múltiplos

Formato:

```text
S01E01-E02 - Nome da Série.ext
```

## 5. Especiais

Pasta:

```text
Especiais
```

Arquivo:

```text
S00E01 - Nome da Série.ext
```

Exemplo:

```text
Nome da Série/
└── Especiais/
    └── S00E01 - Nome da Série.mkv
```

## 6. Anime com numeração absoluta

Formato:

```text
Número Absoluto - Nome do Anime.ext
```

Exemplo:

```text
One Piece/
├── 1121 - One Piece.mkv
├── 1122 - One Piece.mkv
└── 1123 - One Piece.mkv
```

Não criar pasta `Episódios`.

Não converter automaticamente para `SxxExx`.

## 7. Legendas

### Uma legenda

Usar exatamente o mesmo basename do vídeo.

```text
A Favorita.mkv
A Favorita.srt
```

### Múltiplas legendas

Acrescentar idioma e qualificadores necessários.

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

## 8. Sanitização Windows

Caracteres proibidos:

```text
\ / : * ? " < > |
```

Devem ser substituídos por hífen ou removidos quando apropriado.

Exemplo:

```text
John Wick 4: Baba Yaga
```

vira:

```text
John Wick 4 - Baba Yaga
```

Também:

- remover espaços duplicados;
- evitar hífens duplicados;
- remover espaços e pontos inválidos no final;
- tratar nomes reservados do Windows;
- evitar nome vazio;
- preservar extensão correta.

## 9. Informações removidas do nome visível

Quando reconhecidas como metadata de release, remover do nome:

- ano;
- resolução;
- fonte;
- codec;
- áudio;
- canais;
- HDR;
- Dolby Vision;
- Atmos;
- idioma técnico do release;
- release group;
- tags técnicas.

Essas informações podem ser usadas durante parsing e preview, mas não devem aparecer no nome final.

## 10. Regra conservadora

Se não for possível produzir um nome com confiança suficiente, não inventar.

Marcar como `REVIEW_REQUIRED`.
