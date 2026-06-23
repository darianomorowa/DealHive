---
title: Design Decisions
nav_order: 5
has_children: true
---

# Design Decisions

This section documents the most important design decisions in DealHive.

DealHive is a Flask web app for creator-based group buying in the area of board games, TTRPGs, tabletop games and accessories. The app is intentionally built as a small MVP, not as a full marketplace.

| ID | Decision | Status | Main files |
| --- | --- | --- | --- |
| DD-01 | Creator create Hives, buyers join them | Decided | `hives.py`, `creator_routes.py`, templates |
| DD-02 | Buyer and Creator roles are handled through the session | Decided | `user_routes.py`, `sidebar.html`, `creator_routes.py` |
| DD-03 | SQLite is accessed through `execute`, not `db.query` | Decided | `database.py` |
| DD-04 | User-Hive relations are modeled through `user_hives` | Decided | `database.py`, `hives.py`, `creator_routes.py` |
| DD-05 | Discount tiers are stored in `hive_tiers` | Decided | `database.py`, `pricing_logic.py`, `create_hive.html` |
| DD-06 | Flask routes are split by responsibility | Decided | `app.py`, `user_routes.py`, `hives.py`, `creator_routes.py` |
| DD-07 | Shared Jinja layout and sidebar are used | Decided | `layout.html`, `sidebar.html` |
| DD-08 | Communication is modeled as private 1-to-1 chat | Decided | `hives.py`, `chat.html`, `my_chats.html` |
| DD-09 | `/api/hives` provides a small JSON API | Decided | `hives.py` |