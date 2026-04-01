#Online Shopping System (Multi level inheritance)
'''
An e-commerce company organizes products using multiple levels. Create
classes Product → ElectronicProduct → MobilePhone using multilevel
inheritance and display product details.

'''
class Product:
    def __init__(self,product_name,product_price,model_name,discount):
        self.product_name = product_name
        self.product_price = product_price
        self.model_name = model_name
        self.discount = discount
        print("This is product cart")
        
class Electronic(Product):
    def display_product(self):
        print("Product Name: ",self.product_name)
        print("Product price: ",self.product_price)
        
class Mobile(Electronic):
   
    def display_mobile(self):
        print("Model Name: ",self.model_name)
        print("Discount: ",self.discount)

    def display_all(self):
        self.display_product()
        self.display_mobile()
    

#defining object
phone = Mobile("Vivo V40e",23000,"Android",10)

#displaying results
print("Product Details: \n")
phone.display_all()

    
