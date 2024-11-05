from django.db import models

# Create your models here.
class books_manage(models.Model):
    bookName = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    status = models.CharField(max_length=80)


    def __str__(self):
        return self.author
    
 
class patron_manage(models.Model):
    author =models.ForeignKey(books_manage,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    details=models.IntegerField()
    card_no=models.IntegerField()
    due_date=models.DateTimeField(auto_now_add= True )


    def str(self) -> str:
        return self.name
    
class book_borrow(models.Model):
    author=models.ForeignKey(books_manage,on_delete=models.CASCADE)
    name=models.ForeignKey(patron_manage,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(auto_now_add=True)
    retun_date=models.DateTimeField()

    
    def str(self) -> str:
        return self.borrow_date
