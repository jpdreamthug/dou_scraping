import csv


def save_vacancies_to_csv(vacancies, filename):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Title",
                    "Company Name",
                    "Date",
                    "Location",
                    "Salary",
                    "Keywords Found",
                ]
            )

            for vacancy in vacancies:
                writer.writerow(
                    [
                        vacancy.title or "",
                        vacancy.company_name or "",
                        vacancy.date or "",
                        (
                            ", ".join(vacancy.location)
                            if vacancy.location
                            else ""
                        ),
                        vacancy.salary or "",
                        (
                            ", ".join(vacancy.keywords_found)
                            if vacancy.keywords_found
                            else ""
                        ),
                    ]
                )
    except OSError as e:
        raise OSError(f"Error writing to file {filename}: {e}")
