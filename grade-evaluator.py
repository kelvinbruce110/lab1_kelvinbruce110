#!/usr/bin/python3

import csv
import sys
import os


def load_csv_data():

    """
    Prompts the user for a filename, checks if it exists,
    validates CSV structure, and extracts fields into a list of dictionaries.
    """

    filename = input(
        "Enter the name of the CSV file to process (e.g., grades.csv): "
    ) or "grades.csv"



    # Check if file exists

    if not os.path.exists(filename):

        print(
            f"[ERROR] The file '{filename}' was not found."
        )

        sys.exit(1)



    # Check if file is empty

    if os.path.getsize(filename) == 0:

        print(
            "[ERROR] The CSV file is empty."
        )

        sys.exit(1)



    assignments = []

    bad_rows = 0



    try:

        with open(
            filename,
            mode="r",
            encoding="utf-8"
        ) as file:


            reader = csv.DictReader(file)



            # Check CSV headers

            if reader.fieldnames is None:

                print(
                    "[ERROR] CSV file has no header row."
                )

                sys.exit(1)



            required_columns = [
                "assignment",
                "group",
                "score",
                "weight"
            ]



            for column in required_columns:

                if column not in reader.fieldnames:

                    print(
                        f"[ERROR] Missing required column: {column}"
                    )

                    sys.exit(1)




            # Read rows

            for row_number, row in enumerate(reader, start=2):


                assignment = row.get(
                    "assignment",
                    ""
                ).strip()


                group = row.get(
                    "group",
                    ""
                ).strip().capitalize()


                score_value = row.get(
                    "score",
                    ""
                ).strip()


                weight_value = row.get(
                    "weight",
                    ""
                ).strip()



                # Check missing fields

                if (
                    not assignment
                    or not group
                    or score_value == ""
                    or weight_value == ""
                ):

                    print(
                        f"[WARNING] Row {row_number} has missing values. Skipped."
                    )

                    bad_rows += 1

                    continue




                try:

                    score = float(score_value)

                    weight = float(weight_value)



                except ValueError:

                    print(
                        f"[WARNING] Row {row_number} has invalid numbers. Skipped."
                    )

                    bad_rows += 1

                    continue




                assignments.append(
                    {
                        "assignment": assignment,
                        "group": group,
                        "score": score,
                        "weight": weight
                    }
                )




        if bad_rows > 0:

            print(
                f"[WARNING] {bad_rows} bad row(s) were skipped."
            )



        return assignments



    except Exception as error:

        print(
            f"[ERROR] Could not read CSV file: {error}"
        )

        sys.exit(1)





def evaluate_grades(data):

    print(
        "\n------ Processing Grades ------"
    )



    if not data:

        print(
            "[ERROR] No assignment data available."
        )

        sys.exit(1)




    # TODO: a) Check if all scores are between 0-100

    valid_data = []



    for assignment in data:


        if (
            0 <= assignment["score"] <= 100
        ):

            valid_data.append(assignment)



        else:

            print(
                f"[WARNING] {assignment['assignment']} "
                f"has invalid score {assignment['score']}."
            )



    data = valid_data




    if not data:

        print(
            "[ERROR] No valid assignments remain."
        )

        sys.exit(1)




    # TODO: b) Validate total weights

    weights = {

        "total": 0,

        "Formative": 0,

        "Summative": 0

    }



    for assignment in data:


        weights["total"] += assignment["weight"]



        if assignment["group"] == "Formative":

            weights["Formative"] += assignment["weight"]



        elif assignment["group"] == "Summative":

            weights["Summative"] += assignment["weight"]




    print(
        f"Formative weight: {weights['Formative']}/60"
    )

    print(
        f"Summative weight: {weights['Summative']}/40"
    )

    print(
        f"Total weight: {weights['total']}/100"
    )



    if weights["total"] != 100:

        print(
            "[ERROR] Total weight must equal 100."
        )

        sys.exit(1)



    if weights["Formative"] != 60:

        print(
            "[ERROR] Formative weight must equal 60."
        )

        sys.exit(1)



    if weights["Summative"] != 40:

        print(
            "[ERROR] Summative weight must equal 40."
        )

        sys.exit(1)




    print(
        "All weights are correctly calibrated."
    )




    # TODO: c) Calculate Final Grade and GPA


    total_grade = 0



    for assignment in data:


        total_grade += (
            assignment["score"]
            *
            assignment["weight"]
            /
            100
        )



    GPA = (
        total_grade / 100
    ) * 5.0



    print(
        f"Final Grade = {round(total_grade,2)}%"
    )


    print(
        f"GPA = {round(GPA,2)}/5.0"
    )





    # TODO: d) Determine Pass/Fail status


    scores = {

        "Formative": 0,

        "Summative": 0

    }



    for assignment in data:


        contribution = (

            assignment["score"]
            *
            assignment["weight"]
            /
            100

        )



        if assignment["group"] == "Formative":

            scores["Formative"] += contribution



        elif assignment["group"] == "Summative":

            scores["Summative"] += contribution





    formative_percentage = (
        scores["Formative"] / 60
    ) * 100



    summative_percentage = (
        scores["Summative"] / 40
    ) * 100




    if (
        formative_percentage >= 50
        and summative_percentage >= 50
    ):

        status = "PASSED"



    else:

        status = "FAILED"





    print(
        f"Formative performance: {round(formative_percentage,2)}%"
    )


    print(
        f"Summative performance: {round(summative_percentage,2)}%"
    )





    # TODO: e) Find highest-weight failed formative assignments


    failed_formative = []



    for assignment in data:


        if (
            assignment["group"] == "Formative"
            and assignment["score"] < 50
        ):

            failed_formative.append(assignment)




    highest_weight = 0



    for assignment in failed_formative:


        if assignment["weight"] > highest_weight:

            highest_weight = assignment["weight"]




    resubmission = []



    for assignment in failed_formative:


        if assignment["weight"] == highest_weight:

            resubmission.append(
                assignment["assignment"]
            )





    # TODO: f) Print final decision


    print(
        "\n------ Final Decision ------"
    )



    print(
        f"Status: {status}"
    )



    if resubmission:

        print(
            "Available for resubmission:"
        )


        for assignment in resubmission:

            print(
                f"- {assignment}"
            )



    else:

        print(
            "Available for resubmission: None"
        )





if __name__ == "__main__":


    course_data = load_csv_data()


    evaluate_grades(course_data)
