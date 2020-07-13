from django.db import models
import re													
import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')							
							
class UserManager(models.Manager):												
    def validator(self, postData):												
        errors = {}																										
        if 'id' not in postData:  #Creating. if id not exists, that means we creating user
            # NAME VALIDATION 	
            if len(postData['first_name']) < 2:											
                errors['first_name'] = 'First name should be atleast 2 characters long.'	
            if not postData['first_name'].isalpha() and postData['first_name'] != '':
                errors['first_name'] = 'First name must containt only letters.'
            if len(postData['last_name']) < 2:										
                errors['last_name'] = 'Last name should be atleast 2 characters long'
            if not postData['last_name'].isalpha() and postData['first_name'] != '':
                errors['last_name'] = 'Last name must containt only letters.'
            # DATE VALIDATION
            # if - checks if birthday field is empty	
            # else - checks if user older then 13 years:
            if len(postData['birth_date']) < 1:	                							
                errors['birth_date'] = 'Birth date required.'
            else:                                               
                today = datetime.date.today()
                todays_year = today.year
                birthday = postData['birth_date'] 
                x = birthday[0] + birthday[1] + birthday[2] + birthday[3]
                birthday = int(x)
                age = todays_year - birthday
                if age < 13:										
                    errors['birth_date'] = 'User must be older then 13 years.'	
            # EMAIL VALIDATION
            if len(postData['email']) < 1:
                errors['email'] = "Email cannot be blank."
            if not EMAIL_REGEX.match(postData['email']): 
                errors['email'] = "Email is not valid"
            result =  self.filter(email = postData['email'])
            if len(result) > 0:
                errors['email'] = "Email is already registered."
            # PASSWORD VALIDATION
            if len(postData['password']) < 3:
                errors['password'] = 'Password required, should be atleast 8 characters long.'
            # Confirmation match the password: 
            if postData['password'] != postData['confirm_password']:
                errors['password'] = "Confirmation didn't match the password"
            return errors
        else:														
            # Editing. if the email they are trying to change this user's email to already exists BUT the email is not the original email of that user					
            if self.filter(email = postData['email'] and Show.objects.get(id=postData['id']).email != postData['email']):	
                errors['email'] = 'Email allready exists.'	

class User(models.Model):
    first_name = models.CharField(max_length = 255)										
    last_name = models.CharField(max_length = 255)										
    birth_date = models.DateTimeField()											
    email = models.TextField()	
    password = models.TextField()								
    created_at = models.DateTimeField(auto_now_add = True)  								
    updated_at = models.DateTimeField(auto_now = True)									
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
