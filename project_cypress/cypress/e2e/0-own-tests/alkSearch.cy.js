/// <reference types="cypress" />
Cypress.config().waitForAnimations = true;


const testedPage = "https://www.kozminski.edu.pl/pl";
const course1 = "selenium"

describe("ALK search",()=>{
    it("should open tested page",()=>{
        cy.visit(testedPage);
    })

    it("should find course in search bar",()=>{
        cy.get('.agree-button').click();
        cy.get("#search").type(course1).type("{enter}");
    })

    it("schould find course on results", ()=>{
        cy.wait(2000);
        // cy.get('.search-results-block').contains(course1, {matchCase:false});
        // cy.get('.search-results-block').should('have.text', 'Programy');
        cy.get('.search-results-block').then(($block1) =>{
            expect(($block1.text())).to.include('Programy') 
        })

    })

})