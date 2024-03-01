from abc import ABC, abstractmethod

class AddEmployee(ABC):
    @abstractmethod
    def add_employee(self, employee):
        pass

class RemoveEmployee(ABC):
    @abstractmethod
    def remove_employee(self, employee):
        pass

class PayrollCalculable(ABC):
    @abstractmethod
    def calculate_payroll(self):
        pass

class EmployeeManager(AddEmployee, RemoveEmployee, PayrollCalculable):
    pass

class PartTimeEmployeeManager(AddEmployee, PayrollCalculable):
    def add_employee(self, employee):
        # Logique spécifique pour ajouter un employé à temps partiel
        pass

    def calculate_payroll(self):
        # Logique pour calculer la paie des employés à temps partiel
        pass
