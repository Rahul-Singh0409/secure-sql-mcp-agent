# 🛡️ Secure-SQL-Agent (MCP Server)

An advanced Model Context Protocol (MCP) server built with **FastMCP** and **Pydantic v2** that allows Large Language Models (LLMs) to securely interact with an SQLite database. It features dynamic schema inspection, intelligent query execution, and a strict regex-based security guardrail to prevent malicious data modification.

---

## 🚀 Key Features

* **🔒 Built-in Security Guardrail:** Features an automated regex validation layer (`is_query_safe`) that intercepts and blocks hazardous SQL commands (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `TRUNCATE`, `CREATE`) to ensure read-only safety.
* **📊 Dynamic Schema Discovery:** A dedicated tool (`get_db_schema`) that enables LLMs to introspect table structures, columns, and relations before compiling queries, drastically reducing syntax errors.
* **⚡ Modern MCP Architecture:** Built using Context-Aware FastMCP routing with fully integrated type-safe Pydantic data validation schemas.
* **🛠️ Robust Error Management:** Catch-all exception handling loops that abstract raw Python stack traces into neat, informative diagnostic strings for the LLM context.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastMCP (Model Context Protocol Server)
* **Validation:** Pydantic v2
* **Database Engine:** SQLite3
* **Pattern Matching:** Regex (`re`)

---

## 📂 Project Structure

```text
├── company.db           # SQLite Production Database
├── server.py             # Core MCP Server & Tool Definitions
├── .gitignore            # Keeps your database and env files safe from git
└── README.md             # Project Documentation