import zlib
import math

def user_ask():
    string_user = input("Pouvez-vous me donner vos préférence en matières de cinéma ") 
    string_user = string_user.encode('latin-1')
    zdata_user = len(zlib.compress(string_user)) #Compressing user ask
    print("Data user compresser",zdata_user)

    #Define our data and storage in array
    film1 = "La Zone d'intérêt est un drame de guerre américano-britannico-polonais. Le commandant d'Auschwitz, Rudolf Höss, et sa femme Hedwig s'efforcent de construire une vie de rêve pour leur famille dans une maison avec jardin à côté du camp. Historique, Drame".encode('latin-1')
    film2 = "Elly Conway est l'auteure solitaire d'une série de romans d'espionnage à succès. Sa vie tranquille est bouleversée lorsque les intrigues de ses livres commencent à ressembler étrangement aux opérations secrètes d'une véritable organisation d'espions.Action, Espionnage, Thriller ".encode('latin-1')
    film3 = "Jeune fille de dix-sept ans à l'esprit vif, Asha vit dans un royaume fantastique où tous les souhaits peuvent littéralement s'exaucer. Dans un moment de desespoir, elle adresse unn voeu aux étoiles auquel va répondre une force cosmique : une petite boule d'énergie infinie prénommée Star. Aventure, Animation, Famille".encode('latin-1')
    film4 = "Jeune fille".encode('latin-1')

    data_array = [film1,film2,film3,film4]

    #Compressing data movie
    zdata_array = [None] * len(data_array)
    for i in range(len(data_array)):
        zdata_array[i] = len(zlib.compress(data_array[i]))

    for i in range(len(data_array)):
        print("Voici la compression du film",i+1,"=",zdata_array[i])
    
    #Co-compressing
    zijdata_array = [None] * len(data_array) #Array qui stock compression entre user ask et les x films
    for i in range(len(zijdata_array)):
        zijdata_array[i] = len(zlib.compress(data_array[i] + string_user))
    for i in range(len(data_array)):
        print("Voici la compression entre les data_user et les films",i+1,"=",zijdata_array[i])

        
    #NCD part : 
    ncd_array = [None] * len(data_array)
    for i in range(len(data_array)):
        ncd_array[i] = (zijdata_array[i]-min(zdata_user,zdata_array[i]))/max(zdata_user,zdata_array[i])
    for i in range(len(data_array)):
        print("Voici la valeur ncd entre les data_user et le films",i+1,"=",ncd_array[i])
    

     #Final : Top3 des films :
    ncd_array.sort()
    print("Le top 3 des film à voir sont :",ncd_array[0],ncd_array[1],ncd_array[2])
    
    
  
    
    
user_ask()
































 

                     
                         

