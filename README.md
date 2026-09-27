# BMI Calculator with Gender-Aware Health Advisory

A colour-coded, command-line BMI calculator that goes beyond a single number — it
classifies the result into a clinical category and gives gender-specific health
consequences and practical advice, for one person or a whole group in a single session.

Built as a **VITyarthi "Build Your Own Project"** submission.

---

## Overview

Type in a name, age, gender, weight (kg or lb) and height (cm or inches), and the
program calculates BMI, tells you which of five health categories you fall into, and
prints tailored consequences and cures for that category — with different advice for
men and women, since the same BMI carries different risks across genders. Keep adding
people, and at the end the program prints one consolidated, colour-coded table for
everyone entered in that session.

## Features

- **Two weight units** (kilograms / pounds) and **two height units**
  (centimetres / inches), converted internally before calculation.
- **Standard BMI formula** — `weight (kg) ÷ height (m)²`.
- **Five BMI categories**: Underweight, Healthy Weight, Overweight, Obese Category I,
  Obese Category II — each mapped to its own terminal colour (blue, green, yellow,
  magenta, red) so results are readable at a glance.
- **Gender-specific consequences and cures** for every category — men and women get
  different, realistic guidance rather than one generic message.
- **Multi-person sessions** — keep entering people one after another until you choose
  to stop.
- **Consolidated summary table** at the end, colour-coded by BMI category.
- **Input validation** — invalid gender, unit, or height choices are caught with clear
  error messages instead of crashing silently.

## Technologies / Tools Used

| Tool / Library     | Purpose                                              |
|--------------------|-------------------------------------------------------|
| Python 3           | Core implementation language                          |
| `minecolor` (custom, local module — included in this repo) | ANSI colour constants for terminal output |
| Standard library only | No external/third-party packages required to run   |
| Git & GitHub       | Version control and submission                        |

> `minecolor.py` is **not** a package from PyPI — it's a small local helper module
> (included right here in the repository) that defines ANSI escape-code constants
> such as `RED`, `GREEN`, `CYAN`, `BOLD`, and `RESET`. It must sit in the same folder
> as `sc_bmi_calculator.py` for the import to succeed.

## Project Structure

```
.
├── sc_bmi_calculator.py     # Main program: BMI engine, categoriser, table, CLI loop
├── minecolor.py             # Local helper module — ANSI colour constants
├── README.md                # This file
├── statement.md             # Problem statement, scope, target users, features
├── assets/
│   └── bmi_calculator_screenshot.png   # Real terminal session (see Screenshots below)
└── report/
    └── BMI_Calculator_Project_Report.pdf
```

## Steps to Install & Run

1. **Make sure Python 3.8+ is installed.**
   ```bash
   python3 --version
   ```
2. **Clone this repository.**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
3. **No external dependencies to install** — the project uses only the Python standard
   library plus the bundled `minecolor.py`, so there's no `requirements.txt` to run.
4. **Run the program.**
   ```bash
   python3 sc_bmi_calculator.py
   ```
5. **Follow the on-screen prompts** — name, age, gender, weight unit + value, height
   unit + value. After each person's result, you'll be asked whether to add another;
   answer `NO` (exactly, in capitals) when you're done, and the summary table prints
   automatically.

## Instructions for Testing

There's no separate automated test suite bundled with this CLI version, so testing is
done through guided manual runs — which is straightforward given the program's simple,
linear input flow:

1. **Happy-path test** — run the program and enter a normal set of values (e.g. weight
   `72 kg`, height `175 cm`, gender `men`). Confirm the BMI, category, and advice all
   make sense and the colours match the category (green for Healthy Weight, etc.).
2. **Unit-conversion test** — repeat with weight in `lb` and height in `inches` for the
   same real-world body size, and confirm the resulting BMI is (near) identical to the
   metric run.
3. **Boundary test** — try values right around the category edges (BMI ≈ 18.5, 25, 30,
   35) to confirm each band's cut-off is applied correctly.
4. **Invalid-input test** — enter an invalid gender (e.g. `other`) or an invalid unit
   choice (e.g. `3`) and confirm the program prints a clear error and exits gracefully
   instead of crashing.
5. **Multi-person test** — add 2–3 people in one run, answer `YES` to continue after
   each, then `NO` at the end, and confirm the final table lists every person correctly
   with matching colours.

A worked example of exactly this kind of run is shown in the screenshot below.

## Screenshots

The screenshot below is a genuine terminal session — two users (Aarav, a man at
23.51 BMI, and Priya, a woman at 22.66 BMI) were run through the program back-to-back,
ending with the consolidated summary table. Both fall into the **Healthy Weight**
category, shown in green throughout.

![BMI Calculator terminal session — individual results and final summary table](assets/bmi_calculator_screenshot.png)

## Notes on This Implementation

The program is currently implemented as a single, well-organised script
(`sc_bmi_calculator.py`) split internally into four clear responsibilities —
`calculator_bmi()` for the maths, `category_bmi()` for classification and advice,
`table()` for reporting, and `bmi()` as the interactive controller. See
`report/BMI_Calculator_Project_Report.pdf` for the full architecture, workflow, and UML
diagrams, along with design decisions, testing approach, and ideas for future
enhancements (including splitting this into separate module files and adding persistent
storage).
