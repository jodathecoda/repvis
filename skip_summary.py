# Open the file
with open('filename.txt', 'r') as file:
    # Initialize a flag to store whether we are inside the summary or not
    inside_summary = False
    # Iterate over the file
    for line in file:
        # Check if the line is "*** SUMMARY ***"
        if line.strip() == "*** SUMMARY ***":
            # If it is, set the flag to True
            inside_summary = True
        # Check if the line is empty
        elif line.strip() == "PokerStars":
            # If it is, set the flag to False
            inside_summary = False
        # If the flag is False, print the line
        elif not inside_summary:
            print(line)