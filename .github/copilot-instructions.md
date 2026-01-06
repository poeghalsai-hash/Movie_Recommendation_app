**Project Overview**

- **Single-file Streamlit app:** The UI and runtime live in `app.py` (Streamlit). The app calls the Google Generative AI SDK directly to produce recommendations.
- **Primary integration:** `google.generativeai` (configured via environment variable + `python-dotenv`). The model instantiated is `gemini-2.5-flash-lite` in `app.py`.

**Quick dev commands**

- Install deps: `pip install -r requirements.txt`
- Run locally: `streamlit run app.py`

**What to inspect first (high-value areas)**

- `app.py` — single source of truth for UI + model calls. Look for `genai.configure(...)` and `model=genai.GenerativeModel('gemini-2.5-flash-lite')` to understand the request pattern.
- `requirements.txt` — shows declared packages: `streamlit`, `google_generativeAi`, `python-dotenv`, `langchain` (note: `langchain` is present but not yet used in `app.py`).
- `README.md` — short description only; does not contain run instructions.

**Common patterns & expectations for edits**

- Environment config: the app uses `dotenv`. Expect an `.env` with a key for the GenAI API. The intended pattern is to call `genai.configure(api_key=os.getenv('GENAI_API_KEY'))` (check and replace the incomplete `genai.configure(api_key=os.)` line in `app.py`).
- UI flow: read user input via `st.text_input(...)`, trigger on `st.button(...)`, and write results with `st.markdown(...)` — follow this pattern when adding UI elements.
- Error handling is minimal. When adding model calls, guard network/SDK calls and show friendly Streamlit messages (`st.error`, `st.warning`) on failures.

**Integration specifics**

- Model instantiation: `genai.GenerativeModel('gemini-2.5-flash-lite')` — follow the same model identifier when adding examples or tests.
- SDK calls are synchronous inside the Streamlit flow; keep calls short or add status messages to avoid blocking the UI.

**What not to assume**

- There is no separate backend or API server — everything runs in the Streamlit process. Do not introduce long-blocking processes without backgrounding or async handling.
- There is no CI or tests present in the repo. If you add tests, include a short `pytest` or runnable command in `README.md`.

**Suggested quick fixes (explicit, discoverable changes)**

- Fix the API-key configuration in `app.py` to use `os.getenv(...)` and document the required `.env` variable (suggest `GENAI_API_KEY`).
- If `langchain` is kept in `requirements.txt`, either add a small usage example or remove it to avoid confusion.

**When you need more context**

- Ask the maintainer which env var name they expect (current code has an incomplete `os.` reference). If they haven't decided, use `GENAI_API_KEY` and document it in `README.md` and `.env.example`.

If any section is unclear or you want a different level of detail (examples of expected request/response shapes, unit-test scaffolding, or a `.env.example`), tell me which part to expand and I'll update this file.
