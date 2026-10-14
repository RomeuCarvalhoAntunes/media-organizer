# Plano 03 — Parser de filmes

## Objetivo
Interpretar nomes reais de releases de filmes e separar título de metadata técnica.

## Casos-base obrigatórios
```text
John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv
→ John Wick Chapter 4

Mickey.17.2025.1080p.AMZN.WEB-DL.DDP5.1.H264.DUAL-C76.mkv
→ Mickey 17

A.Favorita.2019.1080p.BluRay.x264-SPARKS.DUAL-RK.mkv
→ A Favorita
```

## Escopo
- tokenização de nomes;
- detecção cuidadosa de ano;
- tags técnicas extensíveis;
- resolução, source, codecs, áudio, HDR/DV, Atmos, idioma/release quando reconhecíveis;
- título provável;
- preservação da extensão;
- resultado conservador quando ambíguo.

## Regra importante
Números no título não podem ser removidos apenas por serem números. `Mickey 17` deve permanecer `Mickey 17`.

## Fora do escopo
- consulta externa;
- séries/anime;
- filesystem real.

## Testes
Além dos três casos-base, criar casos para títulos numéricos e anos ambíguos. Ambiguidade deve poder resultar em revisão em vez de nome inventado.

## Teste manual
Fornecer comando/entry point de desenvolvimento que aceite uma lista de filenames e imprima o parse, rodando dentro do Docker.

## Critério de aceite
Os exemplos reais do usuário produzem os títulos esperados e nenhuma operação de filesystem ocorre.

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
