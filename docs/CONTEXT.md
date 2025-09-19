### ✅ `CONTEXT.md` — NextGenHealth (Estado Atual)

```markdown
# CONTEXT.md - NextGenHealth

## 🎯 Visão Geral
Sistema de gestão de identidade para ambientes de saúde, baseado em Clean Architecture e Domain-Driven Design (DDD).  
Objetivo: Criar um modelo unificado de usuário (`User`) com suporte a múltiplos papéis (Patient, Nurse, Doctor, Admin), garantindo conformidade com HIPAA e GDPR desde o domínio.

## 🔧 Arquitetura
- **Clean Architecture**: Camadas bem definidas (Domain → Application → Infrastructure)
- **Domain-Driven Design (DDD)**: Entidades, Value Objects, Aggregates, Specifications
- **TDD**: Testes unitários guiam o design; cobertura >87%
- **Specification Pattern**: Validação composta (And/Or/Not) para regras de negócio
- **Validation Chain**: `UserValidator` orquestra todas as validações antes da criação

## 📦 Domínio Principal: User
- **Entidade central**: `User`
  - Atributos: UUID, email, nome, telefone (E.164), data de nascimento, papel, status
  - Base para especializações: PatientProfile, DoctorProfile, NurseProfile
- **Enums**: `UserRole`, `UserStatus`
- **Validações implementadas**:
  - Email válido (formato RFC-like)
  - Nome com apenas letras e espaços
  - Telefone no formato E.164 (+CCXXXXXXXXXX)
  - Data de nascimento realista (não futura, não excessivamente antiga)
- **Exceções de domínio**: `InvalidEmailError`, `InvalidUserError`, etc.

## 🧪 Testes
- **Cobertura**: 87%+ (com foco em 100% nas entidades principais)
- **Localização**: `tests/unit/domain/user/`
- **Abordagem**: TDD rigoroso, testando todos os caminhos de sucesso e falha
- **Integração com CI**: `make coverage` executa `pytest-cov` no GitHub Actions

## 📚 Documentação Automatizada
- **Ferramenta**: Sphinx
- **Fonte**: Docstrings em Google Style + estrutura modular
- **URL Pública**: https://python-projects-fernando.github.io/nextgenhealth/
- **Atualização**: Automática via GitHub Actions (`docs.yml`)
- **Conteúdo**:
  - API Reference completa do domínio
  - Classes, métodos, docstrings
  - Links para código-fonte (`viewcode`)

## 🔗 Integração com Modelio
- **Modelos UML**: Armazenados em `docs/uml/modelio_project/`
- **Exportação**: Projeto `.mdac` importado como `.zip` para garantir integridade
- **Visualização**: PNGs gerados para diagramas-chave (Class, Sequence, Use Case)
- **Rastreabilidade**: Alinhado com `UC-PAT-01_Register_User.md`, `08_data_dictionary.md`

## ⚙️ Configuração e Empacotamento
- **pyproject.toml**: Define o projeto como pacote Python instalável
- **Instalação local**: `pip install -e .`
- **Benefício**: Permite imports absolutos (`from src.user_management...`) funcionarem em Sphinx, pytest, IDEs

## 🔄 CI/CD
- **GitHub Actions**:
  - `test.yml`: Executa todos os testes unitários + cobertura
  - `docs.yml`: Gera e publica a documentação no `gh-pages`
- **Fluxo**: Todo `git push` aciona ambos workflows
- **Próximo passo**: CD para ambiente staging (futuro)

## 📁 Estrutura do Projeto
```
nextgenhealth/
├── src/
│   └── user_management/
│       └── domain/               # Entities, Specs, Validation
├── docs/
│   ├── api/                      # Sphinx-generated docs
│   ├── uml/                      # Modelio project + PNGs
│   └── sdlc/                     # 01_, 02_, ..., UC-PAT-01_
├── tests/
│   └── unit/
│       └── domain/
│           └── user/             # Unit tests
├── .github/workflows/
│   ├── test.yml
│   └── docs.yml
└── pyproject.toml
```

## ✅ Próximos Passos Imediatos
1. Implementar `RegisterUserUseCase` (Application Layer)
2. Criar `UserCredentials` com hashing seguro (bcrypt)
3. Iniciar `PostgreSQLUserRepository` com UUID PK e unique email constraint
4. Adicionar auditoria de criação (created_at, updated_at)

## 🌐 Autor
Fernando Antunes de Magalhães  
CEO | FM ByteShift Software  
[LinkedIn](https://www.linkedin.com/in/seu-perfil) | [Blog](https://fmbyteshiftsoftware.com/blog-list)
```

---

### ✅ Como usar esse `CONTEXT.md`

1. Salve como `docs/CONTEXT.md` no seu projeto.
2. Atualize sempre que concluir uma fase (ex: após `RegisterUserUseCase`).
3. Quando reiniciar uma conversa comigo (ou com qualquer colaborador), anexe este arquivo.

➡️ Garante velocidade, precisão e continuidade.

---

