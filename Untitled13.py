#!/usr/bin/env python
# coding: utf-8

# In[96]:


pip install bs4


# In[98]:


pip install lxml


# In[202]:


import bs4
import requests as ur
from bs4 import BeautifulSoup as Soup
my_url = 'https://www.avito.ma/fr/maarif/ordinateurs_portables/HP_SPECTRE_i5_tactile_39974176.htm'
uClient=ur.get(my_url)
soup=Soup(uClient.text,'lxml')
def Price(J):
    J1 =J.find('\'Price\'    : ')
    J=J[J1+12:]
    J2=J.find('\n')
    return J[3:J2-3]+' DH'
def Ville(J):
    J1 =J.find('\'City\'         : ')
    J=J[J1+16:]
    J2=J.find('\n')
    return J[3:J2-3]
def Date(J):
    J1 =J.find('\'PublishDate\'')
    J=J[J1+15:]
    J2=J.find('\n')
    return J[3:13]
def Heur(J):
    J1 =J.find('\'PublishDate\'')
    J=J[J1+15:]
    J2=J.find('\n')
    return J[14:J2-3]
def Catégorie(J):
    J1 =J.find('\'MainCategory\'')
    J=J[J1+15:]
    J2=J.find('\n')
    return J[4:J2-3]
def ID(J):
    J1 =J.find('\'ID\'')
    J=J[J1+14:]
    J2=J.find('\n')
    return J[4:J2-2]
def NameTitre(J):
    J1 =J.find('\"name\"')
    J=J[J1+5:]
    J2=J.find('\n')
    J3=J.find('\"name\"')
    J4=J[J3+5:]
    J5=J4.find('\n')
    return[J[4:J2-2],J4[4:J5-1]]
def Desc(J):
    J1 =J.find('\"description\"')
    J=J[J1+15:]
    J2=J.find('\n')
    return J[1:J2-2]
def numerau(J):
    J1 =J.find('telephone: ')
    J=J[J1+10:]
    J2=J.find('\n')
    return J[2:J2-2]
def Annonces(soup):
    x=soup.findAll('script',type="text/javascript")[12]
    J = str(x)
    x1=soup.findAll('script',type="application/ld+json")
    J0 = str(x1)
    x2=soup.findAll('script',type="text/javascript")
    J9=str(x2)
    nametitre=NameTitre(J0)
    Annonce=np.array([ID(J),nametitre[1],nametitre[0],Catégorie(J),Price(J),Ville(J),numerau(J9),Date(J),Heur(J),Desc(J0)])
    return Annonce
Annonces(soup)


# In[203]:


import pandas as pd 
import numpy as np
dataframe=pd.DataFrame(columns=['ID', 'Nom','Titre','Catégorie','Prix','Ville','Téléphone','Date','Heur','Description'])
my_url = 'https://www.avito.ma/fr/mers_sultan/locations_de_vacances/Studio_de_Prestige_38289212.htm'
uClient=ur.get(my_url)
soup=Soup(uClient.text,'lxml')
dataframe.loc[1] = Annonces(soup)
dataframe.to_excel(r'Avit.xlsx') 
my_url = 'https://www.avito.ma/fr/maarif/appareils_photo_cameras/Boitier_sony_fs5_4k_39964935.htm'
uClient=ur.get(my_url)
soup=Soup(uClient.text,'lxml')
dataframe.loc[2] = Annonces(soup)
dataframe.to_excel(r'Avit.xlsx') 


# In[205]:


url='https://www.avito.ma/fr/maroc/?o='
i=1
for j in range (1,11):
    url1='https://www.avito.ma/fr/maroc/?o='+str(j)
    uClient=ur.get(url1)
    soup=Soup(uClient.text,'lxml')
    x1=soup.findAll('a',tabindex="1")
    for link in x1:
        my_url = str(link['href'])
        uClient=ur.get(my_url)
        soup=Soup(uClient.text,'lxml')
        dataframe.loc[i] = Annonces(soup)
        i=i+1
    dataframe.to_excel(r'tD4ata.xlsx')    


# In[ ]:




