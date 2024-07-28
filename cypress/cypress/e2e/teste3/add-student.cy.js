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

      // Selecionar o Course
      cy.get('.last > .info > .coursename > .aalink').click();
      
      // Redirecionamento
      cy.visit('https://sandbox.moodledemo.net/course/view.php?id=3')
      
      // Clicar em Participants
      cy.get('[data-key="participants"] > .nav-link').click();

      cy.visit('https://sandbox.moodledemo.net/user/index.php?id=3')
      
      // Enrol Users
      cy.get('#enrolusersbutton-1 > div > .btn').click();

      // Estou com dificuldade neste ponto:

      // Selecionar o estudante
      cy.contains('input.form-control', 'Search').type('Sam Student');

      // Timed out retrying after 4000ms: Expected to find content: 'Search' within the selector: 'input.form-control' but never did.
        
    });
  
  });
  