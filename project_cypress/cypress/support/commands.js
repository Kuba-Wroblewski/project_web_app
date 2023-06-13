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
import 'cypress-file-upload';
require('cypress-downloadfile/lib/downloadFileCommand')


Cypress.Commands.add('clickButton', (buttonConatactUs)=>{
    cy.get('#contact-link > a').should("exist").and
    ('have.text',buttonConatactUs).click();
})

Cypress.Commands.add('contacUs', (selectChoose)=>{
    cy.get('#id_contact').select(selectChoose).should('have.value','2');
})

Cypress.Commands.add('enterEmail', (email)=>{
    cy.get('#email').type(email).and('exist');
})

Cypress.Commands.add('enterOrder', (order)=>{
    cy.get('#id_order').type(order).and('exist');
})

Cypress.Commands.add('message', (messageToService)=>{
    cy.get('#message').type(messageToService).and('exist');
})

Cypress.Commands.add('uploadFile', (randomFile,fileName)=>{
    cy.downloadFile(randomFile,'cypress/fixtures','randomImage.jpg');
    cy.get('#uniform-fileUpload').click().and('exist');
    cy.get('#fileUpload').attachFile(fileName).wait(1000);
})

 // pass when don't have a alert
Cypress.Commands.add('sendSuccessfully', (submitButton,alertSuccessfully)=>{
    cy.get('#submitMessage').should('have.text',submitButton).click();
    cy.xpath('//*[@id="center_column"]/p/text()').should('have.text',alertSuccessfully);
    // cy.xpath('//*[@id="center_column"]/div/ol/li/text()').should('have.text',alertSuccessfully);
})

// pass when have a alert
Cypress.Commands.add('sendDanger', (submitButton,alertDanger)=>{
    cy.get('#submitMessage').should('have.text',submitButton).click();
    cy.xpath('//*[@id="center_column"]/div/ol/li/text()').should('have.text',alertDanger);
})
