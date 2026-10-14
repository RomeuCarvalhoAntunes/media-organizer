# Plano 02 — Domínio, extensões e regras de naming

## Objetivo
Implementar os modelos internos mínimos e o motor puro de nomenclatura/sanitização, sem scanner real e sem alterar filesystem.

## Escopo
Implementar:
- tipos de mídia necessários ao Alfa;
- estados `READY`, `UNCHANGED`, `POSSIBLE_DUPLICATE`, `CONFLICT`, `IGNORED`, `REVIEW_REQUIRED`, `ERROR`;
- representação simples de filme, série/episódio, especial, episódio absoluto e legenda;
- extensões suportadas;
- sanitização Windows;
- naming de filmes;
- naming de séries;
- episódios múltiplos;
- especiais;
- anime absoluto;
- naming de legendas.

## Regras obrigatórias
Exemplos:
```text
John Wick Chapter 4/
└── John Wick Chapter 4.mkv

Jujutsu Kaisen/
└── 2ª - Temporada/
    └── S02E04 - Jujutsu Kaisen.mkv

One Piece/
└── 1123 - One Piece.mkv
```

Não incluir nome individual do episódio.

## Fora do escopo
- parsing de release;
- scan;
- move/rename real;
- GUI.

## Testes automatizados
Cobrir extensivamente `docs/NAMING.md`, inclusive:
- caracteres inválidos Windows;
- espaços/hífens duplicados;
- nomes reservados;
- filme;
- temporada;
- especial;
- episódio múltiplo;
- absoluto;
- legenda única/múltipla.

## Teste manual do usuário
Fornecer um comando simples dentro do Docker que demonstre entradas e nomes produzidos sem tocar em arquivos reais.

## Critério de aceite
Naming é determinístico, testado e independente de GUI/filesystem.

## Protocolo obrigatório do Codex

Antes de implementar:
1. Leia `AGENTS.md`.
2. Leia `docs/REQUIREMENTS.md`, `docs/NAMING.md`, `docs/SAFETY.md`, `docs/ARCHITECTURE.md` e `docs/TESTING.md`.
3. Leia `plans/IMPLEMENTATION_PLAN.md`.
4. Leia este plano por completo.
5. Inspecione o estado atual do repositório e os resultados dos planos anteriores.
6. Se encontrar contradição entre este plano e a documentação normativa, pare e reporte antes de alterar código.

Durante a implementação:
- Trabalhe somente no escopo deste plano.
- Preserve todos os invariantes de `docs/SAFETY.md`.
- Mantenha Docker funcional.
- Adicione/atualize testes junto com a implementação.
- Não antecipe funcionalidades de planos posteriores.
- Não faça mudanças destrutivas em mídia real do usuário.

Antes de concluir:
- Execute os testes automatizados relevantes.
- Execute lint e type checking configurados no projeto.
- Corrija falhas causadas por este plano.
- Revise `git diff` e informe alterações relevantes.
- Não faça commit/push automaticamente, salvo instrução explícita do usuário.

## Formato obrigatório da entrega

Ao terminar, responda com:

1. **Plano executado**
2. **O que foi implementado**
3. **Arquivos criados/alterados**
4. **Testes automatizados executados e resultados**
5. **Como o usuário deve testar manualmente**, com comandos/passos exatos
6. **Resultado esperado do teste manual**
7. **Limitações ou pontos de atenção**
8. **Status: AGUARDANDO VALIDAÇÃO DO USUÁRIO**

Depois disso, **PARE**. Não execute o próximo plano. O próximo plano só pode começar após o usuário validar explicitamente e solicitar sua execução.
