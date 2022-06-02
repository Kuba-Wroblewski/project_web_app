/// <reference types="cypress" />
Cypress.config().waitForAnimations = true;


// Testowanie aplikacji typu formularz
import { parametersAccountManager } from "../../fixtures/parameters";

const registerURL = parametersAccountManager.formURL + "/register.html"
const loginURL = parametersAccountManager.formURL + "/index.html"
const loggedURL = parametersAccountManager.formURL + "/login.html"

// sprawdzi adres strony na której jesteśmy
const confirmURL = (url) => {
    cy.location().should(($loc=>{
            expect($loc.href).to.eq(url);
        })
    )}

describe("form veryfication tests", ()=>{
    it("should open app",()=>{
        cy.visit(parametersAccountManager.formURL);
    })

    it("should check all UI elements of from",()=>{
        cy.verifyForm(parametersAccountManager.role,
            parametersAccountManager.subtitle,
            parametersAccountManager.buttonText,
            parametersAccountManager.linkText)
    })

    it('should register to app',()=>{
        cy.registerToApp(parametersAccountManager.testedLogin,
            parametersAccountManager.testedPassword,
            parametersAccountManager.linkText,
            parametersAccountManager.setUpAccountText);
            confirmURL(loginURL);
    })

    it("should register to app & confirm URL",()=>{
        cy.loginToApp(parametersAccountManager.testedLogin,
            parametersAccountManager.testedPassword,
            parametersAccountManager.buttonText,
            parametersAccountManager.logoutButtonText);
            confirmURL(loggedURL);
    })

    // home work
    it('should logout from app',()=>{
        cy.logoutApp(parametersAccountManager.logoutButtonText);
        confirmURL(loginURL);
    })

})
