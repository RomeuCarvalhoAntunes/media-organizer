# Safety and Filesystem Invariants

## Objetivo

Evitar perda, sobrescrita ou alteração incorreta de arquivos.

## Invariantes obrigatórios

1. Nunca sobrescrever arquivo silenciosamente.
2. Nunca excluir automaticamente arquivos de vídeo.
3. Nunca excluir automaticamente legendas.
4. Nunca excluir automaticamente arquivos desconhecidos.
5. Nunca remover diretório não vazio.
6. Nunca modificar o filesystem durante scan.
7. Nunca modificar o filesystem durante parsing.
8. Nunca modificar o filesystem durante planning.
9. Toda alteração deve existir previamente no plano aprovado.
10. Conflitos bloqueiam apenas as operações afetadas.
11. Itens ambíguos viram `REVIEW_REQUIRED`.
12. Toda alteração aplicada deve ser registrada no log.
13. O destino deve ser revalidado imediatamente antes de cada mudança.
14. Falha em um item não deve provocar perda dos demais.
15. Rollback é best-effort e nunca deve introduzir sobrescrita.

## Operações permitidas

- criar diretório;
- mover arquivo;
- renomear arquivo;
- remover diretório vazio.

## Operações proibidas no Alfa

- sobrescrever;
- apagar mídia;
- apagar arquivos desconhecidos;
- excluir duplicados automaticamente;
- substituir uma versão por outra;
- remover pasta com conteúdo.

## Conflitos

Qualquer destino já existente deve gerar `CONFLICT`.

## Duplicidades

Possíveis duplicados devem ser listados e preservados.

## Validação

Os invariantes deste documento devem ter testes automatizados.
