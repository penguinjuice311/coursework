```mermaid
erDiagram

Walker ||--o{Appointment: Has
Appointment ||--o{Placement: Has
Owner ||--o{Placement: Placed
Walker ||--o{Review: Reviewed
Owner ||--o{Review: Reviews

Walker {
  string WalkerEmailAdress pk
  string Biography 
  string Fname
  string Lname
  int Rate 
  bitfield WalkerOptions
  string Password }

Owner {
  string OwnerEmailAdress pk
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
  time Time }

Placement {
  int AppointmentID fk
  int OwnerEmailAdress fk
  int PetsNumber
  bool Repeat
  bitfield PlacementOptions
  nstring SpecialRequirements }

Review {
  int OwnerEmailAdress fk
  int WalkerEmailAdress fk
  int Stars
  int Comment }

```
