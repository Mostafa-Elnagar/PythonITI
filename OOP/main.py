from person import Person
from car import Car
from employee import Employee
from office import Office

def main():
    print("=== OOP System Demo ===\n")
    
    print("1. Testing Person Class:")
    print("-" * 30)
    person1 = Person("Ahmed", 1000, "happy", 80)
    print(person1)
    
    person1.sleep(9)  # Should be lazy
    print(person1.mood)
    
    person1.eat(3)  # Should be 100% health
    
    person1.buy(3)  # Should cost 30L.E
    print(person1)
    print()
    
    # 2. Test Car Class
    print("2. Testing Car Class:")
    print("-" * 30)
    car1 = Car("Toyota", 80, 120)
    print(car1)
    
    car1.velocity = 250  
    car1.fuelRate = 150  
    print(car1)
    
    car1.run(60, 100)  # Should complete journey
    print(car1)
    
    car1.fuelRate = 5
    car1.run(80, 100)  # Should run out of fuel
    print()
    
    print("3. Testing Employee Class:")
    print("-" * 30)
    car2 = Car("BMW", 90, 150)
    emp1 = Employee(1, "Sarah", 2000, "happy", 90, car2, "sarah@company.com", 5000, 50)
    print(emp1)
    
    emp1.work(10)  # Should be tired
    
    emp1.drive(30)  # Test driving
    emp1.refuel(20)  # Test refueling
    emp1.send_mail("boss@company.com", "Report", "Monthly report attached")
    print()
    
    # 4. Test Office Class
    print("4. Testing Office Class:")
    print("-" * 30)
    office1 = Office("IT Department")
    print(office1)
    
    # Create more employees
    car3 = Car("Honda", 70, 100)
    emp2 = Employee(2, "Mohammed", 1500, "happy", 85, car3, "mohammed@company.com", 4000, 30)
    
    car4 = Car("Ford", 60, 80)
    emp3 = Employee(3, "Fatima", 1800, "tired", 75, car4, "fatima@company.com", 4500, 40)
    
    # Hire employees
    office1.hire(emp1)
    office1.hire(emp2)
    office1.hire(emp3)
    print(office1)
    
    # Test office methods
    print(f"All employees: {len(office1.get_all_employees())}")
    found_emp = office1.get_employee(2)
    if found_emp:
        print(f"Found employee: {found_emp.name}")
    
    # Test salary operations
    office1.reward(1, 500)
    office1.deduct(2, 200)
    
    # Test lateness checking
    print("\nTesting lateness:")
    office1.check_lateness(1, 8)  # Should be on time
    office1.check_lateness(2, 8.5)  # Might be late depending on distance/velocity
    office1.check_lateness(3, 7)  # Should be on time
    
    # Test static method
    print("\nTesting static calculate_lateness method:")
    is_late = Office.calculate_lateness(9, 8, 50, 60)
    print(f"Employee leaving at 8 AM, 50km distance, 60 km/h speed: {'Late' if is_late else 'On time'}")
    
    is_late = Office.calculate_lateness(9, 8.5, 50, 30)
    print(f"Employee leaving at 8:30 AM, 50km distance, 30 km/h speed: {'Late' if is_late else 'On time'}")
    
    # Test class method
    print("\nTesting class method:")
    Office.change_emps_num(10)
    print(f"Total employees across all offices: {Office.employeesNum}")
    
    # Test firing
    office1.fire(2)
    print(office1)
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main() 