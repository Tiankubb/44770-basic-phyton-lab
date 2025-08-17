// Function to validate form before submission
function validateForm() {
    // Get form inputs
    const fullname = document.querySelector('input[name="fullname"]').value.trim();
    const province = document.querySelector('select[name="province"]').value;
    const address = document.querySelector('textarea[name="address"]').value.trim();
    const iphone = document.querySelectorAll('input[name="iphone[]"]:checked').length;
    const color = document.querySelectorAll('input[name="color[]"]:checked').length;
    const number = document.querySelector('select[name="number"]').value;

    // Check if any required field is empty
    if (!fullname || !province || !address || iphone === 0 || color === 0) {
        // Show error message on page
        const errorDiv = document.createElement('div');
        errorDiv.style.color = 'red';
        errorDiv.style.margin = '10px 0';
        errorDiv.textContent = 'กรุณากรอกข้อมูลให้ครบทุกช่อง';
        
        // Remove previous error if exists
        const existingError = document.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }
        
        errorDiv.className = 'error-message';
        document.querySelector('form').prepend(errorDiv);
        
        // Log error to console
        console.error('ไม่พบข้อมูลหรือข้อมูลไม่ครบ');
        
        return false;
    }
    
    return true;
}

// Function to handle form submission
function handleSubmit(event, paymentType) {
    event.preventDefault();
    
    // Validate form first
    if (!validateForm()) {
        return;
    }
    
    // Show alert to user
    alert('คุณกดส่งข้อมูลแล้ว');
    
    // Submit the form
    const form = event.target.form || event.target.closest('form');
    form.submit();
    
    // This alert won't actually show because page will redirect
    // It's here just to demonstrate the requirement
    // In a real scenario, you might want to use AJAX to submit the form
    // or show this on the PHP page instead
    console.log('ข้อมูลถูกส่งมาหน้า php แล้ว');
}

// Add event listeners to buttons
document.addEventListener('DOMContentLoaded', function() {
    const submitButtons = document.querySelectorAll('input[type="submit"]');
    
    submitButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            handleSubmit(event, this.value);
        });
    });
});