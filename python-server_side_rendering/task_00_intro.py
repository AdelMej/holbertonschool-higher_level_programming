import os


def generate_invitations(template, attendees):
    if (not isinstance(template, str)
            or not isinstance(attendees, list)):
        print("Template is not a string or Attendees is not a list")
        return

    for value in attendees:
        if not isinstance(value, dict):
            print("A²tendees contains none dict object")
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    idx = 1
    for attendee in attendees:
        output = (
                template
                .replace("{name}", attendee["name"] or "N/A")
                .replace("{event_title}", attendee["event_title"] or "N/A")
                .replace("{event_date}", attendee["event_date"] or "N/A")
                .replace("{event_location}", attendee["event_location"] or "N/A")
        )

        filename = "output_" + str(idx) + ".txt"
        with open(filename, "w") as f:
            f.write(output)

        idx += 1
