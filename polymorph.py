#create 1 parent class with the only initializer function. All the other classes will inherit from here. 
class animal:
    def __init__(self, name,limbs):
        self.name = name
        self.limb_count = limbs
    print()

'''creating child classes of the class animal
each class is define with 4 functions; __str__(), move(), reproduction() and body_cover()
Initializer method in each class is inherited from the parent.'''
class mammal(animal):
    
    def __str__(self):
        return f'{self.name.upper()}; Limbs: {self.limb_count}; Body cover: Hair/Fur; Motion: Walk, swim or fly; Reproduction: Give birth.'
    
    def move(self):
        print()
        print(f"{self.name} moves by either of the following modes:")
        print("1. Walking, running or hopping.")
        print('2. Swimming if its Dolphin or Whale.')
        print("3. Flying if its a Bat.")
        print()

    def body_cover(self):
        print(f"The body of {self.name} is covered either in Hair or fur.")
        print()
    
    def reproduction(self):
        print(f"{self.name} gives birth to living young ones.")
        print()

class reptile(animal):
    def __str__(self):
        return f'{self.name.upper()}; Limbs: {self.limb_count}; Body cover: scales; Motion: crawl, swim or slither; Reproduction: lay eggs.'
    
    def move(self):
        print()
        print(f"{self.name} moves by either of the following modes:")
        print("1. Crawling for dry land reps like lizard.")
        print('2. Slithering if snake.')
        print("3. Swimming for water reptiles like croccodile.")
        print()

    def body_cover(self):
        print(f"The body of {self.name} is covered in scales.")
        print()
    
    def reproduction(self):
        print(f"{self.name} lays eggs.")
        print()



class bird(animal):
    def __str__(self):
        return f'{self.name.upper()}; Limbs: {self.limb_count}; Body cover: Feathers; Motion: Walk or fly; Reproduction: Lay eggs.'
    
    def move(self):
        print()
        print(f"{self.name} moves by either of the following modes:")
        print("1. Walking, or hopping for dry land birds like chicken.")
        print("3. Flying.")
        print()

    def body_cover(self):
        print(f"The body of {self.name} is covered in feathers.")
        print()
    
    def reproduction(self):
        print(f"{self.name} lays eggs.")
        print()


class insect(animal):
    def __str__(self):
        return f'{self.name.upper()}; Limbs: {self.limb_count}; Body cover: exoskeleton; Motion: crawl, hop or fly; Reproduction: Egs:Metamorphosis.'
    
    def move(self):
        print()
        print(f"{self.name} moves by either of the following modes:")
        print("1. Crawling or hopping.")
        print("3. Flying.")
        print()

    def body_cover(self):
        print(f"The body of {self.name} is covered in Hard exoskeleton.")
        print()
    
    def reproduction(self):
        print(f"{self.name} lays eggs then undergo metamorphosis most often.")
        print()

# defining the objects 
animal = mammal("dog",4)
print(animal)
animal.move()
animal.reproduction()
animal.body_cover()
print('**************************************************************************')

animal = insect("spider",8)
print(animal)
animal.move()
animal.reproduction()
animal.body_cover()
print('**************************************************************************')


animal = reptile("lizard",4)
print(animal)
animal.move()
animal.reproduction()
animal.body_cover()
print('**************************************************************************')


animal = bird("parrot",2)
print(animal)
animal.move()
animal.reproduction()
animal.body_cover()
print('**************************************************************************')
