# Plano 06 — Agrupamento e Planner

## Objetivo
Converter o inventário lido em um plano completo de organização, ainda sem executar alterações.

## Escopo
- agrupar vídeo + legenda;
- agrupar episódios por série/temporada;
- reconhecer filmes soltos que precisam de pasta;
- produzir destinos finais;
- gerar operações propostas:
  - `CREATE_DIRECTORY`
  - `MOVE`
  - `RENAME`
  - `REMOVE_EMPTY_DIRECTORY` como operação condicional;
- identificar `UNCHANGED`;
- produzir preview estruturado.

## Regra central
O Planner é read-only. Nenhuma chamada de alteração de filesystem pode existir em seu caminho de execução.

## Testes
Criar fixtures representando os exemplos reais e verificar o plano exato esperado.

## Teste manual
Fornecer árvore descartável e comando para gerar plano em modo dry-run. O usuário deve comparar `antes` e `depois proposto` e confirmar que o filesystem real não mudou.

## Critério de aceite
Um plano completo e legível é produzido sem qualquer alteração.

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
