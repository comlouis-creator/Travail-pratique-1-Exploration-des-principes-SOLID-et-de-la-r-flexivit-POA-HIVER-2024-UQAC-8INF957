from abc import ABC, abstractmethod

class EmployeeManager(ABC):
    @abstractmethod
    def add_employee(self, employee):
        pass

    @abstractmethod
    def remove_employee(self, employee):
        pass

    @abstractmethod
    def calculate_payroll(self):
        pass

class PartTimeEmployeeManager(EmployeeManager):
    def add_employee(self, employee):
        # Logique spécifique pour ajouter un employé à temps partiel
        pass

    def remove_employee(self, employee):
        # Logique spécifique pour supprimer un employé à temps partiel
        pass

    def calculate_payroll(self):
        # Logique pour calculer la paie des employés à temps partiel
        pass
