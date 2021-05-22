

#define the jug class
class Jug:
    capacity = 0
    current_volume = 0
    name = 'new jug'

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        self.current_volume = 0

    def fill(self):
        self.current_volume = self.capacity

    def is_full(self):
        return self.current_volume == self.capacity

    def is_empty(self):
        return self.current_volume == 0

    def dump(self):
        self.current_volume = 0

    def has_target_volume(self, target_volume):
        return self.current_volume == target_volume

    def transfer(self, target_jug):

        target_volume = min(target_jug.capacity,
                            (target_jug.current_volume + self.current_volume))
        
        self_volume = max(0, target_jug.current_volume +
                       self.current_volume - target_jug.capacity)
        
        self.current_volume = self_volume
        target_jug.current_volume = target_volume

        return True

# define variables
jv1 = int(input("Jug 1 capacity:"), 10)
jv2 = int(input("Jug 2 capacity:"), 10)
tv = int(input("Target Volume:"), 10)


#define operators
print("----Operators------")
print("A = if the smaller jug is empty, fill it")
print("B = if the larger jug is full, empty it")
print("C = transfer the contents of the smaller jug to the larger")
print("D = if the larger jug is empty, fill it")
print("E = if the smaller jug is full, empty it")
print("F = transfer the contents of the larger jug to the smaller")

print("----------------------")


#define smaller and larger jug
smaller = Jug(min(jv1, jv2), "Jug 1")
larger = Jug(max(jv1, jv2), "Jug 2")



#if user fills the smaller jug first
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

#if user fills the larger jug first
def makeMoveLtoS(smaller, larger):

    if larger.is_empty():
        larger.fill()
        print("D -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True

    if smaller.is_full():
        smaller.dump()
        print("E -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True

    if not (larger.is_empty()):
        larger.transfer(smaller)
        print("C -> [", smaller.current_volume, ",", larger.current_volume, "]")
        return True



#define conditions
found_it1 = (smaller.current_volume + larger.current_volume) == tv
found_it2 = (larger.current_volume + smaller.current_volume) == tv

#define variables to identify steps
step_countStoL = 0
step_countLtoS = 0
while not (found_it1):
    makeMoveStoL(smaller, larger)
    step_countStoL += 1
    found_it1 = (smaller.current_volume + larger.current_volume) == tv

print("----------------------")

smaller.current_volume = 0
larger.current_volume = 0

while not (found_it2):
    makeMoveLtoS(smaller, larger)
    step_countLtoS += 1
    found_it2 = (larger.current_volume + smaller.current_volume) == tv


print("found target volume when filling smaller jug first in", step_countStoL, "steps")
print("found target volume when filling larger jug first in", step_countLtoS, "steps")