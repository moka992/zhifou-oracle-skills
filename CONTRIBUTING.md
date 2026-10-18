# Contributing

Useful contributions include a source correction, a reproducible calculation bug, a better host-integration example, or a behavioral case where an answer loses the user's question or overstates a symbol.

Use synthetic examples. Do not post real reading histories, birthdays, API keys, device screenshots containing personal information, or provider error dumps with credentials.

Run `python3 -m unittest discover -s tests -v` and `python3 tools/check_release.py`. For prompt changes, explain which observable behavior improves and how you evaluated it. Preserve source attribution and distinguish a historical quotation from a modern interpretation. A style preference alone is not evidence of a more accurate prediction.

Changes to classical data require a cited source and a refreshed `data/manifest.json` using `python3 tools/update_manifest.py`. The Zhou Yi dataset remains CC BY-SA 4.0. New images need file-level source and license information; do not add modern commercial tarot artwork or translations.

Keep dependencies minimal and runtime instructions compact. Avoid provider credentials, hidden network calls, unsolicited telemetry, and installation scripts that overwrite a user's existing skill. Proposals for additional traditions should name the actual method and reference material rather than blending systems silently.
