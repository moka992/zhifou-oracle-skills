# Security and Privacy

The bundled Python tools make no network requests and store no reading history. They accept local arguments/files and print JSON. The host agent, terminal, conversation store, or a model API provider may still retain that output; their policies are separate from this repository.

Prefer `--question-stdin` for a private question, avoid committing output, and review files before passing them to a model. The checksum validates internal consistency, not authenticity or the truth of a divination result. Skill instructions cannot guarantee that every model will resist prompt injection.

Do not disclose API keys or real user conversations in a public issue. For a vulnerability, use GitHub's private vulnerability reporting if enabled. Otherwise open a minimal issue asking for a private reporting channel without including exploitable details or secrets.

The pre-publication scanner catches obvious key/private-file patterns and personal machine paths. It is a useful guard, not a substitute for reviewing the staged files and their licenses.
