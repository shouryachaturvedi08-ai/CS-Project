# Project Statement

## Problem Statement

Most people know their weight and height, but very few translate that into something
actually useful. A number like "72 kg" or "175 cm" doesn't tell anyone whether they're
healthy — and the free BMI calculators available online usually stop at giving you a
single number and a one-word label ("Overweight") with no real context about what that
means for *your* body or what to do about it.

There's also a smaller, more personal gap: most calculators are built for one person at
a time. If you're a trainer, a doctor's assistant, a hostel warden, or just someone
tracking BMI for their whole family, you end up running the same calculator over and
over and manually copying results into a spreadsheet.

This project — the **BMI Calculator with Gender-Aware Health Advisory** — was built to
close both gaps: it computes BMI accurately from either metric or imperial input,
explains the category in plain language with gender-specific health consequences and
practical cures, and lets a user process an entire group of people in one sitting,
ending with a clean, colour-coded summary table.

## Scope of the Project

The scope is deliberately focused: this is a **command-line, single-session health
utility**, not a full health-records system. Within that scope, it covers:

- Accepting weight in **kilograms or pounds**, and height in **centimetres or inches**,
  with automatic internal conversion to SI units before calculation.
- Calculating BMI using the standard formula `weight (kg) / height (m)²`.
- Classifying the result into one of **five clinically recognised BMI bands**
  (Underweight, Healthy Weight, Overweight, Obese Category I, Obese Category II).
- Giving **gender-specific** consequences and lifestyle recommendations for each band,
  since health risks and advice genuinely differ between men and women at the same BMI.
- Supporting **multiple people in one run**, so a family, a team, or a small clinic can
  be processed back-to-back.
- Producing a **consolidated, colour-coded table** at the end of the session summarising
  every person entered.

What is explicitly **out of scope** for this version: persistent storage (nothing is
saved once the program exits), a graphical interface, user accounts or authentication,
and medical diagnosis of any kind — the tool gives general wellness pointers, not a
clinical opinion, and is not a substitute for a doctor.

## Target Users

- **Individuals** who want a quick, honest BMI check with advice they can actually act on.
- **Fitness trainers and gym instructors** doing quick group assessments for new members.
- **School or hostel health coordinators** running periodic checks on groups of students.
- **Small clinics or community health camps** that need a fast, offline, no-install
  screening tool without setting up a full health-records system.

## High-Level Features

1. **Dual-unit input** — weight in kg/lb, height in cm/inches, converted automatically.
2. **Accurate BMI computation** using the standard international formula.
3. **Five-tier health classification** — Underweight, Healthy Weight, Overweight, Obese
   Category I, Obese Category II — each with its own colour code for at-a-glance reading.
4. **Gender-specific health guidance** — separate, realistic consequences and cures for
   men and women at every BMI level, instead of one generic message for everyone.
5. **Multi-person session support** — keep adding people until you're done, no restarts.
6. **Consolidated summary table** — every person's name, age, gender, BMI, category,
   consequences, and cure printed together at the end, colour-coded by severity.
7. **Friendly, colourful console experience** — powered by a small custom-built
   `minecolor` helper module so results are easy to scan even in a plain terminal.
