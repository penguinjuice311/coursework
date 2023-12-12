```mermaid
erDiagram

Walker ||--o{Appointment: Has
Appointment ||--o{Placement: Has
Owner ||--o{Placement: Placed
Walker ||--o{Review: Reviewed
Owner ||--o{Review: Reviews

Walker {
  string EmailAdress pk
  string Biography 
  string Fname
  string Lname
  bitfield Options
  string Password }

Owner {
  string EmailAdress pk
  string PhoneNumber 
  string Fname
  string Lname
  string Password }

Appointment {
  int AppointmentID pk
  int WalkerEmailAdress fk
  int Day 
  int MaxPets
  bitfield AppointmentOptions
  Bool Repeat
  time Time }

Placement {
  int AppointmentID fk
  int OwnerEmailAdress fk
  int PetsNumber
  bitfield PlacementOptions
  nstring SpecialRequirements }

Review {
  int EmailAdress fk
  int EmailAdress fk
  int Stars
  int Comment }

```
