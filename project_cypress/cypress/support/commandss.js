// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add('verifyForm', (role,subtitle,buttonText,linkText)=>{
    cy.get(".container").should("contain",role);
    cy.get(".container").should("contain",subtitle);
    cy.get("#login").should("exist");
    cy.get("#password").should("exist");
    cy.get('button').should("exist").and('have.text',buttonText)
    cy.get('a').should("exist").and('have.text',linkText)
})

Cypress.Commands.add('registerToApp', (login,password,signUpLink,registerButton)=>{
    cy.get('a').should("have.text", signUpLink).click();
    cy.get("#login").type(login);
    cy.get("#password").type(password);
    cy.get('button').should("have.text",registerButton).click();
})

Cypress.Commands.add('loginToApp', (login,password,loginButton,logoutButton) =>{
    cy.xpath('//input[@name="login"]').type(login);
    cy.xpath('//input[@name="password"]').type(password);
    cy.get('button').should('have.text',loginButton).click();
    cy.wait(1000);

    cy.window().then($win =>{
        expect($win.localStorage.getItem('username')).to.eq(login);
        expect($win.localStorage.getItem('logged')).to.eq('1')
    })

    cy.get('.container').contains(login);
    cy.get('button').should('contain',logoutButton)
})

Cypress.Commands.add('logoutApp',(logoutButton) =>{
    cy.get('#logout').should('have.text',logoutButton).click();
})

