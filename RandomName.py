import pandas as pd
import random

#initilize class
class RandomPerson():

  def __init__(self,gender=None, origin=None, capitalize=False):
    df = pd.read_csv('randPerson/names.csv', delimiter=';')


#Importing Dataframes for specifc Operations

  #Names
    self.first_names = df.loc[(df['type'] == 'firstname')]
    self.last_names = df.loc[(df['type'] == 'lastname')]

  #Mail
    self.mail_prefix = df.loc[(df['type'] == 'mail_prefix')]
    self.mail_connector = df.loc[(df['type'] == 'mail_connector')]

  #Phonenumber
    self.international_prefix = df.loc[(df['type'] == 'international_prefix')]
    self.national_prefix = df.loc[(df['type'] == 'national_prefix')]

  #Generating Fixed Values
    self.firstname_value = self.get_firstname(gender=gender, origin=origin, capitalize=capitalize)
    self.lastname_value = self.get_lastname(origin=origin, capitalize=capitalize)
    self.phonenumber_value = self.get_phonenumber(origin=origin)


  def get_firstname(self, gender=None, origin=None, capitalize=False):
    df_fnames = self.first_names

    if gender == "male" or gender == 'female' or gender is None: 
      if gender is None: 
        pass 
  
      else: 
        df_fnames = df_fnames.loc[(df_fnames['gender'] == gender)]
    
    else:
      raise Exception('Invalid value. Value: ' +str(gender)+' not valid for parameter gender')

    if origin == "german" or origin == "american" or origin is None:
      if origin is None: 
        pass 

      else: 
        df_fnames = df_fnames.loc[(df_fnames['origin'] == origin)]

    else:
      raise Exception('Invalid value. Value: ' +str(origin)+' not valid for parameter origin')
    
    fname = df_fnames['name'].sample().to_string(index=False)
    fname = fname.strip()

    if capitalize == True:
      return fname.capitalize()

    if capitalize == False: 
      return fname
    else:
      raise Exception('Invalid value. Value: ' +str(capitalize)+' not valid for parameter capitalize')
  
  
  def firstname(self):
    return self.firstname_value


  def get_lastname(self,origin=None, capitalize=False):
    df_lnames = self.last_names

    if origin == "german" or origin == "american" or origin is None:
      if origin is None:
        pass
      
      else:
        df_lnames = df_lnames.loc[(df_lnames['origin'] == origin)]

    else:
      raise Exception('Invalid value. Value: ' +str(origin)+' not valid for parameter origin')
    
    lname = df_lnames['name'].sample().to_string(index=False)
    lname = lname.strip()

    if capitalize == True:
      return lname.capitalize()
    
    if capitalize == False: 
      return lname
    else:
      raise Exception('Invalid value. Value: ' +str(capitalize)+' not valid for parameter capitalize')
  
  
  def lastname(self):
    return self.lastname_value


  def fullname(self):
    return self.firstname_value + " " + self.lastname_value


  def mail_specific_format(self, ending, connector):
    fname = self.firstname_value
    lname = self.lastname_value

    mail = fname + connector + lname + ending

    return mail 


  def mail(self):
    fname = self.firstname_value
    lname = self.lastname_value
    
    mail_connector = self.mail_connector['name'].sample().to_string(index=False)
    mail_connector = mail_connector.strip()

    mail_prefix = self.mail_prefix['name'].sample().to_string(index=False)
    mail_prefix = mail_prefix.strip()
    
    ran = random.randint(1,6)
    
    #p_lustig@yahoo.de
    if ran == 1:
      fname = [char for char in fname]
      fname = fname[0]
      email = fname + mail_connector + lname + mail_prefix 

      

    #peter.lustig1955@yahoo.de
    if ran == 2: 
      birth_year = random.randint(1940,2008)
      email = fname + mail_connector + lname + str(birth_year) + mail_prefix

      


    #peter.l1995@yahoo.de
    if ran == 3: 
      lname = [char for char in lname]
      lname = lname[0]
      birth_year = random.randint(1940,2008)
      email = fname + mail_connector + lname + str(birth_year) + mail_prefix

      

    #p.lustig15@yahoo.de
    if ran == 4:
      birth_year = random.randint(1,100)
      fname = [char for char in fname]
      fname = fname[0]
      email = fname + mail_connector + lname + str(birth_year) + mail_prefix 

      
    #peterlustig@yahoo.de
    if ran == 5:
      email = fname + lname + mail_prefix 


    #pelustig@yahoo.de
    if ran == 6: 
      fname = [char for char in fname]
      fname = fname[0:2]
      fname = "".join(fname)
      email = fname + lname + mail_prefix 
  
  
    return email.lower()



  def get_phonenumber(self, origin=None):
    df_international_prefix = self.international_prefix
    df_national_prefix = self.national_prefix

    if origin is None:
      origin = "german"

    if origin == "german" or origin == "american": 
      
        df_international_prefix = df_international_prefix.loc[(df_international_prefix['origin'] == origin)]
        df_national_prefix = df_national_prefix.loc[(df_national_prefix['origin'] == origin)]

    int_phoneNumber_prefix = df_international_prefix['name'].sample().to_string(index=False)
    int_phoneNumber_prefix = str(int_phoneNumber_prefix.strip())
  
    nat_phoneNumber_prefix = df_national_prefix['name'].sample().to_string(index=False)
    nat_phoneNumber_prefix = str(nat_phoneNumber_prefix.strip())



    if origin == "german":
      rand_lenght = random.randint(8,9)
  
    if origin == "american":
      rand_lenght = random.randint(7,7)

    if origin is None:
      raise Exception('Parameter origin needs to be provided in order to generate phone number')


    phone_number = str(generate_phonenumber(rand_lenght))

    phone_number = int_phoneNumber_prefix + nat_phoneNumber_prefix + phone_number
    
    return phone_number
    

  def phonenumber(self):
    return self.phonenumber_value

    


#Supporting Functions
def generate_phonenumber(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)
