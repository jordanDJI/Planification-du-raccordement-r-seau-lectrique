from infra import Infra

class Batiment:
    def __init__(self,id,list_infrac):
        self.id=id
        self.list_infrac=list_infrac

    
    def bat_dif(self):
        in_df_bt #difficulter des differentes portion d'infraction par batiment
        for infrac in self.list_infrac:
            in_df_bt=infrac.infra_dif()
            self.list_infrac[infrac]= in_df_bt
        return sum(self.list_infrac)


    
    def __lt__(self, other_object):
        if type(other_object) != Batiment:
            raise Exception("ne peut comparer que les batiments")
        else:
             return self.bat_dif() < other_object.bat_dif()
        
    