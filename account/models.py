from django.db import models

# Create your models here.

class allworld(models.Model):
    image=models.ImageField()

    
    


class User(models.Model):
    f_name=models.CharField(max_length=40)
    l_name=models.CharField(max_length=40)
    p_number=models.CharField(max_length=11)
    email=models.EmailField()
    linkdir=models.URLField()
    instagram=models.URLField()
    facebook=models.URLField()
    image=models.ImageField(upload_to='image')
    all_world=models.ForeignKey(allworld,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.f_name


class repsentred(models.Model):
    link=models.URLField()
    name=models.CharField(max_length=40)
    p_numner=models.CharField(max_length=40)
    email=models.EmailField()

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    abount_user=models.TextField()
    image=models.ImageField(upload_to='user_image')
    awarsd=models.TextField()
    rapsentred_by=models.ForeignKey(repsentred,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)


class exbiations(models.Model):
    date=models.DateTimeField()
    describtions=models.TextField()
    profile=models.ForeignKey(profile,on_delete=models.CASCADE)

class categroy(models.Model):
    nema=models.CharField(max_length=40)
    allworld=models.ForeignKey(allworld,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nema

    
                         