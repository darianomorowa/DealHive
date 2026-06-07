---
title: Data Model
nav_exclude: true
nav_order: 2
---

{: .no_toc }
# Data Model

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

# Data Model

## Hive

The central entity of DealHive is the Hive.

A Hive represents a group-buying campaign that users can join in order to reach a required number of participants and unlock a discount.

### Attributes

| Attribute | Type | Description |
|------------|------|-------------|
| id | INTEGER | Unique identifier of the hive |
| title | TEXT | Name of the hive |
| game_system | TEXT | Related game system (e.g. D&D, Pathfinder) |
| short_description | TEXT | Short summary of the hive |
| description | TEXT | Detailed hive description |
| deadline | TEXT | End date of the campaign |
| current_participants | INTEGER | Current number of participants |
| min_participants | INTEGER | Required number of participants |

### SQL Implementation

```sql
CREATE TABLE IF NOT EXISTS hives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    game_system TEXT NOT NULL,
    short_description TEXT NOT NULL,
    description TEXT NOT NULL,
    deadline TEXT NOT NULL,
    current_participants INTEGER NOT NULL,
    min_participants INTEGER NOT NULL
);
```

## Design Decision

For the first prototype we intentionally use a simplified data model containing only one core entity (Hive).

Additional entities such as Users, Orders, Payments or Messages are not yet implemented because the focus of the prototype is to demonstrate the group-buying concept and the Hive overview functionality.

The model can easily be extended in future iterations by introducing user accounts and participation relationships.

## Relationships

### User ↔ Hive

A user can participate in multiple hives.

A hive can contain multiple users.

This many-to-many relationship is represented through the table `hive_participants`.

### User

| Attribute | Type | Description |
|------------|------|-------------|
| id | INTEGER | Unique identifier |
| username | TEXT | Username of the user |
| name | TEXT | Full name |
| email | TEXT | Email address |
| password_hash | TEXT | Encrypted password |
| role | TEXT | User role |
| street | TEXT | Street address |
| postal_code | TEXT | Postal code |
| city | TEXT | City |
| country | TEXT | Country |

### Hive Participant

| Attribute | Type | Description |
|------------|------|-------------|
| id | INTEGER | Unique identifier |
| hive_id | INTEGER | Reference to a hive |
| user_id | INTEGER | Reference to a user |
| is_creator | BOOLEAN | Indicates whether the user created the hive |

### Relationship Diagram

```text
users
 1
 |
 n
hive_participants
 n
 |
 1
hives
```

### Future Extension

In future versions, additional entities such as orders, payments and messages can be introduced.

The `hive_participants` table allows users to join multiple hives while also identifying the creator of each hive.

This structure supports future features such as user profiles, participation management and permissions.