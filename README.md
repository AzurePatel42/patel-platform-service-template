# Patel Platform Service Template (PPST)

## What is PPST?

Patel Platform Service Template (PPST) is a reusable backend application template built with Python and FastAPI.

Its purpose is not simply to create REST APIs.

Its purpose is to provide a consistent engineering foundation that every backend service in the Patel Engineering ecosystem can inherit.

Instead of rebuilding architecture for every project, PPST provides a production-oriented starting point that already includes:

* Clean Architecture
* Dependency Injection
* Repository Pattern
* Configuration Management
* Structured Logging
* Global Exception Handling
* Standardized API Contracts
* Unit Testing
* Extensible Infrastructure

Every future backend service should begin with PPST and then customize only its business domain.

---

## The Problem PPST Solves

Many developers build each project independently.

As projects grow, they often develop:

* Different folder structures
* Different coding styles
* Different logging approaches
* Different error handling
* Different dependency management
* Different testing strategies

Over time, maintaining multiple projects becomes increasingly difficult because each one follows different engineering practices.

PPST solves this problem by establishing one consistent architecture that every service shares.

Instead of reinventing infrastructure, developers can focus on implementing business logic.

This approach improves maintainability, readability, scalability, onboarding, and long-term development speed.

---

## Design Philosophy

PPST follows one simple principle:

**Infrastructure should remain stable. Business logic should change.**

When creating a new service, only a few parts should differ:

* Domain models
* Business rules
* Contracts
* Repository implementation

Everything else—including project structure, configuration, logging, exception handling, dependency injection, and testing—should remain consistent across services.

This creates predictable systems that are easier to understand, extend, and maintain.

# Architecture Philosophy

PPST is built around one fundamental software engineering principle:

> Every layer should have one responsibility.

As software systems grow, mixing responsibilities makes applications difficult to understand, test, and maintain.

PPST separates the application into independent layers so that each layer focuses on solving one specific problem.

This approach follows the principles of Separation of Concerns (SoC) and Clean Architecture.

---

## The Four Core Layers

PPST organizes application logic into four primary layers.


                API
                 │
                 ▼
          Application
                 │
                 ▼
              Domain
                 │
                 ▼
         Infrastructure


Each layer communicates only with the layer directly below it.

Lower layers never depend on higher layers.

This creates a predictable and maintainable application architecture.

---

## API Layer

Purpose:

Receive HTTP requests and return HTTP responses.

Responsibilities:

- Define API endpoints
- Validate incoming requests
- Return response contracts
- Convert HTTP requests into service calls

The API layer should never contain business logic.

Example:

GET /items

should simply call:

ItemService.get_item()

without making business decisions.

---

## Application Layer

Purpose:

Coordinate application use cases.

Responsibilities:

- Execute business workflows
- Call repositories
- Coordinate multiple operations
- Convert database models into response contracts

The application layer acts as the orchestrator of the system.

It answers the question:

"What needs to happen?"

It does not answer:

"How is data stored?"

or

"What business rule determines this?"

---

## Domain Layer

Purpose:

Store business knowledge.

Responsibilities:

- Business rules
- Validation rules
- Domain-specific calculations
- Policies

Example:

ItemRules.is_low_stock(quantity)

belongs in the domain because it represents business behavior rather than infrastructure.

Business rules should not depend on FastAPI, SQLAlchemy, or databases.

---

## Infrastructure Layer

Purpose:

Communicate with external systems.

Responsibilities:

- Database access
- Repository implementations
- Logging
- Cache
- Messaging
- External APIs

Infrastructure answers the question:

"How do we communicate with external systems?"

It should never contain business rules.

---

## Why Separate the Layers?

Separating responsibilities provides several advantages:

- Easier testing
- Better maintainability
- Clear ownership
- Lower coupling
- Higher scalability
- Better readability

When business rules change, only the domain changes.

When databases change, only the infrastructure changes.

When APIs change, only the routes and contracts change.

The rest of the system remains stable.

---

## PPST Design Principle

The framework should remain stable.

Business logic should evolve.

Every new service should reuse the same architecture while replacing only:

- Domain models
- Business rules
- Contracts
- Repository implementation

Everything else should remain familiar across every service.

## Request Lifecycle

Every HTTP request entering PPST follows the same execution path regardless of business domain.

The framework is designed so that every layer has one responsibility.

                 Client
                    │
                    ▼
            FastAPI Route
                    │
                    ▼
         Dependency Injection
                    │
                    ▼
          Application Service
                    │
                    ▼
             Domain Rules
                    │
                    ▼
             Repository Layer
                    │
                    ▼
            SQLAlchemy ORM
                    │
                    ▼
               Database
                    │
                    ▼
             Repository Layer
                    │
                    ▼
          Application Service
                    │
                    ▼
         Response Contract
                    │
                    ▼
                FastAPI
                    │
                    ▼
                 Client




Step 1

Client sends

POST /items

with

{
    "name":"Laptop",
    "quantity":4
}

Step 2

The API Route

Responsibilities:

Validate request
Get database session
Resolve dependencies
Call ItemService

No business logic exists here.

Step 3

Dependency Injection

The container creates

ItemRepository

↓

ItemService

and injects the dependencies into the route.

This keeps object creation outside the business logic.

Step 4

Application Service

The service coordinates the workflow.

ItemRepository.create()

↓

ItemRules.is_low_stock()

↓

ItemResponse

The service orchestrates the application.

Step 5

Domain Layer

Business rules execute.

Example:

LOW_STOCK_THRESHOLD = 5

Only the domain knows this rule.

Step 6

Repository

The repository communicates with SQLAlchemy.

Responsibilities:

INSERT
SELECT
UPDATE
DELETE

No business rules exist here.

Step 7

Database

The transaction commits.

SQLAlchemy refreshes the object.

Step 8

Response Contract

The service converts the database model into

ItemResponse

This prevents exposing database models directly.

Step 9

FastAPI

FastAPI validates

response_model=ItemResponse

before returning

HTTP 200

to the client.