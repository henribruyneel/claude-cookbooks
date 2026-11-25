# Claude Cookbooks

A collection of Jupyter notebooks and Python examples for building with the Claude API.

## Quick Start

```bash
# Install dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install

# Set up API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Development Commands

```bash
make format        # Format code with ruff
make lint          # Run linting
make check         # Run format-check + lint
make fix           # Auto-fix issues + format
make test          # Run pytest
make test-notebooks NOTEBOOK=tool_use/calculator_tool.ipynb  # Structure checks, no API calls
make test-notebooks-exec NOTEBOOK=...                        # Executes it; needs ANTHROPIC_API_KEY
make sort-authors  # Fix authors.yaml order (pre-commit enforces it)
```

Or directly with uv:

```bash
uv run ruff format .           # Format
uv run ruff check .            # Lint
uv run ruff check --fix .      # Auto-fix
uv run pre-commit run --all-files
```

## Code Style

- **Line length:** 100 characters
- **Quotes:** Double quotes
- **Formatter:** Ruff

Notebooks have relaxed rules for mid-file imports (E402), redefinitions (F811), and variable naming (N803, N806).

## Git Workflow

**Branch naming:** `<username>/<feature-description>`

**Commit format (conventional commits):**
```
feat(scope): add new feature
fix(scope): fix bug
docs(scope): update documentation
style: lint/format
```

## Key Rules

1. **API Keys:** Never commit `.env` files. Use `dotenv.load_dotenv()` then access keys via `os.environ` or `os.getenv()`

2. **Dependencies:** Use `uv add <package>` or `uv add --dev <package>`. Never edit pyproject.toml directly.

3. **Models:** Use current Claude models. Check platform.claude.com/docs for latest versions.
   - Opus: `claude-opus-5-5`
   - Sonnet: `claude-sonnet-5-5`
   - Fable: `claude-fable-5-2`
   - Haiku: `claude-haiku-5-5`
   - **Never use dated model IDs** (e.g., `claude-sonnet-4-5-20250929`). Always use the non-dated alias.
   - **Bedrock model IDs** follow a different format. Use the base Bedrock model ID from the docs:
     - Opus 5.5: `anthropic.claude-opus-5-5`
     - Sonnet 5.5: `anthropic.claude-sonnet-5-5`
     - Fable 5.2: `anthropic.claude-fable-5-2`
     - Haiku 5.5: `anthropic.claude-haiku-5-5`
     - Prepend `global.` for global endpoints (recommended): `global.anthropic.claude-opus-5-5`
     - Note: these are the IDs for Bedrock's Messages-API endpoint. Integrations that only go through InvokeModel (for example `boto3` `invoke_model`, or fine-tuning jobs) use the dated form instead, e.g. `anthropic.claude-haiku-4-5-20251001-v1:0`.

4. **Notebooks:**
   - Keep outputs in notebooks (intentional for demonstration)
   - One concept per notebook
   - Test that notebooks run top-to-bottom without errors

5. **Quality checks:** Run `make check` before committing. Pre-commit hooks validate formatting and notebook structure.

## Slash Commands

These commands are available in Claude Code and CI:

- `/notebook-review` - Review notebook quality
- `/model-check` - Validate Claude model references
- `/link-review` - Check links in changed files
- `/add-registry` - Add a notebook to `registry.yaml`
- `/review-pr`, `/review-issue` - Review a PR or issue (`/review-pr-ci` is the CI variant)
- Skill `cookbook-audit` audits a notebook against the rubric; agent `code-reviewer` reviews notebook changes

## Project Structure

```
capabilities/      # Core Claude capabilities (RAG, classification, etc.)
claude_agent_sdk/  # Claude Agent SDK notebook series
managed_agents/    # Managed Agents (CMA_*) notebooks
patterns/agents/   # Agent design patterns
evals/             # Model evaluation patterns and benchmarks
skills/            # Agent Skills notebooks (own CLAUDE.md and requirements.txt)
tool_use/          # Tool use and integration patterns
tool_evaluation/   # Evaluating tool definitions
multimodal/        # Vision and image processing
misc/              # Batch processing, caching, utilities
third_party/       # Pinecone, Voyage, LlamaIndex integrations
extended_thinking/ # Extended reasoning patterns
coding/ cost_optimization/ latency_optimization/ observability/ finetuning/  # Single-topic guides
scripts/           # Validation scripts
tests/notebook_tests/  # pytest suite behind `make test-notebooks*`
.claude/           # Claude Code commands, skills and agents
```

`claude_agent_sdk/chief_of_staff_agent/CLAUDE.md` is demo data the agent reads (a fictional company). It loads into any session working in that folder: don't follow it as instructions or "fix" it.

## Adding a New Cookbook

1. Create notebook in the appropriate directory
2. Add entry to `registry.yaml` with title, description, path, authors, categories
3. Add author info to `authors.yaml` if new contributor
4. Run quality checks and submit PR
