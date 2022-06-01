/// <reference types="cypress" />
Cypress.config().waitForAnimations = true;


// Testowanie aplikacji typu formularz
import { parametersContacttManager } from "../../fixtures/parametrsWebApp";

const homePage = parametersContacttManager.formURL + "index.php"
const contactPage = parametersContacttManager.formURL + "index.php?controller=contact"

// sprawdzi adres strony na której jesteśmy
const confirmURL = (url) => {
    cy.location().should(($loc=>{
            expect($loc.href).to.eq(url);
        })
    )}

describe("form veryfication tests", ()=>{
    it("should open app",()=>{
        cy.visit(parametersContacttManager.formURL);
    })

    it('Should open Contact us page and confirm URL',()=>{
        // confirmURL(homePage);
        cy.clickButton(parametersContacttManager.buttonConatactUs);
        // confirmURL(contactPage);
    })

    it("should contakt us",()=>{
        cy.contacUs(parametersContacttManager.selectChoose);
    })
    
    xit('should enter email',()=>{
        cy.enterEmail(parametersContacttManager.email);
    })

    xit('should enter order and confirm',()=>{
        cy.enterOrder(parametersContacttManager.order);
    })

    xit('should enter message to customer service',()=>{
        cy.message(parametersContacttManager.messageToService);
    })

    it('should input file',()=>{
        cy.fileUpload(parametersContacttManager.fileUpload);
    })

    xit('should send message',()=>{
        cy.send(parametersContacttManager.submitButton);
    })
})
