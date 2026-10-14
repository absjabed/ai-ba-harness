# FleetKeep Demo: inspection rules (draft v2, Product owner, 2 Oct 2026)

1. Every vehicle has its own safety inspection interval, in whole weeks. There is no fleet-wide
   interval.
2. A vehicle's inspection schedule counts from its anchor date. The next due date is the anchor date
   plus a whole number of intervals; doing an inspection early or late doesn't move the schedule.
3. The dashboard shows each vehicle's inspection status: green when the next due date is more than
   14 days away, amber at 14 days or less, red when overdue.
4. An inspection done up to 7 days after its due date is not counted as overdue (grace period).
5. Every safety inspection includes a brake performance test, and its result is recorded.
6. Only a transport manager sets or changes a vehicle's interval or anchor date.
7. Vehicles that are VOR: to be decided.
