# AGENTS.md

## Objetivo

Este repositório contém o Media Organizer, uma aplicação desktop simples e portátil para Windows.

Antes de alterar código ou estrutura, leia:

- `docs/REQUIREMENTS.md`
- `docs/NAMING.md`
- `docs/SAFETY.md`
- `docs/ARCHITECTURE.md`
- `docs/TESTING.md`
- `plans/IMPLEMENTATION_PLAN.md`

## Regras para o Codex

1. Trate o Alfa como o produto final pretendido. Não introduza funcionalidades futuras sem necessidade.
2. Não adicionar banco de dados, servidor web, login, conta, backend remoto ou serviços em background.
3. O projeto deve ser desenvolvido desde o primeiro momento em ambiente Docker reproduzível.
4. A GUI Windows pode exigir execução nativa, mas domínio, parser, planner, testes, lint e type checking devem funcionar em Docker.
5. Nunca modificar o filesystem durante scan ou planning.
6. Nunca sobrescrever arquivos silenciosamente.
7. Nunca apagar arquivos de mídia, legendas ou arquivos desconhecidos automaticamente.
8. Só remover diretórios realmente vazios.
9. Itens ambíguos devem virar `REVIEW_REQUIRED`.
10. Toda alteração executada deve aparecer no log.
11. Preferir implementação simples e legível.
12. Não criar abstrações para funcionalidades que não fazem parte do Alfa.
13. Não adicionar integração externa obrigatória.
14. Parser, planner e executor devem continuar desacoplados.
15. Escrever ou atualizar testes junto de cada mudança funcional.

## Fluxo esperado

```text
scan
→ parse
→ group
→ naming
→ plan
→ validate
→ preview
→ apply
→ log/report
```

Somente a etapa `apply` pode modificar o filesystem.
