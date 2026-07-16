# Patel Platform Service Template (PPST)

A production-oriented backend application template built with **Python**, **FastAPI**, and **Clean Architecture**.

PPST provides a reusable engineering foundation that enables developers to build consistent, maintainable, and scalable backend services without repeatedly solving the same infrastructure problems.

Instead of rebuilding project structure, dependency injection, logging, exception handling, configuration, testing, and architectural patterns for every new project, PPST provides these capabilities out of the box so developers can focus on implementing business logic.

---

# Table of Contents

1. Introduction
2. Why PPST Exists
3. Design Philosophy
4. Engineering Principles
5. Architecture Overview
6. Request Lifecycle
7. Project Structure
8. Layer Responsibilities
9. Dependency Injection
10. Configuration
11. Logging
12. Global Exception Handling
13. Repository Pattern
14. Domain Rules
15. Testing
16. Building a New Service
17. Current Features
18. Roadmap

---

# 1. Introduction

Patel Platform Service Template (PPST) is a reusable backend application template designed to standardize software architecture across every backend service in the Patel Engineering ecosystem.

Rather than serving as a simple CRUD starter project, PPST provides a production-oriented engineering foundation that encourages consistency, maintainability, scalability, and clean separation of responsibilities.

The template already includes the common infrastructure required by modern backend services, allowing developers to spend their time solving business problems instead of rebuilding the same technical foundation.

PPST currently includes:

- Clean Architecture
- Layered Design
- Dependency Injection
- Repository Pattern
- SQLAlchemy Integration
- Configuration Management
- Structured Logging
- Global Exception Handling
- Standardized API Contracts
- Unit Testing
- Extensible Project Structure

Every future backend service should inherit this template and customize only its business domain.

---

# 2. Why PPST Exists

As organizations build more backend services, projects often begin to drift apart.

Different developers make different architectural decisions, resulting in inconsistent folder structures, coding styles, logging strategies, testing approaches, dependency management, and error handling.

Over time, this inconsistency creates unnecessary complexity.

Instead of maintaining one engineering standard, every project becomes its own unique system that developers must learn independently.

Typical problems include:

- Different folder structures
- Different logging implementations
- Different exception handling
- Different testing strategies
- Different configuration approaches
- Duplicated infrastructure code
- Inconsistent API responses
- Difficult onboarding for new developers

PPST solves these problems by providing one consistent engineering foundation that every backend service shares.

Instead of reinventing infrastructure for every project, developers inherit a proven architecture and focus only on implementing business requirements.

This approach improves:

- Maintainability
- Readability
- Scalability
- Developer productivity
- Team collaboration
- Long-term consistency

The result is a collection of backend services that all look, behave, and evolve in a predictable manner.

---

# 3. Design Philosophy

PPST is built around one simple philosophy:

> **Infrastructure should remain stable. Business logic should evolve.**

The architecture should not change every time a new backend service is created.

Instead, only the business domain should change.

When creating a new service, developers typically replace:

- Domain models
- Business rules
- Application use cases
- Repository implementations
- API contracts

Everything else should remain consistent.

This includes:

- Project structure
- Dependency Injection
- Logging
- Configuration
- Exception handling
- Testing
- Middleware
- Startup process

This philosophy creates systems that are predictable, reusable, and easier to maintain over time.

PPST follows several well-established software engineering principles:

### Separation of Concerns (SoC)

Every layer should solve one specific problem.

Responsibilities are separated so that changes in one part of the application have minimal impact on the rest of the system.

### Single Responsibility Principle (SRP)

Every module, class, and layer should have one primary responsibility.

This improves readability, maintainability, and testing.

### Clean Architecture

Business rules should remain independent of frameworks, databases, and external technologies.

Frameworks may change.

Business rules should not.

### Dependency Inversion

High-level application logic should depend on abstractions rather than implementation details.

This makes components easier to replace and test.

### Composition over Duplication

Instead of copying infrastructure into every project, services reuse the same architectural foundation and compose new business functionality on top of it.

---

# 4. Engineering Principles

Every backend service built using PPST should follow the same engineering rules.

These principles keep the codebase consistent and maintainable as the platform grows.

## One Responsibility Per Layer

Every architectural layer exists for one purpose.

Routes process HTTP requests.

Application services coordinate workflows.

The domain contains business rules.

Infrastructure communicates with external systems.

Responsibilities should never overlap.

---

## Keep Business Logic Out of Routes

API routes should remain thin.

Their responsibilities are limited to:

- Receiving requests
- Validating input
- Resolving dependencies
- Calling application services
- Returning responses

Routes should never make business decisions.

---

## Business Rules Belong to the Domain

Business policies belong inside the domain layer.

Examples include:

- Inventory thresholds
- Discount calculations
- Validation policies
- Pricing rules
- Approval logic

The domain should remain independent of FastAPI, SQLAlchemy, databases, and external services.

---

## Services Coordinate Workflows

Application services orchestrate use cases.

They determine:

- Which repositories to call
- Which domain rules to execute
- Which response contracts to return

Services coordinate the application.

They do not directly manage HTTP requests or database implementation details.

---

## Infrastructure Handles External Systems

Infrastructure communicates with technologies outside the application.

Examples include:

- Databases
- Logging
- Cache
- Messaging
- File Storage
- External APIs

Infrastructure should never contain business rules.

---

## Centralize Configuration

Configuration values should have a single source of truth.

Environment variables should be loaded into a centralized configuration object and shared across the application.

Hardcoded configuration values should be avoided whenever possible.

---

## Use Dependency Injection

Application components should receive their dependencies instead of creating them directly.

Dependency Injection reduces coupling and improves testing by making components easier to replace.

---

## Test Business Logic Independently

Business logic should be testable without requiring:

- FastAPI
- SQLAlchemy
- Databases
- External APIs

Unit tests should focus on validating business behavior rather than infrastructure.

---

## Keep Infrastructure Stable

The architecture should remain consistent across every backend service.

As new services are created, developers should only replace the business domain while reusing the same engineering foundation.

This consistency allows every PPST-based project to feel familiar regardless of its business purpose.

---

## Phase 1 Summary

By the end of this section, the goals of PPST should be clear:

- Provide a reusable backend engineering foundation.
- Standardize architecture across multiple services.
- Separate business logic from infrastructure.
- Encourage clean, maintainable, and testable code.
- Allow developers to focus on solving business problems instead of rebuilding common infrastructure.

The following sections explain how PPST achieves these goals through its architecture, layers, request lifecycle, and engineering components.

# Phase 2 — Building Services with PPST

Phase 1 explained **why PPST exists** and the architectural philosophy behind it.

Phase 2 explains **how services are built inside PPST**.

Rather than thinking about a backend as one large application, PPST treats every backend as a collection of small, independent layers that work together.

Each layer has one responsibility.

Each layer communicates through well-defined boundaries.

This approach makes services easier to understand, easier to test, and easier to maintain as they grow.

---

# Layer Responsibilities

PPST separates every service into four primary layers.

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

Each layer answers a different engineering question.

---

## API Layer

Purpose:

Receive HTTP requests and return HTTP responses.

Responsibilities:

- Define endpoints
- Validate requests
- Return response models
- Call the appropriate application service

The API layer should never contain business rules.

Its only responsibility is translating HTTP requests into application calls.

Example:

GET /items

↓

ItemService.get_item()

---

## Application Layer

Purpose:

Coordinate application workflows.

Responsibilities:

- Execute use cases
- Coordinate business operations
- Call repositories
- Convert entities into response contracts

The application layer answers:

"What needs to happen?"

It does not answer:

"How is data stored?"

or

"What is the business rule?"

Those belong elsewhere.

---

## Domain Layer

Purpose:

Contain business knowledge.

Responsibilities:

- Business rules
- Policies
- Validation logic
- Domain calculations

Example:

ItemRules.is_low_stock(quantity)

This represents business behavior.

Business rules should never depend on:

- FastAPI
- SQLAlchemy
- Databases
- HTTP
- External services

The domain should remain independent from infrastructure.

---

## Infrastructure Layer

Purpose:

Communicate with external systems.

Responsibilities:

- Database access
- Repository implementations
- Logging
- Configuration
- Messaging
- Cache
- External APIs

Infrastructure answers:

"How do we communicate with external systems?"

Business rules should never live here.

---

# Why Layer Separation Matters

Separating responsibilities produces several important engineering benefits.

## Maintainability

Each layer has one responsibility.

Changes remain isolated.

---

## Testability

Business logic can be tested without:

- FastAPI
- SQLAlchemy
- Databases

This makes unit testing simple and fast.

---

## Scalability

Infrastructure can evolve independently.

For example:

SQLite

↓

PostgreSQL

↓

Azure SQL

without changing business rules.

---

## Readability

Developers immediately know where code belongs.

Business logic is found in the Domain.

Workflow coordination lives in Application.

Database access lives in Infrastructure.

HTTP handling lives in API.

---

# Dependency Injection

PPST uses Dependency Injection to separate object creation from business logic.

Without Dependency Injection:

The route would manually create:

- Database Session
- Repository
- Service

This tightly couples every layer together.

Instead, PPST creates dependencies inside the Bootstrap layer.

Example flow:

FastAPI Route

↓

Container

↓

Repository

↓

Service

↓

Route receives a fully constructed service.

Benefits:

- Easier testing
- Better modularity
- Lower coupling
- Cleaner code

---

# Contracts

PPST never exposes database models directly.

Instead, every service communicates through contracts.

Example:

Request

↓

ItemCreateRequest

↓

Application Service

↓

ItemResponse

↓

Client

Contracts provide:

- Stable APIs
- Validation
- Clear boundaries
- Documentation through OpenAPI

If the database changes, the API contract can remain unchanged.

---

# Repository Pattern

Application services never communicate directly with SQLAlchemy.

Instead they use repositories.

Application

↓

Repository

↓

Database

Responsibilities of the Repository:

- Create
- Read
- Update
- Delete

Repositories know how data is stored.

Application services know what should happen.

This separation keeps business logic independent from persistence.

---

# Service Layer

The service layer coordinates application workflows.

Example:

Create Item

↓

Repository.create()

↓

Domain Rules

↓

Response Contract

Services answer:

"What sequence of operations should occur?"

Services should never contain SQLAlchemy code.

Services should never contain HTTP logic.

---

# PPST Design Rules

Every service built on PPST follows the same engineering rules.

✓ Routes never contain business logic.

✓ Services never contain SQLAlchemy.

✓ Repositories never contain business rules.

✓ Domain never depends on infrastructure.

✓ Configuration comes from one place.

✓ Logging is centralized.

✓ Exceptions are handled globally.

Following these rules keeps every backend service consistent across the Patel Engineering ecosystem.

---

# Phase 2 Summary

At the end of Phase 2 you should understand:

✓ Why PPST separates responsibilities

✓ How the four layers communicate

✓ Why Dependency Injection exists

✓ Why repositories isolate persistence

✓ Why services coordinate workflows

✓ Why contracts protect the API

These principles remain the same for every future PPST-based service, regardless of its business domain.


# Phase 3 — Engineering Components

# Engineering Components

PPST is composed of several reusable engineering components.

Each component has one responsibility and is designed to be reused across every backend service.

Together, these components provide the infrastructure required for building maintainable and scalable applications.

---

# Configuration

Location

app/core/config.py

Purpose

Provide a single source of truth for application configuration.

Responsibilities

- Environment variables
- Database configuration
- Application settings
- Future cloud configuration

Instead of scattering configuration throughout the project, every component retrieves settings from one location.

Example

DATABASE_URL

DEBUG

PROJECT_NAME

VERSION

Benefits

- No hardcoded values
- Easier deployments
- Environment-specific configuration
- Better maintainability

---

# Dependency Injection

Location

app/bootstrap/container.py

Purpose

Construct application dependencies.

Responsibilities

- Create repositories
- Create services
- Inject dependencies into API routes

Instead of routes creating objects directly, the container assembles the application.

Example

Database Session

↓

Repository

↓

Application Service

↓

API Route

Benefits

- Loose coupling
- Easier testing
- Replaceable implementations
- Clear object ownership

---

# Repository Pattern

Location

app/infrastructure/repositories/

Purpose

Isolate database operations from business logic.

Responsibilities

- INSERT
- SELECT
- UPDATE
- DELETE

Repositories communicate with SQLAlchemy.

Application services never execute SQL directly.

Benefits

- Database independence
- Easier testing
- Cleaner services
- Easier migrations

---

# Domain Rules

Location

app/domain/

Purpose

Contain business knowledge.

Examples

Inventory API

ItemRules

Data Ingestion Pipeline

DocumentRules

The domain decides business behavior.

Examples

Low stock threshold

Supported document types

Validation policies

Business rules should never depend on FastAPI or SQLAlchemy.

Benefits

- Centralized business logic
- Easier maintenance
- Reusable policies
- Framework independence

---

# Application Services

Location

app/application/

Purpose

Coordinate business workflows.

Services answer the question:

"What should happen?"

Responsibilities

- Coordinate repositories
- Execute business rules
- Build response contracts
- Raise application exceptions

Services should never know how the database works.

Benefits

- Clear orchestration
- Easier testing
- Predictable workflows

---

# API Contracts

Location

app/application/contracts/

Purpose

Define communication between clients and the application.

Types

Request Models

Response Models

Error Models

Contracts prevent exposing internal database models to external clients.

Benefits

- Stable APIs
- Validation
- Documentation
- Loose coupling

---

# Global Exception Handling

Location

app/core/handlers.py

Purpose

Provide consistent error handling across the application.

Instead of returning different error formats from different routes, every exception is transformed into a standardized response.

Example

{
    "success": false,
    "error": {
        "type": "NotFoundException",
        "message": "Item not found"
    }
}

Benefits

- Consistent APIs
- Easier debugging
- Better client integration

---

# Structured Logging

Location

app/infrastructure/logging/

Purpose

Capture application behavior.

Logging records

Incoming requests

Outgoing responses

Execution time

HTTP status

Errors

Example

START GET /documents

END GET /documents

STATUS=200

TIME=0.012s

Benefits

- Debugging
- Monitoring
- Performance analysis
- Production troubleshooting

---

# Event Bus

Location

app/events/

Purpose

Allow components to communicate without direct dependencies.

Instead of calling another service directly, components publish events.

Example

Document Uploaded

↓

Event Bus

↓

Worker

↓

Document Processing

Benefits

- Loose coupling
- Asynchronous processing
- Scalable architecture

---

# Workers

Location

app/workers/

Purpose

Execute background processing.

Examples

Document processing

Embedding generation

Cost analysis

Notifications

Workers allow long-running tasks to execute outside HTTP requests.

Benefits

- Faster APIs
- Better scalability
- Asynchronous execution

---

# Testing

Location

tests/

Purpose

Verify business behavior.

Current coverage

Application services

Business rules

Future coverage

Repositories

API routes

Workers

Integration tests

Benefits

- Regression prevention
- Safer refactoring
- Higher confidence

---

# Why These Components Exist

Each engineering component solves one specific problem.

Configuration manages settings.

Dependency Injection manages object creation.

Repositories manage persistence.

Services manage workflows.

Domain manages business knowledge.

Contracts manage communication.

Logging records behavior.

Exception handling standardizes failures.

Workers execute background tasks.

Events connect independent components.

Together these components form the reusable engineering foundation of PPST.

# Phase 4 — Developer Handbook

---

# Building a New Service with PPST

PPST is designed to be reused.

Instead of creating every backend application from scratch, new services begin by copying PPST and replacing only the business domain.

The engineering architecture remains identical.

This provides consistency across every service in the Patel Engineering ecosystem.

---

# Development Workflow

Every new service follows the same engineering workflow.

                Copy PPST
                     │
                     ▼
             Rename Project
                     │
                     ▼
             Replace Domain
                     │
                     ▼
        Implement Business Rules
                     │
                     ▼
         Replace Repository Logic
                     │
                     ▼
          Register Dependencies
                     │
                     ▼
             Register Routes
                     │
                     ▼
               Run Tests
                     │
                     ▼
              Commit & Push

Following the same workflow for every project creates predictable engineering practices and reduces maintenance complexity.

---

# Step 1 — Copy PPST

Create a copy of the PPST repository.

Example:

patel-platform-service-template

↓

patel-data-ingestion-pipeline

PPST remains the master template.

The new repository becomes the business application.

---

# Step 2 — Rename the Domain

PPST contains an example domain called Item.

Replace the example domain with your business domain.

Example:

Item

↓

Document

This includes:

• Domain Rules

• Application Service

• Repository

• Database Model

• API Routes

• Request Contracts

• Response Contracts

The infrastructure remains unchanged.

---

# Step 3 — Keep the Architecture

The project structure should remain identical.

app/

    api/

    application/

    bootstrap/

    core/

    domain/

    events/

    infrastructure/

    workers/

Do not remove layers because a project is small.

Consistency is more valuable than reducing folders.

---

# Step 4 — Add Business Rules

Business knowledge belongs only inside the Domain layer.

Example:

DocumentRules.is_supported_file()

Business rules should never be placed inside:

• API Routes

• Repository

• SQLAlchemy Models

• Infrastructure

The Domain layer should remain independent of frameworks and databases.

---

# Step 5 — Build the Application Service

The Application layer coordinates the workflow.

Example:

Route

↓

DocumentService

↓

Repository

↓

Domain Rules

↓

Response Contract

The service answers the question:

"What needs to happen?"

It should not contain SQL queries or HTTP logic.

---

# Step 6 — Repository Responsibilities

Repositories communicate with the database.

Responsibilities include:

• Create

• Read

• Update

• Delete

Repositories should never contain business rules.

Their responsibility is persistence only.

---

# Step 7 — Dependency Injection

Dependencies are assembled inside the Bootstrap layer.

Routes receive fully configured services.

Route

↓

DocumentService

↓

DocumentRepository

↓

Database Session

Routes should never manually instantiate repositories or services.

Dependency Injection improves maintainability, testing, and flexibility.

---

# Step 8 — Register Routes

Each service registers its router inside the Application Factory.

Example:

app.include_router(document_router)

This allows new features to be added without changing the application's architecture.

---

# Step 9 — Verify the Service

Before committing code, verify:

✓ Swagger loads correctly

✓ CRUD endpoints work

✓ Logging works

✓ Exception handling works

✓ Structured error responses are returned

✓ Unit tests pass

Every milestone should end with a stable, working application.

---

# Step 10 — Commit the Milestone

Commit only completed engineering milestones.

Example:

git add .

git commit -m "Complete document domain migration from PPST template"

git push origin main

A clean Git history tells the engineering story of the project.

Each commit should represent one meaningful improvement.

---

# Engineering Principles

Every service built from PPST should follow the same principles.

Business Rules belong in the Domain.

Application Services coordinate workflows.

Repositories communicate with the database.

Routes remain thin.

Configuration comes from config.py.

Logging is centralized.

Exceptions are handled globally.

Dependencies are injected.

Every feature is tested.

Every milestone is documented.

Consistency is more valuable than cleverness.

---

# Migration Checklist

Before considering a migration complete, verify:

✓ Domain renamed

✓ Contracts updated

✓ Repository replaced

✓ Service implemented

✓ Routes registered

✓ Dependency Injection configured

✓ Database models updated

✓ Logging verified

✓ Error handling verified

✓ Tests passing

✓ README updated

✓ GitHub pushed



# Phase 5 — Building Services with PPST

## From Template to Platform

PPST is not an application.

It is an engineering foundation.

Every backend service begins with the same architecture and engineering standards before business-specific functionality is introduced.

Instead of designing a new project from scratch each time, developers clone PPST and replace only the business domain.

The infrastructure, architecture, and engineering practices remain consistent across every service.

---

# Engineering Workflow

Every service developed from PPST follows the same lifecycle.

```
Architecture

↓

Implementation

↓

Testing

↓

Debugging

↓

Documentation

↓

Release

↓

Cloud Deployment

↓

Maintenance
```

This ensures every project follows the same engineering process from its first commit through production deployment.

---

# Service Development Workflow

When creating a new service, the recommended process is:

1. Clone PPST.
2. Rename the project.
3. Replace the domain model.
4. Replace business rules.
5. Implement repositories.
6. Implement application services.
7. Expose API endpoints.
8. Write unit tests.
9. Update the README.
10. Deploy.

Everything else remains unchanged.

---

# Example

Creating an Inventory API requires replacing:

```
Item
```

Creating a Data Ingestion Pipeline requires replacing:

```
Document
```

Creating an Authentication Service requires replacing:

```
User
```

Creating a Retrieval Service requires replacing:

```
Embedding
```

The architecture remains exactly the same.

---

# Reusable Engineering Components

Every service automatically inherits:

- Clean Architecture
- Dependency Injection
- Repository Pattern
- Configuration Management
- Structured Logging
- Global Exception Handling
- Standard Response Models
- Unit Testing
- Worker Support
- Event Support
- Docker Support

Business logic changes.

Infrastructure does not.

---

# Engineering Standards

Every PPST-based service should satisfy the following checklist before release.

## Architecture

- Clean Architecture
- Separation of Concerns
- Single Responsibility Principle
- Repository Pattern
- Dependency Injection

## Quality

- Unit tests passing
- No hardcoded configuration
- Structured logging
- Global exception handling
- Consistent API contracts

## Deployment

- Environment-variable configuration
- Docker support
- Production-ready configuration

---

# PPST Ecosystem

PPST serves as the common engineering foundation for every Patel Engineering backend service.

```
                     PPST

                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼

 Inventory API   Data Ingestion   Cost Intelligence

      │                 │                 │
      └──────────────┬────────────────────┘
                     │
                     ▼

           Retrieval Service

                     │
                     ▼

             Authentication Service
```

Every service shares the same engineering principles while implementing different business capabilities.

---

# Azure Platform Vision

After PPST reaches v0.1.0, every service will be deployed using the same cloud architecture.

```
                 Azure

        Azure Container Apps
                 │
                 ▼

             PPST v0.1.0

                 │
─────────────────┼────────────────────

Inventory API

Cost Intelligence

Data Ingestion Pipeline

Retrieval Service

Authentication Service
```

This provides a consistent deployment strategy, operational model, and development experience across the entire platform.

---

# Future Roadmap

PPST v0.1.0 establishes the engineering foundation.

Future versions may introduce additional capabilities, including:

- Background job scheduling
- Authentication and authorization
- Event-driven messaging
- Distributed caching
- Observability and tracing
- CI/CD pipelines
- Kubernetes support
- Azure-native integrations

These enhancements should extend the platform without changing its architectural principles.

---

# Conclusion

PPST represents a long-term engineering standard rather than a single project.

Its purpose is to eliminate repetitive infrastructure work so developers can focus on solving business problems.

By enforcing consistent architecture, reusable engineering components, and standardized development practices, PPST enables backend services to remain maintainable, scalable, and production-ready throughout their lifecycle.

The goal is simple:

**Build the platform once. Reuse it everywhere.**



