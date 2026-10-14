# Plano 12 — Validação final controlada

## Objetivo
Validar o Alfa completo antes do uso na biblioteca real.

## Regra principal
Não modificar biblioteca original durante a primeira validação final. Usar cópia controlada.

## Matriz mínima de cenários
- filme solto;
- filme já em pasta;
- filme + legenda;
- múltiplas legendas;
- série com vários episódios;
- especial S00;
- episódio múltiplo;
- anime absoluto;
- sample/trailer/extra;
- jpg/nfo/txt;
- arquivo desconhecido;
- possível duplicado;
- conflito real de destino;
- item de revisão;
- pasta que fica vazia;
- pasta que permanece não vazia;
- falha parcial simulada;
- log e relatório.

## Tarefas
1. Rodar suíte automatizada completa em Docker.
2. Rodar lint/typecheck.
3. Criar pacote Windows atual.
4. Montar dataset de validação descartável.
5. Executar fluxo completo pela GUI.
6. Comparar árvore antes/depois.
7. Conferir todas as listas e o log.
8. Registrar qualquer desvio.
9. Corrigir apenas bugs necessários ao Alfa e repetir os testes afetados.

## Entrega
Produzir checklist final com PASS/FAIL para cada requisito relevante.

## Critério de aceite
Zero perda/sobrescrita de dados, comportamento esperado nos cenários e suíte automatizada verde.

Após este plano, o Codex deve parar e aguardar a decisão do usuário sobre uso na biblioteca pessoal.

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
