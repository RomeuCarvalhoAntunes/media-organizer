# Plano 04 — Parser de séries, especiais e anime absoluto

## Objetivo
Interpretar releases episódicos sem alterar arquivos.

## Casos obrigatórios
```text
Jujutsu.Kaisen.S02E04.1080p.BluRay.Opus2.0.x265.DUAL-Anitsu.mkv
→ title=Jujutsu Kaisen, season=2, episode=4
→ S02E04 - Jujutsu Kaisen.mkv
```

Episódio múltiplo:
```text
Show.S01E01E02.1080p.mkv
→ S01E01-E02 - Show.mkv
```

Especial:
```text
Show.S00E01...
→ Especiais/S00E01 - Show.mkv
```

Absoluto:
```text
One.Piece.1123.1080p...
→ absolute_episode=1123
→ 1123 - One Piece.mkv
```

## Regra de segurança
Numeração absoluta só deve ser assumida quando houver evidência suficiente. Casos ambíguos devem resultar em `REVIEW_REQUIRED`.

## Fora do escopo
- consulta externa;
- título individual de episódio;
- move/rename;
- GUI.

## Testes
Cobrir temporadas/episódios de um e vários dígitos, S00, episódios múltiplos, absoluto e ambiguidades.

## Teste manual
Fornecer comando Docker para o usuário colar nomes de releases e visualizar parse + nome proposto.

## Critério de aceite
Os padrões definidos em Requirements/Naming são reproduzidos sem modificar filesystem.

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
