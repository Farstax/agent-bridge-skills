# Farstax Agent Bridge Skills

Curated optional Skills for Agent Bridge. Agent Bridge owns installation, projection, integrity checks and removal.

`catalogue.json` publishes canonical Skills plus lightweight Collections. Installing a Collection installs missing ordinary Skills; removing it leaves independently installed or shared Skills in place.

The catalogue groups skills by task:

- **Marketing:** market research, positioning, content, advertising and measurement.
- **Build:** parallel work, temporary previews and structured challenges.
- **Design:** interface critique and refinement.
- **Documents:** Excel, Word, PowerPoint and PDF creation and editing.
- **Business:** data analysis, financial modelling, investment research, legal document review, sales research and product specifications.
- **Research:** multi-source, cited deep research.

Each Skill is independently installable. Skills are instructions, not software installers or new services; tool availability depends on the workspace and provider. A Skill must check required tools and verify outputs rather than assume an external environment's packages are present.

Skills do not require a Farstax Stack and do not authorize Connections, OAuth, hosted services, tools or providers.

See `AGENTS.md` for the publishing and validation contract and `catalogue.source.json` for the curated inventory.
