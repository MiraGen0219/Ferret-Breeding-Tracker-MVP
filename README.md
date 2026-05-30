# 🦦 Ferret Breeding Tracker MVP

A full-stack ferret breeding management application built with Flask, SQLAlchemy, and MySQL. This project provides a centralized system for managing ferrets, breeding pairings, litter records, and breeder analytics while establishing the foundation for future pedigree and genetic analysis tools.

---
## 🚧 Current Development Status

### MVP 1 Progress

#### Ferret Management
- [x] Create Ferret
- [x] View Ferrets
- [x] Edit Ferret
- [x] Delete Ferret
- [x] Parentage Tracking

#### Pairing Management
- [ ] Create Pairing
- [ ] View Pairings
- [ ] Edit Pairing
- [ ] Delete Pairing

#### Litter Management
- [ ] Create Litter
- [ ] View Litters
- [ ] Edit Litter
- [ ] Delete Litter

#### Reports
- [ ] Breeder Analytics Dashboard
- [ ] Production Summaries

---

## 📖 Overview

The Ferret Breeding Tracker MVP was designed to replace scattered spreadsheets and manual record keeping with a structured relational database system.

The application allows breeders to:

* Track individual ferret records
* Record breeding pairings
* Manage litter information
* Track parentage relationships
* Monitor active and retired breeders
* Generate breeding and production summaries
* Analyze yearly breeding outcomes

This MVP focuses on operational breeder management and reporting.

Future versions will expand into pedigree analysis, genetic tracking, inbreeding coefficient calculations, color/pattern inheritance analysis, and breeding recommendation tools.

---

## ✨ Features

### 🦦 Ferret Management

* Create ferret records
* Update ferret information
* Remove ferret records
* Track:

  * Name
  * Sex
  * Birth date
  * Breeder
  * Status
  * Size
  * Color
  * Pattern
  * Heritage
  * Temperament
  * Health notes
  * Condition notes

---

### 👨‍👩‍👧 Parentage Tracking

* Store father and mother relationships
* Build pedigree foundations
* Support future pedigree visualization features

---

### ❤️ Pairing Management

* Create breeding pairings
* Track:

  * Jill
  * Hob
  * Season
  * Year
  * Compatibility notes
  * Breeding notes
  * Planned status

---

### 🍼 Litter Management

* Create litter records
* Track:

  * Kits born
  * Kits passed
  * Kits survived
  * Pregnancy behavior notes
  * Birth notes
  * Postpartum notes

---

### 📊 Analytics & Reporting

Generate breeding statistics including:

* Litters by jill
* Pairings by hob
* Active breeders
* Retired breeders
* Yearly production summaries
* Hob production summaries
* Jill production summaries
* Average litter sizes
* Survival rates

---

### 🌱 Demo Data Seeding

Includes a seed script for:

* Automatic database population
* Demo breeder records
* Demo pairings
* Demo litters
* Parentage relationships

---

## 🏗 Tech Stack

### Backend

* 🐍 Python
* 🌶 Flask
* 🗄 SQLAlchemy ORM
* 📦 Marshmallow
* 🐬 MySQL

### Frontend

* HTML
* CSS
* Jinja Templates

### Development Tools

* Git
* GitHub
* VS Code
* Postman

---

## 🗂 Database Structure

### Ferret

Stores individual ferret records.

Key relationships:

```text
Ferret
├── father_id → Ferret
├── mother_id → Ferret
├── Pairings (as Jill)
└── Pairings (as Hob)
```

---

### Pairing

Stores breeding pair information.

```text
Pairing
├── Jill
├── Hob
└── Litters
```

---

### Litter

Stores litter records and production outcomes.

```text
Litter
├── Pairing
├── Kit Counts
└── Behavioral Notes
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ferret-breeding-tracker-mvp.git
cd ferret-breeding-tracker-mvp
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙ Database Setup

Create MySQL database:

```sql
CREATE DATABASE ferret_breeding_tracker;
```

Configure environment variables in:

```text
.env
```

Example:

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=ferret_breeding_tracker
```

---

## ▶ Running the Application

Start Flask:

```bash
python app.py
```

---

## 🌱 Loading Demo Data

Populate the database:

```bash
python seed.py
```

This script:

* Clears existing demo data
* Creates ferret records
* Creates parentage relationships
* Creates pairings
* Creates litter records

---

## 🔌 Example API Endpoints

### Ferrets

```http
GET /ferrets
POST /ferrets
PUT /ferret/<id>
DELETE /ferret/<id>
```

---

### Pairings

```http
GET /pairings
POST /pairings
PUT /pairing/<id>
DELETE /pairing/<id>
```

---

### Litters

```http
GET /litters
POST /litters
PUT /litter/<id>
DELETE /litter/<id>
```

---

### Reports

```http
GET /jill/<id>/litters
GET /hob/<id>/jills
GET /year/<year>/litters
GET /breeders/active
GET /breeders/retired
GET /year/<year>/summary
GET /hob/<id>/production-summary
GET /jill/<id>/production-summary
```

---

## 📈 Future Roadmap

### Version 2

* Pedigree visualization
* Family tree generation
* Pedigree printing

### Version 3

* Genetic inheritance tracking
* Color/pattern analysis
* Outcome statistics

### Version 4

* Inbreeding coefficient calculations
* Relationship analysis
* Breeding recommendations

### Version 5

* Mobile-first interface
* User authentication
* Multi-ferretry support

---

## 🎯 Learning Objectives

This project demonstrates:

* Relational database design
* ORM modeling
* REST API development
* SQLAlchemy relationships
* Query optimization
* Data analytics
* Git workflows
* Full-stack application architecture

---

## 🧠 Lessons Learned

Some of the most valuable lessons came from debugging and solving real-world development problems.

### 🐬 MySQL & Database Management

* Learned that `db.create_all()` creates tables but does not create the database itself.
* Learned how foreign key constraints protect data integrity.
* Learned that self-referencing relationships (parent → offspring) require special consideration when deleting data.

### 🗄 Relational Database Design

* Designed a normalized schema for ferrets, pairings, and litters.
* Implemented one-to-many relationships between pairings and litters.
* Implemented self-referencing parentage relationships using `father_id` and `mother_id`.
* Learned how relationship dependencies affect creation and deletion order.

### 🐍 Python & SQLAlchemy

* Learned how ORM models map Python objects to database tables.
* Learned the importance of model serialization using `to_dict()`.
* Learned how object IDs are assigned after database commits.
* Learned how to use multiple commits within a single script to build dependent records.
* Learned the difference between model logic, route logic, and schema behavior.

### 🌱 Seed Data & Development Workflow

* Built a reusable seed script to populate the database with realistic breeder records.
* Learned that seed scripts bypass API routes and therefore require their own data handling.
* Learned how to create and maintain repeatable development environments.
* Learned how to work with foreign keys and parentage assignments during data seeding.

### 🔌 API Development

* Built and tested CRUD endpoints for multiple related models.
* Built custom query endpoints for breeder analytics and reporting.
* Learned how to aggregate data and generate summary reports.
* Used Postman extensively for endpoint testing and debugging.

### 🧰 Development Tools

* Learned how dependency management works through `requirements.txt`.
* Learned how package installation issues can affect application startup.

### 🌿 Git & GitHub

* Learned how `.gitignore` protects sensitive files and local environments.
* Established a workflow for version control and future development.

### 🎯 Biggest Takeaway

* Designing data structures
* Managing dependencies
* Debugging unexpected behavior
* Understanding how systems interact
* Building reliable workflows

Many of the most valuable skills were learned while solving problems that were never part of the original feature list.

---

## 📜 License

This project is intended for educational, portfolio, and breeder-management purposes.

---

## 👤 Author

Erin

Software Engineer | Ferret Breeder | Database & Breeding Analytics Enthusiast
