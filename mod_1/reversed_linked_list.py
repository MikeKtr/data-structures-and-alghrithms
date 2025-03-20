def reverse(p):
    poprzedni,obecny = None,p
    while obecny is not None:
        temp=obecny.next
        obecny.next = poprzedni
        poprzedni,obecny = obecny,temp