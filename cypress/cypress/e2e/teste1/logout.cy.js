describe('Login Test', () => {
  it('should log in successfully with valid credentials', () => {
    cy.clearLocalStorage()
    
    // Visitar a página de login
    cy.visit('https://sandbox.moodledemo.net/login/index.php')
      
    // Encontrar e preencher o campo de nome de usuário
    cy.get('#username').type('admin')
            
    // Encontrar e preencher o campo de senha
    cy.get('#password').type('sandbox')
      
    // Encontrar e clicar no botão de login
    cy.get('#loginbtn').click()
      
    // Verificar se o login foi bem-sucedido
    cy.url().should('include', '/')
    cy.get('.align-items-center > .mb-3')

    //LOGOUT
    cy.visit('https://sandbox.moodledemo.net/');
    cy.get('#user-menu-toggle').click()
    cy.contains('a', 'Log out').click({force: true})
  });
});


