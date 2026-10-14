# Telemedicine Slot Booking & Prescription Portal

**Course/Lab:** Software Engineering Lab 3 — Component Modelling & Architectural Pattern Selection  
**Domain:** Healthcare & Telemedicine

## Overview

This lab focuses on selecting an architectural pattern and modelling the components of the Telemedicine Slot Booking & Prescription Portal. The selected approach is a **Layered Architecture**, separating presentation, business processing, and data management.

The architecture is intended to support the portal's core workflows: discovering physicians, viewing and booking consultation slots, conducting video consultations, and managing digital prescriptions.

## Selected Architectural Pattern: Layered Architecture

The system is divided into three layers.

### 1. Presentation Layer

Contains the user-facing interfaces:

- **Patient Portal UI** — supports doctor discovery, viewing available slots, booking consultations, and downloading prescriptions.
- **Physician Dashboard** — supports appointment management, consultation access, and prescription-related actions.

### 2. Business Layer

Contains the components responsible for application logic:

- **Booking Manager** — handles doctor/slot discovery and booking-related operations.
- **Teleconsult Service** — manages consultation functionality and room-link operations.
- **Prescription Service** — manages prescription creation, signing, and retrieval.

### 3. Data Layer

Contains data storage and security-related components:

- **Slot & Booking Database** — stores slot and booking information.
- **Encryption Module** — provides encryption and decryption operations for sensitive data.
- **Prescription Store** — stores and retrieves prescriptions and supports signature verification.

### External Component

- **Video Consultation Provider** — an external service used for video-meeting operations.

## Component Diagram

The UML component diagram in the Lab 3 report illustrates the components across all three layers and their interfaces. It shows the Patient Portal UI and Physician Dashboard in the Presentation Layer; the Booking Manager, Teleconsult Service, and Prescription Service in the Business Layer; and the Slot & Booking Database, Encryption Module, and Prescription Store in the Data Layer. The Video Consultation Provider appears as an external component.

## Why Layered Architecture?

### Separation of concerns

Separating user interaction, business processing, and data management makes the system easier to understand, maintain, and modify. For example, interface changes can be made without directly changing booking or prescription logic.

### Suitability for telemedicine functions

The layers separate slot booking, video consultation, and prescription management into dedicated components. The Booking Manager handles appointment-related operations, the Teleconsult Service manages consultation functionality, and the Prescription Service manages digital prescriptions.

### Security advantage

Security mechanisms can be centralized in components such as the Encryption Module and Prescription Store. This helps protect sensitive consultation and prescription information before it is stored or exchanged between components.

### Performance benefit

Dedicated business and data components can handle frequently accessed operations such as viewing available slots and booking consultations, helping reduce unnecessary processing and support efficient responses.

## Key Design Components

| Layer | Component | Responsibility |
|---|---|---|
| Presentation | Patient Portal UI | Doctor discovery, slot viewing, booking, prescription download |
| Presentation | Physician Dashboard | Appointment and consultation access, prescription actions |
| Business | Booking Manager | Doctor/slot discovery and booking operations |
| Business | Teleconsult Service | Consultation and room-link operations |
| Business | Prescription Service | Prescription creation, signing, and retrieval |
| Data | Slot & Booking Database | Slot and booking data storage |
| Data | Encryption Module | Data encryption and decryption |
| Data | Prescription Store | Prescription storage, retrieval, and signature verification |
| External | Video Consultation Provider | External video-meeting functionality |


## Author

**J Pavithra**  
**SRN:** PES2UG24CS198
