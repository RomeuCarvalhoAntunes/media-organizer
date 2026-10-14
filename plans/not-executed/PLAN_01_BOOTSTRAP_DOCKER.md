# Plano 01 — Bootstrap e ambiente Docker

## Objetivo
Transformar o repositório documental em um projeto Python mínimo, reproduzível e dockerizado, sem implementar ainda regras de organização de mídia.

## Pré-requisitos
- Repositório `RomeuCarvalhoAntunes/media-organizer` clonado.
- Documentação inicial presente.
- Branch `main`.

## Escopo
Criar/configurar:
- `pyproject.toml`;
- `.gitignore`;
- `Dockerfile`;
- `compose.yaml`;
- pacote Python mínimo em `src/media_organizer`;
- infraestrutura de `pytest`;
- lint;
- type checking;
- comandos documentados para desenvolvimento Docker;
- execução Python mínima nativa para Windows.

Escolha ferramentas Python simples e maduras. Não adicionar framework web, banco ou frontend web.

## Tarefas
1. Verificar estrutura existente e preservar documentação.
2. Configurar projeto Python com layout `src/`.
3. Criar imagem Docker de desenvolvimento.
4. Configurar `docker compose` para montar o repositório e executar comandos de desenvolvimento.
5. Configurar testes, lint e type checking.
6. Criar teste mínimo de sanidade.
7. Atualizar README somente no necessário para documentar comandos reais.
8. Garantir que o ambiente não dependa de banco, servidor ou serviço externo.

## Testes automatizados mínimos
Devem existir comandos equivalentes a:
```bash
docker compose build
docker compose run --rm app pytest
docker compose run --rm app <lint-command>
docker compose run --rm app <typecheck-command>
```

Todos devem concluir com sucesso.

## Teste manual do usuário
O relatório final deve ensinar exatamente como:
1. clonar/entrar no repositório;
2. construir a imagem;
3. rodar testes;
4. rodar lint;
5. rodar type checking;
6. confirmar que o container encerra normalmente.

## Critério de aceite
- Ambiente Docker funciona do zero.
- Testes/lint/typecheck passam.
- Projeto Python é importável.
- Nenhuma funcionalidade de organização foi antecipada.

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
