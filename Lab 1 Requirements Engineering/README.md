# Telemedicine Slot Booking & Prescription Portal

**Course/Lab:** Software Engineering Lab 1 – Requirements Engineering & UML Use-Case Modelling  
**Problem Statement:** #11 – Telemedicine Slot Booking & Prescription Portal  
**Domain:** Healthcare & Telemedicine

## Overview

The Telemedicine Slot Booking & Prescription Portal is designed to help patients find physicians, book available video consultation slots, access consultation details, and download digitally signed prescriptions when issued. Attending physicians can manage consultations and create prescriptions, while an external tele-consultation service supports the generation of encrypted consultation-room links.

This repository documents the system's requirements and use-case modelling for Lab 1.

## Actors

- **Patient** — views physicians and available slots, books a consultation, receives booking confirmation, and downloads an issued prescription.
- **Attending Physician** — conducts confirmed consultations and authors and digitally signs prescriptions.
- **Tele-consultation Service** — supporting external actor that helps provide encrypted consultation-room links. This actor is inferred from the room-link requirement.

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-001 | Allow attending physicians to author and digitally sign structured prescriptions, compiled into downloadable PDF records. |
| FR-002 | Allow patients to view physicians and specialties and select an available video consultation slot. |
| FR-003 | Book a selected slot and create a unique booking record containing the patient, physician, date, and time. |
| FR-004 | Generate and deliver an encrypted tele-consultation room link for each confirmed booking to the patient and attending physician. |
| FR-005 | Allow the attending physician to access and complete a confirmed consultation and make an issued digitally signed prescription available to the patient. |

## Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-001 | Encrypt video-session metadata and patient clinical notes in transit using TLS 1.3 and at rest using AES-256. |
| NFR-002 | Under the defined simulated peak-load test, at least 95% of slot-view and booking requests should complete within 3 seconds, without duplicate bookings. |

## Use-Case Diagram

The use-case diagram models the interactions between the Patient, Attending Physician, and Tele-consultation Service.

The main use cases are:

- View Physician & Slots
- Validate Slot Availability
- Book Consultation Slot
- Generate Encrypted Room Link
- Receive Booking Confirmation
- Conduct Video Consultation
- Author & Sign Prescription
- Download Signed Prescription

## Main Use Case: Book Video Consultation Slot

### Preconditions

- The patient is authenticated in the portal.
- Attending physicians and their available consultation slots are registered.
- The selected physician has at least one available slot.
- The telemedicine booking service is available.

### Main Success Scenario

1. The patient selects a physician or specialty.
2. The system displays available video consultation slots.
3. The patient selects a preferred date and time.
4. The system validates that the selected slot is still available.
5. The system creates a unique booking record with the patient, physician, date, and time.
6. The system marks the slot as booked.
7. The system generates an encrypted consultation-room link.
8. The system associates the link with the booking and makes it available to the patient and physician.
9. The system displays the booking confirmation and consultation details.
10. The use case ends successfully.

### Alternate Flows

- **Selected slot is no longer available:** The system informs the patient and displays the currently available slots. The patient selects another slot, which the system validates before continuing.
- **Room-link generation fails:** The system does not indicate that consultation-room access is ready. It records the failure and prompts the patient to retry or select another available slot after the booking state has been safely handled.

### Postconditions

- A unique booking record exists for the selected patient, physician, date, and time.
- The selected slot is marked as booked and is unavailable to other patients.
- An encrypted consultation-room link is generated and associated with the confirmed booking.
- The patient and attending physician can access the consultation details.

## Acceptance Criteria Highlights

- Prescriptions must include validated physician identity/license information and a valid digital signature.
- Patients must only be able to book available consultation slots.
- Each successful booking must have a unique booking ID and all required booking details.
- Each confirmed booking must have a protected consultation-room link accessible only to the authorized patient and physician.
- An issued signed prescription must be linked to the consultation and downloadable by the authorized patient.
- Security testing must verify the stated encryption requirements.
- Load testing must meet the stated 3-second target for at least 95% of slot-view and booking requests without duplicate bookings.

## Scope Note

This README describes the requirements and UML use-case modelling documented for **Lab 1**. It does not claim that a working software implementation, database, API, or deployment is included.

## Author

**J Pavithra**  
**SRN:** PES2UG24CS198
