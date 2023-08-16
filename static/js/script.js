
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


// ======================= burger menu ===================================
const burgerMenu = document.getElementById('burger');
const navItems = document.getElementById('navItems');
const headerLogo = document.getElementById('headerLogo');
burgerMenu.addEventListener('click', () =>{
  navItems.classList.toggle('active');
  headerLogo.classList.toggle('disable-logo');
});