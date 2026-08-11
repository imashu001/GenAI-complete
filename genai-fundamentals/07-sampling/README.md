# LLM Sampling: How Models Pick the Next Word

Welcome to the control panel of Generative AI! Every time you call an LLM API (like OpenAI, Anthropic, or local models via Ollama), you configure parameters like temperature, top_p, and top_k.

As a software developer, it helps to realize that LLMs are fundamentally probabilistic text-completion engines, not hard-coded search queries. When given a prompt, the model doesn't just output a single definitive word; it outputs a massive probability distribution across its entire vocabulary (tens of thousands of tokens).  

Sampling is the algorithmic process of choosing which token to pick from that probability distribution at each step

## Phase 1: The Pipeline (From Logits to Selection)
When text is generated, it goes through a specific pipeline:  
**Logits:** The raw, unnormalized score numbers computed by the transformer's final layer for every token.  
**Softmax:** Converts those raw logits into percentages (probabilities) that sum up to $1.0$ (100%).  
**Sampling & Filtering:** Parameters modify or slice this distribution before a random roll of the dice picks the final token.

Example: If you prompt "The capital of France is", the raw probabilities might look like this:

Paris: 62%  
Lyon: 3%  
Mars: 0.0001%
Banana: 0.00001%

Without sampling rules, the model usually picks Paris, but occasionally a random roll might pick Lyon or something wild. Sampling parameters let you control how strict or wild that randomness is.

## Phase 2: The Core Knobs You Need to Know
### 1. Temperature ($T$) — The Sharpness & Creativity Dial
Temperature scales the logits before softmax is applied. It acts as a multiplier/divider that flattens or sharpens the probability curve.  
$T = 0$ (Greedy Decoding): Completely turns off sampling. The model always picks the absolute highest-probability token. Outputs are 100% deterministic, but can become repetitive or robotic. Use for: Code generation, JSON structuring, math, and factual Q&A.  

$T = 0.7$ (Balanced): The standard default for conversational chatbots. Good mix of coherence and mild variability.  

$T > 1.0$ (Creative / Wild): Flattens the distribution, making underdog tokens more competitive. Use for: Brainstorming, poetry, and creative storytelling. 

### 2. Top-K — The Hard Vocabulary Cutoff
Top-K tells the model: "Look only at the top $K$ most likely tokens, and completely throw away the rest (set their probability to zero)".  

If $K = 40$, the model picks strictly from the 40 best options, ignoring thousands of absurd lower-probability words.
The Flaw: It's static. If the model is completely confident, cutting to 40 options might introduce weird noise. If the model is confused, 40 options might still contain garbage. (Many modern setups keep Top-K disabled or set to 0).  

### 3. Top-P (Nucleus Sampling) — The Dynamic Confidence Filter
Introduced to fix Top-K's rigidity, Top-P looks at cumulative probabilities.  
If you set top_p = 0.9, the model pools together the top-ranked tokens whose probabilities add up to 90%.  

Adaptive behavior: If the model is extremely sure of the next word, the top 2 or 3 words might already equal 90%, so it restricts choices tightly. If the model is uncertain, it automatically widens the net to include more choices to reach that 90% threshold.  

### 4. Min-P (The Modern Standard)
An increasingly popular alternative to Top-K/Top-P in modern open-source inference engines. Min-P sets a floor relative to the top token. If the best token has a 50% probability, and min_p = 0.05, any token with less than $5\% \times 50\% = 2.5\%$ probability is automatically discarded. It dynamically scales cleanly even at high temperatures.

Phase 3: Developer Cheat Sheet (When to Use What)

| Use Case | Recommended Temperature | Recommended Top-P / Other | Why?
| :--- | :--- | :--- | :--- |
| Code Generation / APIs | 0.0 to 0.2 | 0.95 (or default) | Code requires syntax precision; syntax errors break compilers. Zero tolerance for creative hallucinations.
| Factual RAG / Search Q&A | 0.1 to 0.3 | 0.5 | Forces the model to stick closely to retrieved context documents rather than inventing facts.
| General Chatbot | 0.7 | 0.9 | Gives a natural human-like variation in tone without wandering off-topic.
| Creative Writing / Brainstorming | 1.0 to 1.2 | 0.95 to 1.0 | "Flattens constraints to produce unexpected, vivid narrative directions."