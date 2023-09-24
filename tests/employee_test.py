from pycon2023 import Employee


def test_intern_employee():
    id_intern = "000"
    alice = Employee(id_intern, "Alice", None)

    assert alice.is_intern()

def test_hired_employee():
    tom = Employee("355", "Tom", 100_000.00)
    
    assert not tom.is_intern()