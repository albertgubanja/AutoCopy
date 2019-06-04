from os import walk, path, system
import os
import shutil

def copyfichier():
    dircopy = input('Saisissez le chemin vers le dossier de destination :') # dossier destinateur

    if not path.exists(dircopy):
        os.makedirs(dircopy) # creation du dossier de destinantion
    filesearch = input('Saisissez le nom du fichier à copier :') # fichier a chercher
    filesearch=filesearch.upper()
    listflash = ['C:\\','D:\\','E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\' ] # liste des flash

    partitions_hdd_pc=int(input('Précisez le nombre des partition(s) existante(s) sur votre PC: '))
    p=0
    while p<partitions_hdd_pc:
        q=input("Tapez la lattre de la partion {0} :".format(p))
        q=q.upper()
        q=q+':\\'
        if q in listflash:
            listflash.remove(q)
        p +=1
                

    #def copy(filedepart, pathdest):
        
        # formatage de la commande dos pour la copie
        
        #command = "copy " + filedepart + " " + pathdest # ommand
        #system(command) # execution de la commande

    while True:
        for flash in listflash:
            for response in walk(flash): # parcout dossier et sous-dossiers du flash
                chemindossier = response[0] # le chemin vers le dossier actuel
                listedossiers = response[1] # la liste des dOssiers
                listefichiers = response[2] # la liste des fichiers

                for x in listefichiers:  # affectation du nom de chaque fichier trouvé dans le flash à x pour le test
                    d=x.upper()
                    e=len(d)

                    #FILTRE
                    #if e<len(filesearch): #test de longueur de chaque fichier par rapport au fichier recherché
                        #continue
                    if d[0]!=filesearch[0]:#
                        continue

                    else:
                        a=""
                        for j in range(len(filesearch)):# Recherche du fichier
                            if d[j]!=filesearch[j]:
                                continue
                            else:
                                a=a+x[j]
                        if a==filesearch:
                            fichieracopier= path.join(chemindossier, x) #Création du chemier du chier à copier

                            #VERIFICATION SI LE FICHIER EXISTE DEJA (On ne copiera que si le fichier n'a pas encore été copié)
                            for response2 in walk(dircopy):
                                fichiersexistants=response2[2]
                                if x in fichiersexistants: 
                                    continue
                                else:
                        
                                    shutil.copy2(fichieracopier, dircopy) # copie dans vers le dossier de l'etudiant
                                    print("Copie fichier de   " + fichieracopier + " vers  " + dircopy)
                                    print("Fichier copié avec succès")
                                    
                    

