"""

    Some of the options of the protocol specification

    LINE
    1-8

    PAGE
    A-Z     (remapped to 0-25)

    LEADING
    A/a = Immediate (Image will be immediately disappeared)
    B/b = Xopen (Image will be disappeared from center and extend to 4 side)
    C/c = Curtain UP (Image will be disappeared one line by one line from bottom to top).
    D/d = Curtain Down(Image will be disappeared one line by one Line from Top to Bottom
    E/e = Scroll Left (Image will be scrolled from Right to Left and disappeared )
    F/f = Scroll Right (Image will be scrolled from Right to Left and disappeared)
    G/g = Vopen (Image will be disappeared from center to top and Bottom one line by one line)
    H/h = Vclose(Image will be disappeared from Top and Bottom to Center one line by one line.)
    I/i = Scroll Up(Image will be scrolled from Bottom to Top and disappeared)
    J/j = Scroll Down (Image will be scrolled from Bottom to Top and disappeared)
    K/k = Hold (Screen will be kept)

"""

def get_message_cmd(
    message, 
    line = '1', 
    page = 0,
    leading = 'E',
    method = 'A',
    wait = 'C',
    lagging = 'E'):
    """ returns the command to send a message into a line of a page """
    return '<L%s><P%s><F%s><M%s><W%s><F%s>%s' % (
        line, 
        _num_to_code(page), 
        leading, 
        method, 
        wait, 
        lagging, 
        message
    )

def get_schedule_cmd(pages):
    """ returns the command to set the schedule (order) of the pages """
    # no support for start date / end date
    return '<TA>00010100009912302359' + _nums_to_codestr(pages)

def _num_to_code(n):
    # converts 0 -> A, 1 -> B
    # using 'A', 'B', 'C' ... for pages is uncomfortable
    return chr(ord('A') + n)

def _nums_to_codestr(numbers):
    return "".join(map(_num_to_code, numbers))

