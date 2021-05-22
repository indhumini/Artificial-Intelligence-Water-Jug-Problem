import jug
import sys

jv1 = int(input("Jug 1 capacity:"), 10)
jv2 = int(input("Jug 2 capacity:"), 10)


tv = int(input("Target Volume:"), 10)


smaller = jug.Jug(min(jv1, jv2), "Jug 1")
larger = jug.Jug(max(jv1, jv2), "Jug 2")


def makeMoveStoL(smaller, larger):

    if smaller.is_empty():
        smaller.fill()
        print("A -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True

    if larger.is_full():
        larger.dump()
        print("B -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True

    if not (smaller.is_empty()):
        smaller.transfer(larger)
        print("C -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True


found_it1 = (smaller.current_volume + larger.current_volume) == tv

step_countStoL = 0
step_countLtoS = 0
while not (found_it1):
    makeMoveStoL(smaller, larger)
    step_countStoL += 1
    found_it1 = (smaller.current_volume + larger.current_volume) == tv


print("found target volume in", step_countStoL, "steps")
