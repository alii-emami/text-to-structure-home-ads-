# 🏠 Real Estate Ad Information Extractor

**A high-performance, modular API for extracting structured data from Persian real estate advertisements using a fine‑tuned NER model and rule‑based regex patterns.**

---

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green)](https://fastapi.tiangolo.com)
[![Transformers](https://img.shields.io/badge/Transformers-4.46.0-yellow)](https://huggingface.co/docs/transformers)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Made with ❤️ in Iran](https://img.shields.io/badge/Made%20with-❤️%20in%20Iran-red)]()

---

## 📖 Project Description

**Real Estate Ad Information Extractor** is a production‑ready microservice that takes a Persian real estate advertisement text and returns a structured JSON output containing key property features:

- **Building area** (square meters)
- **Number of rooms**
- **Availability of elevator**
- **Availability of parking**
- **Renovation status**

The system combines two complementary approaches:

1. **Rule‑based extraction (Regex)** – for well‑defined patterns like area (`۸۵ متر`) and room count (`دوخوابه`).
2. **Fine‑tuned NER model (ParsBERT)** – for nuanced context like negations (`آسانسور ندارد`) and semantic variations.

This hybrid approach ensures high accuracy on common cases while maintaining robustness against linguistic variations in Persian real estate ads.

---

## ✨ Key Features

- ✅ **Hybrid Extraction** – regex for structured fields + deep learning NER for semantic understanding.
- ✅ **Offline & Local** – runs completely offline after initial model download.
- ✅ **Modern API** – built with FastAPI, fully documented (via Swagger/ReDoc, optional).
- ✅ **Production‑ready** – modular architecture with logging, CORS, and error handling.
- ✅ **Persian NLP** – optimized for Persian language (supports Hazm normalization, handling of Persian digits, and common misspellings).
- ✅ **Extensible** – easy to add new fields or swap the NER model.
- ✅ **Container‑ready** – can be Dockerized with minimal changes.

---

   ```bash
   git clone https://github.com/yourusername/real-estate-info-extractor.git
   cd real-estate-info-extractor
