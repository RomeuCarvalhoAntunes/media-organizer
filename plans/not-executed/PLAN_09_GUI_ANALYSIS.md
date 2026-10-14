# Plano 09 — GUI: seleção, análise e preview

## Objetivo
Criar a primeira interface desktop Windows utilizável, ainda focada em análise e preview.

## Escopo
- escolher pasta/unidade;
- iniciar análise;
- mostrar progresso suficiente para não parecer travado;
- resumo de arquivos;
- preview;
- listas navegáveis de:
  - ready;
  - unchanged;
  - duplicados;
  - conflitos;
  - ignorados;
  - revisão;
  - erros.

## Regra
A GUI não contém regras de parsing/naming/planning; apenas chama os componentes existentes.

## Docker e Windows
Testes de domínio continuam em Docker. Documentar como iniciar/testar a GUI nativamente no Windows.

## Teste manual
Fornecer passos exatos para abrir a GUI no Windows e apontar para uma pasta descartável. Neste plano, o foco do teste é análise/preview.

## Critério de aceite
O usuário consegue selecionar uma pasta e compreender exatamente o que seria feito antes de aplicar.

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
