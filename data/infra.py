class Infra:
    def __init__(self, id,length,a_remplacer,nb_maison):
        self.id = id
        self.length = length
        self.statut = a_remplacer
        self.nb_maison = nb_maison 

    @staticmethod
    def infra_dif(self):
        return self.length / self.nb_maison
    
    def __radd__(self, other_object):
        return self.infra_dif + other_object
    
    def Istatut(self):
        self.statut = 'infra_intacte'
    
