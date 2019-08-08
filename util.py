def as_str(state):
    return "%s%s%s" % (state[0], state[1], state[2])


def as_array(state):
    return [int(state[0]), int(state[1]), int(state[2])]