def count_helper(colors):
    triple_a_count = 0
    triple_b_count = 0

    triple_a_found = False
    triple_b_found = False

    i = 0
    while i < len(colors) - 2:
        if colors[i] == "A":
            if triple_b_found:
                triple_b_found = False
            if not triple_a_found:
                if colors[i] == "A" and colors[i + 1] == "A" and colors[i + 2] == "A":
                    triple_a_found = True
                    triple_a_count += 1
                    i += 3
                    continue

            else:
                # increment triple_a_count
                triple_a_count += 1

            # if a found, set found to
        else:
            if triple_a_found:
                triple_a_found = False
            if not triple_b_found:
                if colors[i] == "B" and colors[i + 1] == "B" and colors[i + 2] == "B":
                    triple_b_found - True
                    triple_b_count += 1
                    i += 3
                    continue
            else:
                triple_b_count += 1

        i += 1
    return (triple_a_count, triple_b_count)


print(count_helper("AAAABBBB"))
