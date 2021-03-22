from cassandra.cluster import Cluster
from datetime import datetime


class DataAccess :

    @classmethod
    def connexion(cls):
        cls.cluster = Cluster(['127.0.0.1'])
        cls.session = cls.cluster.connect('resto')

    @classmethod
    def infos_resto(cls, id_resto):
        id_resto = str(id_resto)
        objet = cls.session.execute(f'SELECT * FROM restaurant WHERE id = {id_resto}')
        liste_cles = ["id", "borough", "buildingnum", "cuisinetype", "name", "phone", "street", "zipcode"]
        dict_infos = {}
        for ligne in objet:
            for index in range(8):
                dict_infos[liste_cles[index]] = ligne[index]
        return dict_infos

    @classmethod
    def liste_cuisine(cls, cuisine):
        objet = cls.session.execute(f"SELECT name FROM restaurant WHERE cuisinetype = '{cuisine}'")
        liste_cuisine = []
        for ligne in objet:
            for nom in ligne:
                liste_cuisine.append(nom)
        return liste_cuisine

    @classmethod
    def compte_inspections(cls, id_resto):
        objet = cls.session.execute(f'SELECT inspectiondate FROM inspection WHERE idrestaurant = {id_resto}')
        liste_inspections = []
        for ligne in objet:
            for inspectiondate in ligne:
                inspectiondate = str(inspectiondate)
                liste_inspections.append(inspectiondate)
        return liste_inspections

    @classmethod
    def premiers_restos(cls, grade):
        objet = cls.session.execute(f"SELECT idrestaurant FROM inspection WHERE grade = '{grade}'")
        liste_id = []
        liste_restos = []
        counter = 0
        for ligne in objet:
            if counter <= 10:
                for id_resto in ligne:
                    if id_resto not in liste_id:
                        liste_id.append(id_resto)
                        counter += 1
        
        for id_resto in liste_id:
            objet = cls.session.execute(f"SELECT name FROM restaurant WHERE id = {id_resto}")
            for ligne in objet:
                for nom in ligne:
                    liste_restos.append(nom)
        return liste_restos




DataAccess.connexion()
#print(DataAccess.infos_resto(50041578))
#print(DataAccess.liste_cuisine("American"))
#print(DataAccess.compte_inspection(41553467))
#print(DataAccess.premiers_restos("A"))