class MyClass:
    def __init__(self, value):
        self.value = value
    
    def my_method(self):
        print("Executing my_method with value:", self.value)
        
# Création d'une instance de MyClass
obj = MyClass(42)

# Accès à la méthode my_method à l'exécution à l'aide de la réflexion
method_name = "my_method"
if hasattr(obj, method_name):
    method = getattr(obj, method_name)
    method()  # Appel de la méthode
else:
    print("Method not found")

# Résultat:
# Executing my_method with value: 42
