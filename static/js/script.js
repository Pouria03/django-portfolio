
// ======================= portfolio modal ===================================
// Get all elements with the class name "portfolio-card"
const portfolioCards = document.querySelectorAll('.portfolio-card');

// Get the portfolio modal element
const portfolioModal = document.querySelector('.portfolio-modal');

// Get the close button element inside the portfolio modal
const closeModalBtn = portfolioModal.querySelector('.close-modal-btn');

// Function to handle the portfolio card click
function handlePortfolioCardClick() {
  // Get all elements with the class name "section"
  const sections = document.querySelectorAll('.section');

  // Change the opacity of each section to 0.2
  sections.forEach(section => {
    section.style.opacity = 0.2;
  });

  // Display the portfolio modal
  portfolioModal.style.display = 'flex';
}

// Function to handle the close button click
function handleCloseModalClick() {
  // Reset the opacity of sections
  const sections = document.querySelectorAll('.section');
  sections.forEach(section => {
    section.style.opacity = 1;
  });

  // Hide the portfolio modal
  portfolioModal.style.display = 'none';
}

// Add click event listeners
portfolioCards.forEach(portfolioCard => {
  portfolioCard.addEventListener('click', handlePortfolioCardClick);
});

closeModalBtn.addEventListener('click', handleCloseModalClick);


// ======================= burger menu =========================================================
const burgerMenu = document.getElementById('burger');
const navItems = document.getElementById('navItems');
const headerLogo = document.getElementById('headerLogo');
burgerMenu.addEventListener('click', () =>{
  navItems.classList.toggle('active');
  headerLogo.classList.toggle('disable-logo');
});



// ======================== jquery for getting data from contact form ==========================
$(document).ready(function() {
    $('.btn').click(function(event) {
        event.preventDefault(); // Prevent the default form submission

        var phone = $('input[name="phone"]').val();
        var email = $('input[name="email"]').val();
        var name = $('input[name="name"]').val();
        var content = $('textarea[name="content"]').val();

        // Validate email format
        if (!isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate phone number format
        if (!isValidPhoneNumber(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }

        // Create the data object to send in the POST request
        var formData = {
            'phone': phone,
            'email': email,
            'name': name,
            'content': content,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val() // Include CSRF token
        };

        // Send the POST request
        $.ajax({
            type: 'POST',
            url: '/send_message/', // Update with the correct URL
            data: formData,
            success: function(response) {
                // Handle the success response here (e.g., show a success message)
                alert('your message was sent successfully');
            },
            error: function(xhr, textStatus, errorThrown) {
                // Handle the error here (e.g., display an error message)
                alert('invalid data, try again later');
            }
        });
    });
});

// Email format validation function
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Phone number format validation function
function isValidPhoneNumber(phone) {
    var phoneRegex = /^09([0-9][0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$/; // Change this regex pattern based on your requirements
    return phoneRegex.test(phone);
}
