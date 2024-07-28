describe('Login Test', () => {
  
    it('Insert Student', () => {
      // cy.clearLocalStorage()
      
      // Visitar a página de login
      cy.visit('https://sandbox.moodledemo.net/login/index.php ');
        
      // Encontrar e preencher o campo de nome de usuário
      cy.get('#username').type('admin');
              
      // Encontrar e preencher o campo de senha
      cy.get('#password').type('sandbox');
        
      // Encontrar e clicar no botão de login
      cy.get('#loginbtn').click();

      // Não tem como adicionar um Student se não selecionar Available courses anteriormente
        
    });
  
  });