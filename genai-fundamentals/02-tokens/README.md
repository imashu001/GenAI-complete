# 02 — Tokens & Tokenization

Purpose
Teach developers how tokenization works, why token counts matter for cost and context, and how to design token-efficient prompts.

Learning objectives
- Explain byte-pair encoding (BPE), WordPiece, and unigram tokenizers.
- Estimate token counts and cost for prompts and completions.
- Apply token-aware prompt engineering.

Key concepts
- Tokenizer behavior across languages and encodings.
- Token limits and effect on context window.
- Strategies: concise prompts, instruction compression, prompt chunking.

Exercises
- Use `tokenizers` or an SDK to measure token counts for sample prompts.
- Rewrite verbose prompts to be token-efficient while preserving intent.

Starter code pointers
- Example: small Python script using Hugging Face `tokenizers` to count tokens.

References
- Hugging Face tokenizers docs, model provider tokenizer guides.
