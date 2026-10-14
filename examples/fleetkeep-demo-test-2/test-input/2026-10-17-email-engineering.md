From: Engineering lead
Date: 17 Oct 2026
Subject: Anchor dates and VOR

Two things from looking at the code. Anchor dates are stored per vehicle today, but nothing stops two
vehicles sharing a record when a vehicle is re-registered, which could double up their schedules.
And we have no field for when a vehicle went VOR, so we can't pause anything while it's off the road.
Who decides whether the schedule pauses while a vehicle is VOR?
