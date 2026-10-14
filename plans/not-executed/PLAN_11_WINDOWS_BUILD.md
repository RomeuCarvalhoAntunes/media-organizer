# Plano 11 — Build portátil para Windows

## Objetivo
Produzir a forma de distribuição pessoal do Media Organizer.

## Prioridade
1. `Media Organizer.exe` single executable.
2. ZIP portátil como fallback se single executable for inadequado.

## Escopo
- ferramenta de empacotamento adequada;
- build reproduzível/documentado;
- inclusão somente das dependências necessárias;
- inicialização sem Python instalado;
- documentação de build;
- smoke test do artefato.

## Não fazer
- instalador complexo;
- auto-update;
- assinatura de código como requisito;
- serviço Windows.

## Teste manual
O Codex deve instruir o usuário a testar o artefato em Windows fora do ambiente de desenvolvimento, preferencialmente em pasta limpa, usando biblioteca descartável.

## Critério de aceite
Aplicação abre e executa o fluxo principal sem exigir Python ou Docker no computador de uso.

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
