# Plano 08 — Executor, revalidação, log e rollback best-effort

## Objetivo
Introduzir pela primeira vez alterações reais de filesystem, inicialmente apenas em diretórios temporários/controlados.

## Escopo
- executar somente operações `READY` aprovadas;
- criar diretório;
- mover;
- renomear;
- remover somente diretório vazio;
- revalidar destino imediatamente antes de executar;
- log por execução;
- rollback best-effort em memória;
- relatório final.

## Segurança
Nunca testar inicialmente em biblioteca real.
Nunca sobrescrever.
Nunca apagar mídia.
Nunca apagar arquivo desconhecido.

## Testes automatizados
Usar `tmp`/fixtures e cobrir:
- execução normal;
- destino criado entre plan/apply;
- falha no meio;
- rollback possível;
- rollback impossível sem risco;
- pasta vazia;
- pasta não vazia;
- conteúdo do log.

## Teste manual
O Codex deve fornecer script/comandos para criar uma biblioteca descartável de teste, executar organização e mostrar:
1. árvore antes;
2. preview;
3. aplicação;
4. árvore depois;
5. log.

## Critério de aceite
Apenas o plano aprovado é aplicado, conflitos não sobrescrevem e o log permite auditar tudo.

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
