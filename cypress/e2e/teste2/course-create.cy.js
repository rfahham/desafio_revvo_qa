describe('Login Test', () => {
  
  it('Create Course', () => {
    // cy.clearLocalStorage()
    
    // Visitar a página de login
    cy.visit('https://sandbox.moodledemo.net/login/index.php ');
      
    // Encontrar e preencher o campo de nome de usuário
    cy.get('#username').type('admin');
            
    // Encontrar e preencher o campo de senha
    cy.get('#password').type('sandbox');
      
    // Encontrar e clicar no botão de login
    cy.get('#loginbtn').click();

    cy.get('[data-key="mycourses"] > .nav-link').click();
  
    cy.contains('button', 'Create course').click();

    cy.get('#id_fullname').type('Curso de Cypress');

    cy.get('#id_shortname').type('Cypress');

    // cy.get('#id_startdate_day').type('1');

    // cy.get('#id_startdate_month').type('August');

    cy.get('#id_saveanddisplay').click();

    
  });
  
 });