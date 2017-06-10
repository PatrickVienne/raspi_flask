# hallo patrick, kannst du mir einen tip geben warum das folgende nicht funktioniert:
# coding: utf8

class Suspect(object):
    def __init__(self, name, gender, ethnos, hair, eye, face):
        self.name = name
        self.gender = gender
        self.ethnos = ethnos
        self.hair = hair
        self.eye = eye
        self.face = face

    def get_details(self):
        return self.name + " " + self.gender + " " + self.ethnos + " " + self.hair + " " + self.eye + " " + self.face

if __name__ == '__main__':

    eva = Suspect(name='eva', gender='female', ethnos='white', hair='blonde', eye='blue', face='oval')
    larisa = Suspect(name='larisa', gender='female', ethnos='white', hair='brown', eye='brown', face='oval')
    matej = Suspect(name='matej', gender='male', ethnos='white', hair='black', eye='blue', face='oval')
    miha = Suspect(name='miha', gender='female', ethnos='white', hair='brown', eye='green', face='square')

    suspects = [eva, larisa, matej, miha]

    for person in suspects:
        print person.get_details()

