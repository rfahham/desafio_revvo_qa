describe('Log out Test', () => {
  
  it('should log in', () => {
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
    cy.get('div h5').should('have.text', 'Welcome!')
    
    cy.visit('https://sandbox.moodledemo.net/#')
    cy.get('.userinitials').click()
    cy.contains('div a.dropdown-item', 'Log out').click({force: true})

  });

});

