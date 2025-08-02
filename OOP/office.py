class Office:
    employeesNum = 0  # Class variable for total employees across all offices
    
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees else []
    
    @classmethod
    def change_emps_num(cls, num):
        """Class method to modify the number of employees in all offices"""
        cls.employeesNum = num
        print(f"Total employees across all offices set to: {cls.employeesNum}")
    
    def get_all_employees(self):
        """Return a list of the current employees"""
        return self.employees
    
    def get_employee(self, empId):
        """Return the employee of given id"""
        for employee in self.employees:
            if employee.id == empId:
                return employee
        return None
    
    def hire(self, employee):
        """Hire the given employee"""
        if employee not in self.employees:
            self.employees.append(employee)
            Office.employeesNum += 1
            print(f"Employee {employee.name} (ID: {employee.id}) hired at {self.name}")
        else:
            print(f"Employee {employee.name} is already employed at {self.name}")
    
    def fire(self, empId):
        """Fire employee with the given id"""
        employee = self.get_employee(empId)
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1
            print(f"Employee {employee.name} (ID: {empId}) fired from {self.name}")
        else:
            print(f"Employee with ID {empId} not found in {self.name}")
    
    def deduct(self, empId, deduction):
        """Deduct money from salary of employee"""
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction
            print(f"Deducted {deduction}L.E from {employee.name}'s salary. New salary: {employee.salary}L.E")
        else:
            print(f"Employee with ID {empId} not found in {self.name}")
    
    def reward(self, empId, reward):
        """Add money to salary of employee"""
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward
            print(f"Added {reward}L.E to {employee.name}'s salary. New salary: {employee.salary}L.E")
        else:
            print(f"Employee with ID {empId} not found in {self.name}")
    
    def check_lateness(self, empId, moveHour):
        """Check if employee is late or not and deduct/reward accordingly"""
        employee = self.get_employee(empId)
        if not employee:
            print(f"Employee with ID {empId} not found in {self.name}")
            return
        
        # Assume target hour is 9 AM
        targetHour = 9
        is_late = Office.calculate_lateness(targetHour, moveHour, employee.distanceToWork, 
                                          employee.car.velocity if employee.car else 0)
        
        if is_late:
            self.deduct(empId, 10)
            print(f"{employee.name} is late! Deducted 10L.E from salary.")
        else:
            self.reward(empId, 10)
            print(f"{employee.name} is on time! Rewarded 10L.E to salary.")
    
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        """Static method to calculate if employee is late or not"""
        if velocity <= 0:
            return True  # Can't move, definitely late
        
        # Calculate travel time in hours
        travel_time = distance / velocity
        
        # Calculate arrival time
        arrival_time = moveHour + travel_time
        
        # Check if late (arrival after target hour)
        return arrival_time > targetHour
    
    def __str__(self):
        return f"Office: {self.name}, Employees: {len(self.employees)}, Total Office Employees: {Office.employeesNum}" 