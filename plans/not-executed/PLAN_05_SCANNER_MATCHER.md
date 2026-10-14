# Plano 05 — Scanner recursivo, classificação e associação de legendas

## Objetivo
Ler uma árvore de diretórios de forma read-only e construir inventário lógico dos arquivos.

## Escopo
- scan recursivo;
- classificação por extensão;
- vídeo principal candidato;
- legendas;
- arquivos adicionais;
- samples/trailers/extras;
- associação segura de legenda a vídeo;
- múltiplas legendas;
- itens ignorados/revisão quando associação for ambígua.

## Segurança
Scanner e matcher são estritamente read-only.

## Testes
Usar somente diretórios temporários/fixtures.
Cobrir:
- arquivo solto;
- pasta de filme;
- série em subpastas profundas;
- uma legenda;
- múltiplas legendas;
- legenda órfã;
- sample/trailer;
- jpg/nfo/txt;
- extensão desconhecida.

## Teste manual
Criar uma árvore de teste descartável, fornecendo comandos exatos. O usuário deve poder executar scan e conferir inventário sem qualquer mudança nos arquivos.

## Critério de aceite
A árvore é inventariada recursivamente e permanece byte/path-identical após o scan.

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
