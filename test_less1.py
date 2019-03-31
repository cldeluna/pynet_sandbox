import less1
import re

def test_print_header():
    assert "Testing123" in less1.print_header("Testing123")
    assert "Lesson Separator" in less1.print_header("Lesson Separator")


# def test_enter_ip():
#     # Exercise 1
#     assert re.match(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", less1.enter_ip()) == True

def test_validate_ip():
    assert less1.validate_ip('1.2.3.4') == True
    assert less1.validate_ip('255.2556.255a.2557') != True
