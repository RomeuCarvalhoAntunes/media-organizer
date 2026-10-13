# Testing Strategy

## 1. Objetivo

Garantir que parsing e operações de filesystem sejam previsíveis e seguras.

## 2. Testes unitários obrigatórios

### Filmes

```text
John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv
```

deve gerar título provável:

```text
John Wick Chapter 4
```

### Mickey 17

```text
Mickey.17.2025.1080p.AMZN.WEB-DL.DDP5.1.H264.DUAL-C76.mkv
```

deve preservar `17` como parte do título.

### Série

```text
Jujutsu.Kaisen.S02E04.1080p.BluRay.Opus2.0.x265.DUAL-Anitsu.mkv
```

deve produzir:

- título: `Jujutsu Kaisen`
- temporada: `2`
- episódio: `4`

Nome final:

```text
S02E04 - Jujutsu Kaisen.mkv
```

### Anime absoluto

```text
One.Piece.1123.1080p...
```

quando reconhecido com segurança deve produzir:

- título: `One Piece`
- episódio absoluto: `1123`

Nome:

```text
1123 - One Piece.mkv
```

### Sanitização

```text
John Wick 4: Baba Yaga
```

deve virar:

```text
John Wick 4 - Baba Yaga
```

### Legendas

Vídeo e legenda associada devem produzir basenames compatíveis.

### Episódio múltiplo

`S01E01E02` deve resultar em:

```text
S01E01-E02 - Nome da Série.ext
```

## 3. Testes de planner

O planner não pode modificar o filesystem.

Dado um fixture, verificar apenas as operações propostas.

## 4. Testes de executor

Usar diretórios temporários.

Verificar:

- criação de pasta;
- move;
- rename;
- bloqueio de sobrescrita;
- remoção somente de pasta vazia;
- comportamento em falha parcial;
- log.

## 5. Invariantes

Cada regra de `SAFETY.md` deve possuir cobertura de teste adequada.

## 6. Docker

A suíte padrão deve rodar dentro do ambiente Docker desde o início do projeto.

O mesmo ambiente deve executar lint e type checking.

## 7. Teste real

Antes de rodar contra biblioteca importante:

1. criar cópia de teste;
2. incluir releases reais;
3. analisar;
4. revisar plano;
5. aplicar;
6. conferir estrutura;
7. conferir conflitos;
8. conferir log.

Nunca usar biblioteca pessoal real como fixture automatizado.
