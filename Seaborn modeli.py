#!/usr/bin/env python
# coding: utf-8

# In[169]:


import seaborn as sns #seaborn kütüphanesi eklendi
import pandas as pd  #pandas kütüphanesi eklendi
tips = sns.load_dataset("tips")  #load_dataset() metodu ile seaborn kütüphanesinde bulunan hazır veri setlerinden tips verisi eklendi
df.head() #head() metodu ile ilk 5 satır görüntülendi


# In[170]:


df.isnull() #isnull() metodu ile verideki eksiklikler varsa tablolanır


# In[171]:


df.isnull().sum() #isnull().sum() metodu her değişkende kaç tane eksik veri olduğunu söyler


# In[172]:


df.info() #info() metodu veri setinin yapısını gösterir


# In[173]:


kat_df = df.select_dtypes(include = ["category"]) 
#Veri setindeki kategorik değişkenleri incelemek için kat_df değişkenine tanımladık
#select_dtypes ile category değişkenini almak istediğimizi belirttik


# In[174]:


print("SEX")  #Sınıfların isimleri yazıldı
print(kat_df.sex.unique()) #Bu satırı sınıfların içindeki kategorik değişkenlerin kaç sınıfa sahip olduklarına ve isimlerine bakmak için yazdık
print()
print("SMOKER")
print(kat_df.smoker.unique()) 
print()
print("DAY")
print(kat_df.day.unique())
print()
print("TIME")
print(kat_df.time.unique())
print()


# In[175]:


tips.describe().T #describe() metodu tips veri setindeki sayısal sütunların istatistiksel bilgilerini verir, T ise bu sütunların yan yana olmasını sağlar


# In[176]:


sns.countplot(x="sex",data=df) #Cinsiyet kategorisindeki kadın-erkek sayısını gösterir


# In[177]:


sns.countplot(x="smoker",data=df) #Sigara kategorisindeki içen ve içmeyenlerin sayısını gösterir


# In[178]:


sns.countplot(x="day",data=df) #Gün kategorisindeki günlerin sayısını gösterir


# In[179]:


sns.countplot(x="time",data=df); #Zaman kategorisindeki öğle ve akşam yemeği sayılarını gösterir


# In[180]:


sns.barplot(x = "day", y = "total_bill",hue = "sex",data = df) 
#Toplam faturanın cinsiyete göre günlere dağılımını gösteren grafik oluşturuldu
#barplot metodu bar grafiği oluşturmak için kullanıldı
#hue parametresi grafiğe bir boyut daha eklemek için kullanıldı
#data=df verilerin veri setinden gelmesini sağladı


# In[181]:


sns.barplot(x = "smoker", y = "total_bill",hue = "size",data = df) 
#Sigara içmeye göre kişilerin toplam faturalarını gösterir


# In[182]:


sns.barplot(x = "day", y = "tip",hue = "time",data = df) 
#Günün hangi zamanlarında ne kadar bahşiş olduğunu gösterir


# In[183]:


sns.barplot(x = "size", y = "tip",hue = "sex",data = df) 
#Cinsiyete göre kişilerin bahşiş sayılarını gösterir


# In[184]:


sns.barplot(x = "smoker", y = "size",hue = "sex",data = df) 
#Cinsiyete göre sigara içen ve içmeyenleri gösterir


# In[185]:


sns.barplot(x = "day", y = "tip", hue="size",data = df) 
#Günlere göre kişilerin bahşiş sayısını gösterir

