# Inspections workshop, 14 Oct 2026 (Lead BA's notes)

Present: Product owner, Lead BA, Compliance adviser, Pilot transport manager (Ravi Menon, 07700 900123),
Engineering lead.

- Every vehicle has a safety inspection interval, set per vehicle. Pilot uses 6 weeks for HGVs and
  8 weeks for vans. Compliance adviser: the regulator expects the interval to be written down per
  vehicle, not per fleet.
- Product owner: "The next due date is calculated from the anchor date, not from when the last
  inspection actually happened. A late inspection doesn't move the schedule." Decided.
- Ravi said they usually move the due date forward when an inspection is done early. Product owner
  disagreed - early is fine, schedule stays anchored. Ravi not convinced.
- Banding on the dashboard: green if due in more than 14 days, amber 14 days or less, red when
  overdue. Product owner: agreed, ship it like that.
- Engineering lead asked what happens to the due date when a vehicle is VOR for a long time. Nobody
  knew. Product owner to think about it.
- Brake tests: Compliance adviser said a brake performance test is needed at every safety inspection.
  Should FleetKeep block closing an inspection without a brake test result? Product owner: "probably
  yes, but let me check with the pilot".
- The dashboard needs to load fast for big fleets.
- Action: Compliance adviser to send the regulator's inspection-interval guidance by 21 Oct.
- Action: Engineering lead to check how anchor dates are stored today, by 17 Oct.
- Term: "anchor date" = the date the inspection schedule counts from. Ravi calls it the "start date".
