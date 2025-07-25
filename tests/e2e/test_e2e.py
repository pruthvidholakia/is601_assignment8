# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_message(page, fastapi_server):
    """
    Test that the homepage displays "I am calculator, how can I assist you".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<p>`) correctly displays the text "I am calculator, how can I assist you". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <p> tag is exactly "I am calculator, how can I assist you".
    # If the text does not match, the test will fail.
    assert page.inner_text('p') == 'I am calculator, how can I assist you'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    This test simulates a user performing an addition operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Add" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 15'

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subract functionality of the calculator.

    This test simulates a user performing an minus operation using the calculator
    on the frontend. It fills in two numbers, clicks the "subtract" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '5'.
    page.fill('#a', '5')
    
    # Fill in the second number input field (with id 'b') with the value '3'.
    page.fill('#b', '3')
    
    # Click the button that has the exact text "Subtract". This triggers the subtract operation.
    page.click('button:text("subtract")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 2".
    # This verifies that the subtract operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 2'
    
@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the subract functionality of the calculator.

    This test simulates a user performing an minus operation using the calculator
    on the frontend. It fills in two numbers, clicks the "multiply" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '5'.
    page.fill('#a', '5')
    
    # Fill in the second number input field (with id 'b') with the value '3'.
    page.fill('#b', '3')
    
    # Click the button that has the exact text "multiply". This triggers the multiply operation.
    page.click('button:text("multiply")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the multiply operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 15'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    This test simulates a user attempting to divide a number by zero using the calculator.
    It fills in the numbers, clicks the "Divide" button, and verifies that the appropriate
    error message is displayed. This ensures that the application correctly handles invalid
    operations and provides meaningful feedback to the user.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '0', attempting to divide by zero.
    page.fill('#b', '0')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Error: Cannot divide by zero!". This verifies that the application handles division by zero
    # gracefully and displays the correct error message to the user.
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'
    
@pytest.mark.e2e
def test_calculator_power(page, fastapi_server):
    """
    Test the power functionality of the calculator.

    This test simulates a user raising a number to a given power using the
    calculator. It fills in the numbers, clicks the "power" button, and verifies
    that the correct result is displayed.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')

    # Fill in the first number input field (with id 'a') with the value '2'.
    page.fill('#a', '2')

    # Fill in the second number input field (with id 'b') with the value '3'.
    page.fill('#b', '3')

    # Click the button that has the exact text "power". This triggers the power operation.
    page.click('button:text("power")')

    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Calculation Result: 8". This verifies that the power operation was performed correctly
    # and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 8'    
