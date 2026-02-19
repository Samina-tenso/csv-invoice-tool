 # CSV Invoice Matching Tool
## Overview

The CSV Invoice Matching Tool is a full-stack application that helps automate financial reconciliation workflows.

The application allows users to:

- Upload blank CSV file containing transaction.
- Upload invoice PDF files
- Match transactions to invoices
- Rename invoices based on transaction data
- View matched and unmatched transactions

The goal is to reduce manual bookkeeping work and minimize human error in invoice reconciliation.

---

## MVP Scope

The initial Minimum Viable Product (MVP) includes:

- CSV upload endpoint
- CSV parsing and transaction extraction
- Invoice upload endpoint
- Basic transaction-to-invoice matching logic
- Simple UI to display results
- Rename invoice files based on match results

The MVP will prioritize correctness, clean architecture, and maintainability over feature complexity.

---


## Tech Stack

Frontend: Next.js + Typescript + Tailwind
Backend: FastAPI + SQLAlchemy(planned) + Pydanctic + Python + Pandas (Planned) + Pytest (Planned)

## Project Structure

csv-invoice-tool/
│
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ ├── app/
│ │ ├── routes/
│ │ ├── services/
│ │ ├── models/
│ │ └── utils/
│
├── frontend/
│ ├── package.json
│ └── src/
│
└── README.md


### Architecture Principles

- Modular backend design
- Separation of concerns (routes, services, models)
- Typed frontend with TypeScript
- Clean, readable, testable code
- Reproducible environments via virtual environments and lock files

---

## How to Run Locally

### Backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload

Visit
http://localhost:8000
http://localhost:8000/docs

### Frontend 

```bash 
cd frontend
npm install
npm run dev

Visit 
http://localhost:3000
